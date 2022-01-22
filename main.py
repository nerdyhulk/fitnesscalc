print("Welcome to your Health & Fitness Calculator")
name = input('What do I call you?: ')
height = float(input("Enter your height in inches(google is your friend): "))
weight = float(input("Enter your weight in lb: "))
goal = int(input("What is your goal weight? "))
age = int(input("Enter your age in years: "))
active_level = input("How active are you?(Type one of the following:Low/Light/Moderate/High/Athlete):\n").lower()

mheight = height / 39.3700787
kgweight = weight / 2.20462262
age_int = age

bmi = int(kgweight / (mheight ** 2))

print(f"Your current bmi is {bmi}")

if bmi > 25:
  print("Lets get you on the road to a healthier lifestyle")
elif bmi < 25:
  print("Way to go nerd, guess you are just here for the numbers then")  
elif active_level != "low" or active_level != "Low":
  print("Good work! It looks like you are already taking the right steps. Let's figure out your BMR and project where you will be with these changes.")
else:
  print("Lets get you started on a healthy journey by calculating your Basal Metabolic Rate...or how much your body burns on its own.")

#harris-benedict formula(1990) to find base metabolic rate
harris = round((10 * kgweight) + (6.25 * (mheight*30.48)) - (5 * age_int))

#will need to then multiple harris by activity level asked in prompt 4
if active_level == "Low" or active_level == "low":
  a = round(harris * 1.2)
  d = a - 500
  print(f"Couch Mode activated, eat {a} calories to maintain, eat {d} to start defict")
elif active_level == "Light" or active_level == "light":
  a = round(harris * 1.375)
  d = a - 500
  print(f"Starter Mode activated, eat {a} calories to maintain, eat {d} to start defict")
elif active_level == "Moderate" or active_level == "moderate":
  a = round(harris * 1.55)
  d = a - 500
  print(f"Buff Mode activated, eat {a} calories to maintain, eat {d} to start defict")
elif active_level == "High" or active_level == "high":
  a = round(harris * 1.725)
  d = a - 500
  print(f"Beast Mode activated, eat {a} calories to maintain, eat {d} to start defict")
elif active_level == "Athlete" or active_level == "athlete":
  a = round(harris * 1.9)
  d = a - 500
  print(f"You animal!! You should eat {a} calories a day! Or, eat {d} to start defict" )

period = int(input("How many months out are we looking to project your weight? "))

weight_in_lbs = float(kgweight) * 2.20462262

per_week = 1
per_month = per_week * 4
weight_loss_diet = per_month * period
result = int(weight_in_lbs) - weight_loss_diet

print(f"In a caloric defict, You should be at {result} pounds in {period} months from diet alone! Thats ~{weight_loss_diet} lbs!")

kcals_burned = int(input(f"Lets add Excercise to the equation. You said you were a '{active_level}' level of activity. How many calories do you burn per workout?:\n "))
activity = input("Through what activity are you accomplishing your goals? ")
workouts_per_week = int(input(f"How many {activity} sessions a week?: "))

total_burned_week = kcals_burned * workouts_per_week
month_cal_burned = total_burned_week * 4 
month_off_in_lb = month_cal_burned / 3500
ex_loss = round(month_off_in_lb * period)
weight_by_ex = weight - ex_loss

grand_loss = round(int(weight_loss_diet) + int(ex_loss))
target_weight = int(weight_in_lbs) - round(int(weight_loss_diet) + int(ex_loss))
new_bmi = int((target_weight/2.20462262) / (mheight ** 2))
bmi_diff = round(((bmi - new_bmi) / bmi ) * 100)

print(f"You should be burning off about {ex_loss} lbs due to {activity} in {period} months, putting you @{weight_by_ex} lbs")
print(f"Combined, you should lose {grand_loss} lbs from diet and {activity}. Making you {target_weight} lbs!!")
print(f"Your new BMI then would be {new_bmi}. That is a -{bmi_diff}% drop!")
