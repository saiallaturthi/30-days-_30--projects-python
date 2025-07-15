def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def cm_to_inches(cm):
    return cm / 2.54

def inches_to_cm(inches):
    return inches * 2.54

def main():
    print("🔄 Unit Converter")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    print("3. Centimeters to Inches")
    print("4. Inches to Centimeters")

    choice = input("Choose a conversion (1-4): ")

    if choice == '1':
        km = float(input("Enter kilometers: "))
        print(f"{km} km = {km_to_miles(km):.2f} miles")
    elif choice == '2':
        miles = float(input("Enter miles: "))
        print(f"{miles} miles = {miles_to_km(miles):.2f} km")
    elif choice == '3':
        cm = float(input("Enter centimeters: "))
        print(f"{cm} cm = {cm_to_inches(cm):.2f} inches")
    elif choice == '4':
        inches = float(input("Enter inches: "))
        print(f"{inches} inches = {inches_to_cm(inches):.2f} cm")
    else:
        print("❌ Invalid option. Please try again.")

if __name__ == "__main__":
    main()
