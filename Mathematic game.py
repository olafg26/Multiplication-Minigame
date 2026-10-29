#IMPORTS
import random
import time

#VARIABLES
score = 0
play = input("Do you want to play this mathematical quiz?").lower().strip()
time.sleep(1)

#WHILE LOOP
while play == "yes":
    
#VARIABLES AND PROCESS
    number1 = random.randint(1,20)
    number2 = random.randint(1,20)
    answer = number1 * number2
    userAnswer = int(input(f"What is {number1} * {number2}?"))
    time.sleep(1)
    
#CONDITION BLOCK
    if userAnswer == answer:
        print("Well done.")
        time.sleep(1)
        score = score + 1
        print("Next question is loading...")
        time.sleep(1)
    else:
        print(f"That is incorrect. The answer was {answer}. Your score was {score}!")
        time.sleep(1)
        score = 0
        play = input("Do you want to play again?").lower().strip()
        time.sleep(1)

else:
    print("Goodbye!")
    time.sleep(1)
    
