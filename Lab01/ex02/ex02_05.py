workhours = float(input("Enter work hours: "))
hourly_rate = float(input("Enter hourly rate: "))
standard_hours = 44
overstandard_hours = max(0, workhours - standard_hours)
salary = standard_hours * hourly_rate + overstandard_hours * hourly_rate * 1.5
print("Salary: " + str(salary)) 