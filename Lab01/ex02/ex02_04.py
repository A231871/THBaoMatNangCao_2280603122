j=[]
for i in range(2000,3201):
    if i%7==0 and i%5!=0:
        j.append(str(i))
print(','.join(j))
# The code above generates a list of numbers between 2000 and 3000 that are divisible by 7 but not by 5, and then prints them as a comma-separated string.