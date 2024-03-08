weight = input ("Tell me your weight (Kg): ")
height = input (" Tell me your height (m): ")

weight = float(weight)
height = float(height)

bmi = weight / (height ** 2)
    
if 30 < bmi:
    print("Obesity")
elif 25 <= bmi <= 30:
    print("Overweight")  
elif 18.5 <= bmi < 25:
    print("Overweight")
else:
    print ("Underweight") 

print ("Your BMI is", round(bmi,2)) 
