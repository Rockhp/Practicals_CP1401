"""JCU Grades"""

import random

def main():
    score = float(input("How much did you score (0-100): "))
    while score >= 0:
        grade = return_grade(score)
        print(f"{score} = {grade}")
        score = float(input("How much did you score (0-100): "))
    num_score = int(input("How many random scores do you want? "))
    for i in range(num_score):
        score = random.randint(0, 100)
        grade = return_grade(score)
        print(f"{score} = {grade}")


def return_grade(score):
    if score >= 85:
        return "HD"
    elif score >= 75:
        return "D"
    elif score >= 65:
        return "C"
    elif score >= 50:
        return "P"
    else:
        return "N"

main()