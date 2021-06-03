""" Escriba la función bmi que calcula 
el índice de masa corporal 
(bmi = peso / altura2). """
bmi = lambda w, h : 'Underweight' if round(w / (h**2), 1) <= 18.5 else 'Normal' if round(w / (h**2), 1) <= 25.0 else 'Overweight' if round(w / (h**2), 1) <= 30.0 else 'Obese'

# TEST CASES
print(bmi(50, 1.80))#Output Underweight
print(bmi(110, 1.80))#Output Obese
print(bmi(50, 1.50))#Output Normal