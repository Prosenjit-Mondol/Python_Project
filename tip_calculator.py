#1. welcome
print("welcome to the tip calculator.")
bil=float(input("What was the total bill? $ "))
tip=int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people=int(input("How many people to split the bill? "))
bil_tip=tip/100
tpa=bil*bil_tip
tb=bil+tpa
bilpp=tb/people
final=round(bilpp,2)
print(f"Each person should pay $ {final}")
