# Code from schalto/ it can recognize whether we are in a leap year or not
def kontrolle_schaltjahr(jahr):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 ==0)

Loop = True
# Code is not part of the function, hence this position - just like "def"
while Loop: # If Loop has the status false, the loop will not continue.
 year = int(input("Enter a year: "))
 if kontrolle_schaltjahr(year):
     print(f"{year} is a leap year!")
 else:
     print(f"{year} This is not a leap year.")

