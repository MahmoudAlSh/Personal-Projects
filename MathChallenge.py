import random
import time

OPERATORS = ["+", "-", "*"]
# Easy Mode
MAX_OPERAND = 5
MIN_OPERAND = 2
TOTAL_PROBLEMS = 3
# Normal Mode
NMAX_OPERAND = 10
NMIN_OPERAND = 4
NTOTAL_PROBLEMS = 7
# Hard Mode
HMAX_OPERAND = 15
HMIN_OPERAND = 5
HTOTAL_PROBLEMS = 10

playmode = input("Choose difficulty: for Easy Mode enter E, Normal Mode enter N, Hard Mode enter H: ")

if playmode.lower() == 'e':
    def generate_problem():
        left = random.randint(MIN_OPERAND, MAX_OPERAND)
        right = random.randint(MIN_OPERAND, MAX_OPERAND)
        operator = random.choice(OPERATORS)

        expr = str(left) + " " + operator + " " + str(right)
        answer = eval(expr)
        return expr, answer

    wrong = 0
    input("Press enter to start")
    print("-----------------------")

    start_time = time.time()

    for i in range(TOTAL_PROBLEMS):
        expr, answer = generate_problem()
        while True:
            guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")  
            if guess == str(answer):
                break
            wrong += 1

    end_time = time.time()
    total_time = round(end_time - start_time, 2)

    print("-----------------------")
    print("Nice work! You finished in", total_time, "seconds")

elif playmode.lower() == 'n':
    def generate_problem():
        left = random.randint(NMIN_OPERAND, NMAX_OPERAND)
        right = random.randint(NMIN_OPERAND, NMAX_OPERAND)
        operator = random.choice(OPERATORS)

        expr = str(left) + " " + operator + " " + str(right)
        answer = eval(expr)
        return expr, answer

    wrong = 0
    input("Press enter to start")
    print("-----------------------")

    start_time = time.time()

    for i in range(NTOTAL_PROBLEMS):
        expr, answer = generate_problem()
        while True:
            guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")  
            if guess == str(answer):
                break
            wrong += 1

    end_time = time.time()
    total_time = round(end_time - start_time, 2)

    print("-----------------------")
    print("Nice work! You finished in", total_time, "seconds")

elif playmode.lower() == 'h':
    def generate_problem():
        left = random.randint(HMIN_OPERAND, HMAX_OPERAND)
        right = random.randint(HMIN_OPERAND, HMAX_OPERAND)
        operator = random.choice(OPERATORS)

        expr = str(left) + " " + operator + " " + str(right)
        answer = eval(expr)
        return expr, answer

    wrong = 0
    input("Press enter to start")
    print("-----------------------")

    start_time = time.time()

    for i in range(HTOTAL_PROBLEMS):
        expr, answer = generate_problem()
        while True:
            guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")  
            if guess == str(answer):
                break
            wrong += 1

    end_time = time.time()
    total_time = round(end_time - start_time, 2)

    print("-----------------------")
    print("Nice work! You finished in", total_time, "seconds")

