""" Escriba la función bmi que calcula 
el índice de masa corporal 
(bmi = peso / altura2). """
def bmi(weight, height):
    indc = round(weight / (height**2), 1)
    return 'Underweight' if indc <= 18.5 else 'Normal' if indc <= 25.0 else 'Overweight' if indc <= 30.0 else 'Obese'

# TEST CASES
print(bmi(50, 1.80))#Output Underweight
print(bmi(110, 1.80))#Output Obese
print(bmi(50, 1.50))#Output Normal