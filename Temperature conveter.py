temp = float(input("Enter Temperature:"))
unit = input("From('C'elcius or 'F'ahreheit:)")
if unit.upper() == 'C':print(f"{temp * 9/5 + 32}F")
elif unit.upper() == 'F': print(f"{(temp-32) * 5/9} C")