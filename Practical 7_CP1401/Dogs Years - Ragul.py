def main():
    hum_age = 1
    while hum_age >= 0:
        hum_age = float(input("Enter the age of your dog in human years: "))
        if hum_age >=0:
            dog_age = calc_dog_age(hum_age)
            print(f"Your dog is {dog_age:.2f} dog years old.")
        else:
            print("End program")

def calc_dog_age(hum_age): # convert the age in human years to dog years
    if hum_age <= 2:
        dog_age = hum_age * 10.5
    else:
        dog_age = 21 + 4 * (hum_age - 2)
    return dog_age

main()