""" Escriba la función bmi que calcula 
el índice de masa corporal 
(bmi = peso / altura2). """
def bmi(weight, height):
    BMI = round(weight / (height**2), 1)
    if BMI <= 18.5 : return 'Underweight'
    if BMI <= 25.0 : return 'Normal'
    if BMI <= 30.0 : return 'Overweight'
    return 'Obese'

# TEST CASES
print(bmi(50, 1.80))#Output Underweight
print(bmi(110, 1.80))#Output Obese
print(bmi(50, 1.50))#Output Normal