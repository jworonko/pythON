import zadanie3.calculations
from Pakiety_moduly.zadanie3 import calculations

print("Oto kalulator lokaty")
initial_value = int(input("Jaką kwotę wpłacasz? "))
time = int(input("Na jaki okres? "))
percentage = int(input("Jakie jest oprocentowanie? "))

final_value = zadanie3.calculations.calculate_investment_value(initial_value, percentage, time)

print(f"Wartość Twojej lokaty wyniesie {round(final_value)}")