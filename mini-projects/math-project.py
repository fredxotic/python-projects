import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)
    expr = f"{left} {operator} {right}"
    answer = eval(expr)
    return expr, answer

wrong_attempts = 0

input("Press Enter to start the quiz!")
print("----------------------------")

start_time = time.time()

for index in range(1, TOTAL_PROBLEMS + 1):
    expr, answer = generate_problem()
    while True:
        try:
            guess = int(input(f"Problem {index}: {expr} = "))
            if guess == answer:
                break
            else:
                print("Incorrect. Try again.")
                wrong_attempts += 1
        except ValueError:
            print("Invalid input. Please enter a number.")
            wrong_attempts += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)

print("----------------------------")
print("Nice work! You finished in", total_time, "seconds.")
print("Wrong attempts:", wrong_attempts)
