from typing import Dict, List

python_age = 30

# info = "Python ma już prawie: " + str(python_age) + "lat!"
# print(info)

# info = f"Python ma już prawie {python_age} lat!"
# print(info)

# calculation = f"Wynik działania 3 x 6 to {3 * 6}"
# print(calculation)
#
# name = input("Jak masz na imię?")
# Hello = f"Nazywam się {name}"
# print(Hello)

# your_street = input("Na jakiej ulicy mieszkasz? ")
# print(f"Nazwa tej ulicy ma aż {len(your_street)} liter!")

# big_letters = "mówię głośno!"
# print(big_letters.upper())
#
# small_letters = "CICHO I SPOKOJNIE"
# print("mówię " + small_letters.lower())

# all_upper = "RóŻnE RoZmiaRy Liter".upper()
# print(all_upper)

# name = input("Jak się nazywasz? ")
# print(f"Nazywam się: {name.title()}")

# phone_number = input("Jaki masz numer telefonu? ")
# phone_number_with_dash = phone_number.replace(' ', "-")
# print(phone_number_with_dash)

# prel_value = int(input("Ile wpłasciłeś na lokatę? "))
# time = int(input("Na jaki okres jest lokata? "))
# percentage = int(input("jakie oprocentowanie? "))
#
# print(f"Wartość twojej lokaty wyniesie: {round(prel_value * (1 + percentage/100) ** time, 2)} zł")

# name = input("Jak masz na imię? ")
# print(f"Twoje imię zawiera aż: {len(name)} liter")

# city = input("Gdzie mieszkasz? ")
# print(f"Jak miło, że mieszkasz {city.title()}")

# ford = "ab100100"
# audi = "EEE 123123"
# citroen = "Zk-300300"
# honda = "AB210210"

# print(ford.upper())
# print(audi.replace(' ',''))
# print(citroen.replace('-', '').upper())
# print(honda)

# home = input("W jakim mieście mieszkasz?\n")

list = [
    "chleb",
    "mąka",
    "cukier"
]
# print("Druga pozycja listy to:", list[1])
# print(f"Na liście są: {len(list)} pozycje")
# print("Ostatnia rzecz na liście to:", list[-1])

# print("Dwie najważniejsze rzeczy to:", list[:2])
# list.append("woda")
# print(list)
# list.insert(0, "woda")
# print(list)
# del list[2]
# print(list)
# druga_rzecz = list.pop(1)
# print(druga_rzecz)
#
# list.remove("chleb")
# print(list)

# name = "Joanna"
# print("Pierwsza litera to: ", name[0])
# print("Ostatnia litera to: ", name[-1])
# print("Wszystkie litery poza pierwsza i druga to:", name[2:])

# name = "M" + name[1:]
# print(name)

# words = "To jest całe zdanie".split(" ")
# print(words)
# print("Pierwsze słowo:", words[0])

#zadanie nr 1
# favourite_sports = ["pływanie",
#                     "bieganie",
#                     "jazda na rowerze",
#                     "siatkówka",
#                     "koszykówka"]
# print("Pierwsza pozycja na liście to", favourite_sports[0])
# print("Ostatnia pozycja na liście to", favourite_sports[-1])
# favourite_sports[1] = "triathlon"
# print(favourite_sports)

# #zadanie nr 2
# dishes = input("Podaj trzy ulubione potrawy ")
# favourite_dishes = dishes.split(',')
# print(favourite_dishes)
#
# zadanie nr 3
# users_nr_tel = input("Podaj swój numer telefonu ")
# secret_users_nr_tel = users_nr_tel[:6]
# print(f"Twoj tajny numer telefonu to: ", {secret_users_nr_tel + "---"})

# pol_eng = {
#     "amnezja": "amnesia",
# }
# print(pol_eng)
#
# print(f"Po polsku 'amnezja' to po angielsku '{pol_eng['amnezja']}")

# empty = {}
# print("Pusty słownik:", empty)


# teacher = {
#    "first_name": "Jan",
#     "last_name": "Kowalski",
#     "age": 45,
#     "contract": {
#         "sign_date": "23-11-2018",
#         "salary": 3500
#     }
# }
# print(teacher)
#
# teacher["first_name"] = "Albert"
# print(teacher)

# teacher["city"] = "Gdańsk"
# print(teacher)

# del teacher["last_name"]
# print(teacher)
#
# print(teacher["first_name"])
# print(teacher["age"])

# age = teacher.pop("age")
# print(age)
# print(teacher)

# print(teacher.keys())
# print(teacher.values())
# keys = list((teacher.keys()))
# print(keys)

#zadanie nr 1
# print("Dziennik ucznia:")
# dziennik_ucznia = {
#     "matematyka": [5, 4, 3, 2, 1],
#     "historia": [4, 4, 4],
#     "jezyk_polski": [4.5, 5.5, 6],
#     "biologia": [3],
#     "w_f": [6, 5],
# }
# print(dziennik_ucznia)

#zadanie nr 2
# my_family = {
#     "ja": {
#     "imie": "Joanna",
#     "nazwisko": "Woronko",
#     "data urodzenia": "01-10-1989",
#     "parents": [
#         "mama": {
#          "imie": "Barbara",
#         "nazwisko": "Wiland",
#         "data urodzenia": "26-05-1963",}
#     ]
#
#     }
# }
# }
# print(my_family)

# zadanie nr 3
# jedzenie = int(input("Ile wydajesz na jedzenie? " ))
# rozrywka = int(input("Ile wydajesz na rozrywkę? "))
# opłaty = int(input("Ile wydajesz na opłaty ? "))
# inne =  int(input("Ile wydajesz na inne rzeczy? "))
#
# wszystkie_wydatki = (jedzenie + rozrywka + opłaty + inne)
# wszystkie_wydatki_perc = {
#     "jedzenie": jedzenie * 100 / wszystkie_wydatki,
#     "rozrywka": rozrywka * 100 / wszystkie_wydatki,
#     "opłaty": opłaty * 100 / wszystkie_wydatki,
#     "inne": inne * 100 / wszystkie_wydatki,
# }
#
# wybrana_kategoria = input("Wybierz jedną kategorią spośród (jedzenie, rozrywka, opłaty, inne: ")
# print(f"Na {wybrana_kategoria} wydajesz {wszystkie_wydatki_perc[wybrana_kategoria]:.0f} % wszystkich wydatków")


# print(f"Jedzenie stanowi", round(((jedzenie / wszystkie_wydatki) * 100), 0), " % wszystkich Twoich wydatków")
# print(f"Rozrywka stanowi", round(((rozrywka / wszystkie_wydatki) * 100), 0),  " % wszystkich Twoich wydatków")
# print(f"Opłaty stanowią", round(((opłaty / wszystkie_wydatki) * 100), 0),  " % wszystkich Twoich wydatków")
# print(f"Inne rzeczy stanowią", round(((inne / wszystkie_wydatki) * 100), 0),  " % wszystkich Twoich wydatków")

# nothing = None
# print(f"Nic: {nothing}")
#
# print(f"None jest typu: {type(None)}")

# people = [
#     {
#         "name": "Joanna",
#         "car": {
#             "brand": "Toyota",
#             "year": 2015
#         }
#     },
#     {
#         "name": "Maria",
#         "car": None
#     }
# ]
# print(people)

# none_str = str(None)
# print("abc" + none_str)

# apples = 3
# banana = 4.5
# pears = 3
#
# print(f"Czy jabłka są droższe od bananow? \n\t\t\t\t\t {apples > banana}")



# name = "Joanna"
# result = name == "Joanna"
# print(f"name == 'Joanna' -> {result}")

# your_name = input("Jak masz na imię ")
# are_you_joanna = your_name == "Joanna"
# print(f"Twoje imię to Joanna? {are_you_joanna}")

# print(f"Warzywa > Owoce -> {'Warzywa' > 'Owoce'}")

# lista = ["mąka", "jogurt"]
# my_list = ["czekolada", "marchew", "buraki"]
# print(f"{lista} > {my_list} -> {lista > my_list}")

# jablka = input("Ile kosztują jabłka? ")
# banany = input("ile kosztują banany? ")
# mąka = input("Ile kosztuje mąka? ")
#
# print(f"jablka są droższe od bananów: \t\t\t {jablka > banany}")
# print(f"mąka kosztuje tyle samo co jabłka: \t\t\t {mąka == jablka}")

# lista_zakupów = input("Wypisz listę zakupów oddzielając poszczególne rzeczy przecinkami")
# print(f"Twoja lista zakupów ma {len(lista_zakupów.split(','))} pozycji")
# if len(lista_zakupów.split(',')) >= 5:
#     print("Twoja lista jest długa")


# name = input("Jak sie nazywasz? ")
# print(f"Miło Cię poznać {name}")
#
# if len(name) >=7:
#     print(f"{name} to całkiem długie imię!")
# else:
#     print(f"{name} to raczej krótkie imię!")

# age = int(input("Ile masz lat? "))
# if age < 18:
#     print("Jeszcze nie możesz głosować")
# else:
#     print("Już możesz głosować")
#     if age >= 21:
#         print("Możesz kandydować na posła")
#     if age >= 30:
#         print("Możesz kandydować na senatora")
#     if age >= 35:
#         print("Możesz kandydować na prezydenta")

# name = input("Jak masz na imię? ")
#
# if name[-1] == "a":
#     print("to znaczy, że jesteś kobietą")
# else:
#     print("To znaczy, że jesteś mężczyzną")
#
# computer_price = float(input("Ile średnio kosztuje komputer? "))
# car_price = float(input("Jaka jest cena samochodu? "))
# bike_price = float(input("Ile średnio kosztuje rower? "))
#
# if computer_price > car_price:
#     print("Komputer jest droższy niż samochód")
# else:
#     print("Komputer jest tańszy ")
#
# shopping_elements = input("Wprowadz listę zakupów, oddzielając przecinkiem ")
# shopping_list = shopping_elements.split(",")
#
# if len(shopping_list) > 3:
#     print("Ale długa lista zakupów")
# else:
#     print("To jest krótka lista zakupów")

# income = float(input("Jaki jest miesięczny przychód? "))
# employees = int(input("Ilu pracowników zatrudniasz? "))
# support_answer = input("Czy Twoja firma otrzymała już dotacje? (T/N) ")
#
# if support_answer == "T":
#     support_used = True
# else:
#     support_used = False
#
# if not support_used and (income < 15500 or employees >=3):
#     print("Możesz otrzymać dotacje")
# else:
#     print("Nie możesz otrzymać dotacji")

# if not 3 < 2:
#     print("3 nie jest mniejsze od 2")

# income = 4000
# expenditures = 2000
# age = 30
#
# if age < 18 or income < expenditures:
#     print("Nie możesz wziąć kredytu")
# else:
#     print("Możesz wziąć kredyt")

# kwota_kredytu = float(input("Jaką kwotę kredytu potrzebujesz? "))
# oprocentowanie = float(input("Jakie jest oprocentowanie w %? "))
# wkład = float(input("Jaki masz wkład własny? "))
# czas_kredytu = float(input("Na ile lat chcesz wziąć kredyt? "))
# przychod = float(input("Jakie masz miesięczne przychody? "))
# wydatki = float(input("Jakie masz miesięczne wydatki? "))
#
# wysokość_raty = round((kwota_kredytu * oprocentowanie / 100)) / 12 + (kwota_kredytu / (czas_kredytu * 12))
# print("Wysokość Twojej raty będzie wynosiła", wysokość_raty)
#
# dostępne_środki = przychod - wydatki
# print("Twoje dostępne środki miesięcznie wynoszą", dostępne_środki)
#
# wartość_nieruchomości = wkład + kwota_kredytu
# print("Wartość nieruchomości wyniesie", wartość_nieruchomości)
#
# if wkład >= (0.2 * wartość_nieruchomości) and dostępne_środki > 1000:
#     print("Możesz otrzymać kredyt")
# else:
#     if wkład >= (0.1 * wartość_nieruchomości) and wkład < (0.2 * wartość_nieruchomości) and dostępne_środki > 2000:
#         print("Możesz otrzymać kredyt")
#     else:
#         print("Nie możesz otrzymać kredytu")
# if not wkład > (0.1 * wartość_nieruchomości):
#     print("Nie możesz otrzymać kredytu")

# Mamy 4 rodzaje wsparcia - od najlepszych do najgorszych są to:
# - Główne wsparcie -> przychód poniżej 5000
# - Wsparcie z funduszu pracowników -> od 5 do 10 pracowników
# - Wsparcie dla nowych firm -> krócej niż 3 lata na rynku
# - Wsparcie na pocieszenie -> dla każdego kto nie dostał żadnego innego

income = 5000
employees_number = 7
years_on_the_market = 3

# if income < 5000:
#     print("Otrzymujesz główne wsparcie")
# elif 5 < employees_number < 10:
#         print("Otrzymujesz wsparcie z funduszu pracowników")
# elif years_on_the_market < 3:
#         print("Otrzymujesz wsparcie dla nowych pracowników")
# else:
#     print("Otrzymujesz wsparcie na pocieszenie")
#

# age = int(input("Ile masz lat? "))
# gender = input("Jesteś kobietą czy mężczyzną K/M? ")
# result = int(input("Jaki był Twój wynik biegu w metrach na 12 min? "))
#
# if 20 < age < 29:
#     if gender == "M":
#         if result >= 2800:
#             print("Bardzo dobrze!")
#         elif 2400 < result < 2800:
#             print("Dobrze!")
#         elif 2200 < result < 2399:
#             print("Średnio")
#         elif 1600 < result < 2199:
#             print("Źle")
#         else:
#                 print("Bardzo źle")

# name = input("Jak masz na imię? ")
# if "a" in name:
#     print("W Twoim imieniu jest 'a'")

# sports = ["koszykówka", "siatkówka", "pływanie"]
# if "pływanie" in sports:
#     print("O, widzę, że lubisz pływać")

# person = {
#     "first_name": "Joanna",
#     "last_name": "Woronko",
# }
#
# if "first_name" in person:
#     print(person["first_name"])

# age = 45
# # if age:
# #     print("if age")
#
# # if age is True:
# #     print("age is True")
#
# true_value = True
# if true_value is True:
#     print("true_value is True")
#
# nothing = None
# if not nothing:
#     print("if not nothing")
#
# zero = 0
# if not zero:
#     print("if not zero")
#
# if zero is None:
#     print("zero is None")

#Zadanie nr 2
# tel_number = input("Jaki jest Twój numer telefonu? ")
# if "0" in tel_number:
#     print("Twój numer zawiera '0'")
# else:
#     print("Twój numer nie zawiera '0'")

#Zadanie nr 1
# shopping_list = input("Podaj listę zakupów oddzielając je przecinkiem. ")
# shopping_list_list = shopping_list.split(",")
#
# if "chleb" in shopping_list or "bułki" in shopping_list_list:
#     print("O, widzę, że potrzebujesz pieczywo")
# else:
#     print("Nie potrzebujesz pieczywa?")

# zadanie nr 3
# value = True
# if value is True:
#     print("to prawda")
# elif value is False:
#     print("to fałsz")
# elif value is None:
#     print("to None")
# else:
#     print("To inna wartość")

# counter = 0
# while counter <= 30:
#     print(counter)
#     counter += 1

# expected_potatoes = int(input("Ile ziemniaków zjesz na obiad? "))
# potatoes = []
# while len(potatoes) < expected_potatoes:
#     print("Obieram ziemniaka...")
#     print("I wrzucam go do garnka...")
#     potatoes.append("Ziemniak")
#     print(potatoes)

# number = int(input("Podaj liczbę większą niż 100 " ))
# while number <= 100:
#     print(f"{number} nie jest większa niż 100, spróbujmy jescze raz")
#     number = int(input("Podaj liczbę większą niż 100 "))
# print(f"Brawo")

# favourite_sports = ["pływanie", "biagenie", "jazda na rowerze", "triathlon"]
# sport_index = 0
# while sport_index < len(favourite_sports):
#     print(favourite_sports[sport_index])
#     sport_index += 1

# favourite_sports = ["pływanie", "biagenie", "jazda na rowerze", "triathlon"]
# sport_index = 0
# while sport_index < len(favourite_sports):
#     if sport_index % 2 == 0:
#         print(favourite_sports[sport_index])
#     sport_index += 1

# numbers = [1, 3, 510, 123, 24]
# numbers_sum = 0
# number_index = 0
# while number_index < len(numbers):
#     numbers_sum += numbers[number_index]
#     number_index += 1
# print(f"Suma: {numbers_sum}")

# post_code = input("Jaki jest Twój kod pocztowy?")
# post_code = post_code.replace("-", "")
# formatted_post_code = ""
# letter_index = 0
# while letter_index < len(post_code):
#     if letter_index % 2 == 0 and letter_index !=0:
#         formatted_post_code += "-"
#     formatted_post_code += post_code[letter_index]
#     letter_index += 1
# print(formatted_post_code)

#Zadanie 1
# number = int(input("Podaj liczbę parzystą "))
# counter = 1
# while not counter < 10 and (number % 2 != 0):
#     number = int(input("To nie jest liczba parzysta, spróbuj jeszcze raz"))
# counter += 1
# print(counter)
# if counter == 10:
#     print("Wykorzystałes 10 prób, koniec gry")
# else:
#     print("Brawo!")

#Zadanie 2
# phone_number = input("Jaki masz numer telefonu? ")
# phone_number_with_dash = phone_number.replace(' ', "-")
# print(phone_number_with_dash)

# phone_number = input("Podaj swój numer telefonu ")
# phone_number = phone_number.replace("-", " ")
# formatted_phone_number = ""
# digit_index = 0
# while digit_index < len(phone_number):
#     if digit_index % 3 == 0 and digit_index !=0:
#          formatted_phone_number += "-"
#     formatted_phone_number += phone_number[letter_index]
#     digit_index += 1
# print(formatted_phone_number)

# dishes = input("Podaj swoje ulubione dania, oddzielając je przecinkiem ")
# favourite_dishes = dishes.split(",")
#
# dish_index = 0
# while dish_index < len(favourite_dishes):
#     print(f"Ulubione danie numer {dish_index}: {favourite_dishes[dish_index]}")
#     dish_index += 1

# favourite_sports = ["bieganie", "pływanie", "piłka", "koszykówka"]
# for sport in favourite_sports:
#     print(sport)
#
# post_code = input("Jaki jest Twoj kod pocztowy")
# for letter in post_code:
#     print(letter)
#
# wydatki  = {
#     "prąd": [150],
#     "woda": [20],
#     "zakupy": [
#         500,
#         170,53,
#         10.15,
#     ]
# }

# for wydatki_name in wydatki:
#     print(f"{wydatki_name} -> {wydatki[wydatki_name]}")
#

# for wydatki in wydatki.values():
#     print(wydatki)

# for wydatki_name, wydatki in wydatki.items():
#     print(f"{wydatki_name} -> {wydatki}")

# for item in wydatki.items():
#     print(item)
#     print(f"{item[0]} -> {item[1]}")
#     print(type(item))

# item = ["prąd", 240]
# item[1] = 20
# print(item)

# item = ("prąd", 240)
# name, value = item
# print(name, value)

# post_code = input("Jaki jest Twój kod pocztowy? ")
# for index, letter in enumerate(post_code):
#     print(f"[{index}] -> {letter}")

# favourite_sports = ["bieganie", "pływanie", "piłka", "koszykówka"]
# for index, sport in enumerate(favourite_sports):
#     if index % 2 == 0:
#         print(sport)


# post_code = input("Jaki jest Twój kod pocztowy? ")
# post_code = post_code.replace("-", "")
# formatted_post_code = ""
# for index, letter in enumerate(post_code):
#     if index % 2 == 0 and index !=0:
#         formatted_post_code += "-"
#     formatted_post_code += letter
# print(formatted_post_code)

# phone_number = input("Podaj swój numer telefonu ")
# phone_number = phone_number.replace("-", " ")
# formatted_phone_number = ""
# for index, number in enumerate(phone_number):
#     if index % 3 == 0 and index !=0:
#          formatted_phone_number += "-"
#     formatted_phone_number += number
# print(formatted_phone_number)

# grades = []
# grade_input = input("Podaj kolejną ocenę lub zakończ wpisująć 'X': ")
# while grade_input != 'X':
#     grade = int(grade_input)
#     grades.append(grade)
#     grade_input = input("Podaj kolejną ocenę lub zakończ wpisując 'X': ")
#
# grades_sum = 0
# for grade in grades:
#     grades_sum += grade
#
# avarage = grades_sum / len(grades)
# print(f"Twoja średnia wynosi: {avarage:2f} ")
#
# print("Kalkulator budżetu miesięcznego")
# expenditures = {}
#
# category_name = input("Podaj kategorię wydatków albo zakończ wpisując 'X': ")
# while category_name != 'X':
#     expenditures[category_name] = []
#     expenditure = input(f"Podaj wartość następnego wydatku w kategorii {category_name} albo zakończ wpisując 'X': ")
#     while expenditure != 'X':
#         expenditure_value = float(expenditure)
#         expenditures[category_name].append(expenditure_value)
#         expenditure = input(f"Podaj wartość następnego wydatku w kategorii {category_name} albo zakończ wpisując 'X': ")
#     category_name = input("Podaj kategorię wydatków albo zakończ wpisując 'X': ")
#
#
# total_expenditures = 0
# for category_expenditures in expenditures.values():
#     for expenditure_value in category_expenditures:
#         total_expenditures += expenditure_value
#     # total_expenditures += sum(category_expenditures)
#
#
# expenditures_percentage = {}
# for category_name, category_expenditures in expenditures.items():
#     total_category_expenditures = 0
#     for expenditure_value in category_expenditures:
#         total_category_expenditures += expenditure_value
#     # total_category_expenditures = sum(category_expenditures)
#     expenditures_percentage[category_name] = total_category_expenditures * 100 / total_expenditures
#
# most_important_category = None
# most_important_category_percentage = 0
# for category, percentage in expenditures_percentage.items():
#     if percentage > most_important_category_percentage:
#         most_important_category_percentage = percentage
#         most_important_category = category
#
# if most_important_category is not None:
#     print(f"Najwięcej wydajesz na {most_important_category} - {most_important_category_percentage:.0f}% wszystkich wydatków")
#
# for category, percentage in expenditures_percentage.items():
#     print(f"Na {category} wydajesz {percentage:.0f}% miesięcznych wydatków")

# for number in range(12):
#     print(number)
#
# for number in range(1,13):
#     print(number)

# for number in range(1,13,4):
#     print(number)

# print("Kalkulator wartości lokaty z roczną kapitalizacją")

# initial_value_input = input("Jaką kwotę wpłaciłeś/wpłaciłaś? ")
# initial_value = int(initial_value_input)
# percentage_input = input("Jakie jest oprocentowanie (%)? ")
# percentage = int(percentage_input)
# years_input = input("Ile lat trwa lokata? ")
# years = int(years_input)
#
# for year_number in range(1, years + 1):
#     investment_value = initial_value * (1 + percentage / 100) ** year_number
#     print(f"Po {year_number} latach Twoja lokata będzie warta {investment_value:.2f}")

# sentence = "Napis z dużą liczbą aaa - sia laaa laaa"
# print(sentence.count(("a")))

# phone_number = input("Jaki jest Twoj numer telefonu? ")
# for digit in range(10):
#     digit_times_in_number = phone_number.count(str(digit))
#     print(f"Cyfra {digit} występuje: {digit_times_in_number} razy")

# favourite_sports = ["bieganie", "pływanie", "piłka", "koszykówka"]
# for index, sport in enumerate(favourite_sports):
#     if index % 2 != 0:
#         continue
#     print(sport)

# numbers = [1, 3, 4, 66, 88, 97, 43]
# for number in numbers:
#     if number % 2 == 0:
#         continue
#     print(number)

# def pole_prostokąta(length, width):
#     return length * width
# print(f"Pole prostokąta o bokach 5 i 18 to {pole_prostokąta(5,18)}")
#
# def avarage_speed(distance, time):
#     return distance / time
#
# run_distance = float(input("Ile ostatnio przebiegłes? "))
# run_time = float(input("Ile Ci to zajęło "))
# bike_distance = float(input("Ile ostatnio przejechałeś rowerem? "))
# bike_time = float(input("Ile Ci to zajęło "))
# car_distance = float(input("Ile przejechałeś autem? "))
# car_time = float(input("Ile Ci to zajęło "))

# print(f"Twoja średnia prędkość biegu to {round(avarage_speed(run_distance, run_time))} km/h")
# print(f"Twoja średnia prędkość jazdy na rowerze to {avarage_speed(bike_distance, bike_time)} km/h")
# print(f"Twoja średnia prędkość jazdy autem to {avarage_speed(car_distance, car_time)} km/h")

# def calculate_investment_value (initial_value, percentage, years):
#     result = initial_value * (1 + percentage / 100) ** years
#     return result
#
# initial_value = 1000
# percentage = 4
# years = 5
#
# final_value = calculate_investment_value(1000, 4, 5 )
# print(f"Po 4 latach Twoja lokata będzie warta {final_value:.2f}")

# def avg_speed(distance, time):
#     return distance / time

# def avg_run_speed_calculator(vechicle_name):
#     distance = float(input(f"Ile ostatnio pokonałeś za pomocą {vechicle_name}? "))
#     time = float(input("Ile Ci to zajęło "))
#     avarage_speed = avg_speed(distance=distance, time=time)
#     print(f"Twoja średnia prędkość przemieszczania się za pomocą {vechicle_name} to {avarage_speed} km/h")
#
# avg_run_speed_calculator(vechicle_name="biegu")
# avg_run_speed_calculator(vechicle_name="roweru")
# avg_run_speed_calculator(vechicle_name="samochodu")

# def best_grades(grades, best_grades_number=1):
#     grades.sort(reverse=True)
#     if best_grades_number < len(grades):
#         return grades[:best_grades_number]
#     print("Nie można zwrócić więcej niż jest na liście. Zostaną zwrócone wszystkie... ")
#     return grades
#
# math_grades = [1, 3, 4, 1, 2, 5, 4]
# print(best_grades(math_grades))
# print(best_grades(math_grades, 4))
# print(best_grades(math_grades, best_grades_number=4))

# def write_final_grade(subject_grades, final_grades=None):
#     if final_grades is None:
#         final_grades = []
#     grades_avg = sum(subject_grades) / len(subject_grades)
#     final_grades.append(int(grades_avg))
#     return final_grades
#
# john_math_grades = [3, 4, 5, 2, 5]
# john_physics_grades = [4, 4, 4, 4, 4]
# john_final_grades = write_final_grade(subject_grades=john_math_grades)
# john_final_grades = write_final_grade(subject_grades=john_physics_grades, final_grades=john_final_grades)
# print(f"Oceny John'a: {john_final_grades}")
#
# bob_math_grades = [5, 5, 5]
# bob_physics_grades = [3, 3, 3, 4, 4]
# bob_final_grades = write_final_grade(subject_grades=bob_math_grades)
# bob_final_grades = write_final_grade(subject_grades=bob_physics_grades, final_grades=bob_final_grades)
# print(f"Oceny Bob'a: {bob_final_grades}")
# print(f"Oceny John'a: {john_final_grades}")

# def add_person(names_str, participants=None):
#     if participants is None:
#         participants = []
#     names = names_str.split(',')
#     for name in names:
#         participants.append(name)
#     return participants
#
# attendees_names = "Ola, Bob, Ala, Kuba"
# course_participants = add_person(attendees_names)
# print(course_participants)

# def value_with_tolerance(value, tolerance_percentage = 10):
#     tolerance_value = tolerance_percentage * value / 100
#     return value - tolerance_value, value + tolerance_value
#
# print(value_with_tolerance(value = 90))
# print(value_with_tolerance(value = 90, tolerance_percentage=40))

# def no_return():
#     print("Coś robię, nic nie zwracam")
# value = no_return()

# number = 1
# while number % 2 !=0:
#     number = int(input("Podaj liczbę parzystą "))
#
# print("Brawo!")

# wydatki = [120, 300, 3000, 50, 40, 1200]

# for wydatek in wydatki:
#     print(wydatek)
#     if wydatek > 1000:
#         print("Drogi wydatek został znaleziony!")
#         continue

import funkcje