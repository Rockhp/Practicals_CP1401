
"""Coffee Brew Ratio"""

def main():
    cof_dose = float(input("Enter the dose: "))
    cof_yield = float(input("Enter the yield: "))
    cof_ratio = calculate_ratio(cof_dose, cof_yield)
    cof_type = determine_type(cof_ratio)
    print(f"The ratio of the coffee is 1:{cof_ratio:.2f},and it's a {cof_type}.")

def calculate_ratio(cof_dose, cof_yield):
    return cof_yield / cof_dose

def determine_type(cof_ratio):
    if cof_ratio < 2:
        return "ristretto"
    elif 2 > cof_ratio >= 3:
        return "normale"
    else:
        return "lungo"

main()