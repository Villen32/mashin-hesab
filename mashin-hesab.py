num1 = int(input("adad aval ra vared konid : "))
num2 = int(input("adad dovom ra vared konid : "))
am = input("amalgar ra vared konid :  (+, -, *, /, **): ")

if am == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif am == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif am == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif am == "/":
    print(f"{num1} / {num2} = {num1 / num2}")
elif am == "**":
    print(f"{num1} ** {num2} = {num1 ** num2}")
else:
    print("amalgari na dorost vared kardi!")
