quiz={
    "what is capital of india ":"delhi",
    "Which language is used for web apps? ": "javascript"
}
score=0
print("welcome to quiz app")
print("enter your answer\n")  #\n new line
for quiz,answer in quiz.items():
    user_answer=input(f"{quiz}").lower().strip() #f formate 
    if user_answer == answer:
        print("correct answer\n")
        score= +1
    else:
        print("wrong answer")
        
print(f"Your Score: {score} out of {len(quiz)}")

#if we wanted to write formate it ahs to be on starting
        