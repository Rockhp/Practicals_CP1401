DISCOUNT=0.2
original_price= float(input("original price:"))
discounted_price= DISCOUNT*original_price
new_price= original_price-discounted_price
print(new_price)

MILE= 1.60934
kilometres= float(input("kilometres:"))
mile_final= MILE*kilometres
print(mile_final)

HOTEL_COST= 75
Daily_activities= float(input("Daily activities:"))
Number_of_days= float(input("Number of days:"))
Daily_food= float(input("Daily food:"))
total_cost= (Daily_food+Daily_activities+HOTEL_COST)*Number_of_days
print(total_cost)

istop = float(input("i-stop on in s: "))
time_stopped = float(input("Time stopped in s: "))
percentage = istop / time_stopped * 100
print("istop: ", round(istop/60, 0), "minute", istop%60, "seconds")
print("Time stopped: ", round(time_stopped/60, 0), "minute", time_stopped%60, "seconds")
print("Percentage:", round(percentage, 1), "%")





























