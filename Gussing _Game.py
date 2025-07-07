import random

print("welocme to gussing game")
print("guess a number between 1 to 100")

secrete_num=random.randint(1,100)

while True:
    a=input("guess number: ")
    b=int(a)
    if secrete_num > b:
        print("number is low")
    elif secrete_num < b:
        print("number is high")
    else:
        print("you guessed it right")
        break
        
    
    
    
    
    
    
    
    
    