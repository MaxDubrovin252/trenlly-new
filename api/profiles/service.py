def overweight(weight:int,height:int)->bool:
    height_m = height / 100.0
    # Calculate BMI
    bmi = weight / (height_m ** 2)
    # Check if the BMI is 25 or greater
    return bmi >= 25
    