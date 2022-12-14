def main():
    height = 1.75
    for weight in range(50, 101, 2):
        bmi = calc_bmi(height, weight)
        cat = determine_bmi_category(bmi)
        print(f"Height {height}m, Weight {weight:3}kg = BMI {bmi:.1 f}, considered {cat}")


def calc_bmi(height, weight):
    return weight / (height ** 2)


def determine_bmi_category(bmi):
    if bmi < 18.5:
        return "underweight"
    elif bmi < 25:
        return "normal"
    elif bmi < 30:
        return "overweight"
    else:
        return "obese"


main()