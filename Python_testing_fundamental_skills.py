import math
import random

MIN_VALUE = 1
MAX_VALUE = 99

def main():
    print("STEM 2 Academy")
    random_n1 = random.randint(MIN_VALUE, MAX_VALUE)
    random_n2 = random.randint(MIN_VALUE, MAX_VALUE)
    random_question = print("What is", str(random_n1), "+", str(random_n2))
    user_answer = (int(input("Your answer: ")))
    add_problem = int(random_n1) + random_n2 
    if add_problem == user_answer:
        print("Correct.")

    else:
        print("Incorrect.")
        print("The expected answer is", add_problem)
    
    
    
    
if __name__ == '__main__':
    main()
