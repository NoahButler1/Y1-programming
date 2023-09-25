HoursPerNight = float(input("how many hours do you sleep per night"))
HoursPerWeek = HoursPerNight * 7

print(" you sleep", HoursPerWeek, "hours per week")

HoursPerMonth = float(HoursPerWeek * 4.35)
print("this is equal to", HoursPerMonth, "hours slept per month")

DaysPerMonth = HoursPerMonth / 24
print("this is equal to", DaysPerMonth, "days slept per month")