import streamlit as st
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# --- Helpers ---
def human_delay(a=2, b=5):
    time.sleep(random.uniform(a, b))

def human_typing(element, text):
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(0.1, 0.3))

# --- Dice automation function ---
def run_dice_automation(email, password, technology):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)

    # Step 1: Login
    driver.get("https://www.dice.com/dashboard/login")
    human_delay(5, 8)

    email_box = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='email']"))
    )
    human_typing(email_box, email)
    email_box.send_keys(Keys.RETURN)
    human_delay(3, 6)

    password_box = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='password']"))
    )
    human_typing(password_box, password)
    password_box.send_keys(Keys.RETURN)
    human_delay(5, 8)

    # Step 2: Go to job search page
    tech_query = technology.replace(" ", "+")
    driver.get(
        f"https://www.dice.com/jobs?filters.easyApply=true&filters.postedDate=ONE&filters.employmentType=PARTTIME%7CCONTRACTS&q={tech_query}"
    )
    human_delay(5, 8)

    # Step 3: Collect job links
    job_links = [
        link.get_attribute("href")
        for link in driver.find_elements(
            By.CSS_SELECTOR,
            "a.text-xl.font-semibold.text-zinc-800.no-underline.hover\\:underline",
        )
        if link.is_displayed()
    ]

    st.write(f"📌 Found **{len(job_links)}** jobs for `{technology}`")

    applied_jobs, skipped_jobs, error_jobs = [], [], []

    # Step 4: Loop through jobs
    for job_url in job_links:
        driver.execute_script("window.open(arguments[0], '_blank');", job_url)
        driver.switch_to.window(driver.window_handles[-1])
        human_delay(5, 8)

        # --- Get Job Title ---
        try:
            job_title = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "h1[data-cy='jobTitle']"))
            ).text.strip()
        except:
            job_title = "Unknown Title"

        st.write(f"🔎 Opened Job: **{job_title}**  \n🔗 {job_url}")

        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "apply-button-wc"))
            )
            apply_button = driver.execute_script("""
                let el = document.querySelector("apply-button-wc");
                if (el && el.shadowRoot) {
                    return el.shadowRoot.querySelector("button.btn.btn-primary");
                }
                return null;
            """)
            if apply_button:
                st.info(f"➡️ Starting Easy Apply for **{job_title}**")
                driver.execute_script("arguments[0].click();", apply_button)
                human_delay(4, 7)

                # Next → Submit loop
                try:
                    while True:
                        try:
                            next_btn = WebDriverWait(driver, 3).until(
                                EC.presence_of_element_located(
                                    (By.CSS_SELECTOR, "button.seds-button-primary.btn-next")
                                )
                            )
                            st.info("➡️ Clicking Next...")
                            driver.execute_script("arguments[0].scrollIntoView(true);", next_btn)
                            driver.execute_script("arguments[0].click();", next_btn)
                            human_delay(2, 4)
                        except:
                            break

                    submit_btn = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located(
                            (By.CSS_SELECTOR, "button[data-cy='form-step-submit-button']")
                        )
                    )
                    st.info("➡️ Clicking Submit...")
                    driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
                    driver.execute_script("arguments[0].click();", submit_btn)
                    st.success(f"✅ Successfully applied for **{job_title}**")
                    applied_jobs.append((job_title, job_url))

                except Exception:
                    st.warning(
                        f"Applied **{job_title}**  \n🔗 {job_url}"
                    )
                    skipped_jobs.append((job_title, job_url))
            else:
                st.warning(f"⚠️ No Easy Apply button for **{job_title}**  \n🔗 {job_url}")
                skipped_jobs.append((job_title, job_url))
        except Exception:
            st.error(f"❌ Error while applying for **{job_title}**  \n🔗 {job_url}")
            error_jobs.append((job_title, job_url))

        human_delay(5, 10)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    # --- Final Summary ---
    st.subheader("📊 Summary")
    st.write(f"✅ Applied: {len(applied_jobs)}")
    st.write(f"⚠️ Skipped: {len(skipped_jobs)}")
    st.write(f"❌ Errors: {len(error_jobs)}")

    if applied_jobs:
        st.write("### ✅ Applied Jobs")
        for title, url in applied_jobs:
            st.write(f"- **{title}**  \n🔗 {url}")

    if skipped_jobs:
        st.write("### ⚠️ Skipped Jobs")
        for title, url in skipped_jobs:
            st.write(f"- **{title}**  \n🔗 {url}")

    if error_jobs:
        st.write("### ❌ Error Jobs")
        for title, url in error_jobs:
            st.write(f"- **{title}**  \n🔗 {url}")

    driver.quit()

# --- Streamlit UI ---
st.title("🎯 Joyce Easy Apply Automation")
st.write("Enter your Dice credentials and technology to start automation.")

email = st.text_input("Dice Email")
password = st.text_input("Dice Password", type="password")
technology = st.text_input("Technology (e.g., Data Engineer)")

if st.button("Start Automation"):
    if not email or not password or not technology:
        st.error("Please provide all fields!")
    else:
        st.success(f"🚀 Starting automation for `{technology}`...")
        run_dice_automation(email, password, technology)
