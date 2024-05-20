import run_calculator

distance = float(input("Ile km ostatnio przebiegłeś? "))
time = float(input("W jakim czasie? "))

avg_speed = run_calculator.avg_speed(distance, time)

print(f"Twoja średnia prędkość to {avg_speed} km/h")
