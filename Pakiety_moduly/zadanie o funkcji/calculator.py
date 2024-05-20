import funkcje

print("To jest kalkulator lokat")

initial_value = int(input("Jaka jest wartość lokaty? "))
percentage = int(input("Jakie oprocentowanie? "))
years = int(input("na jaki okres czasu? "))

final_value = funkcje.calculate_investment_value(initial_value, percentage, years)

print(f"Wartość Twojej lokaty po {years} latach będzie wynosiła {final_value:.2f}")


longer_term = years * 2
alternative_value = funkcje.calculate_investment_value(initial_value, percentage, longer_term)
print(f"Rozważ zostawienie lokaty na {longer_term} lat - będzie wtedy warta {alternative_value:.2f}")
