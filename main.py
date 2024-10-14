# Katelyn Curtiss
# October 11 2024
# Carpet Calculater Project


# Input
length = int(input("Enter the length of the room: " ))
width = int(input("Enyter the width of the room in feet: "))
price = float(input("Enter the price per square yard of carpet"))
SALES_TAX_RATE = 0.06

square_yards = (length * width) / 9
# print(f"You need" + str(square_yards) + " square yards of carpet.")
print(f"You need {square_yards:.2f} square yards of carpet.")

subtotal = square_yards * price
#print(f"Your subtotal is" + str(subtotal)+ ".")
print(f"Your subtotal is ${subtotal:.2f}.")

# sales_tax = salestax_rate
sales_tax = SALES_TAX_RATE * subtotal

grandtotal = subtotal + sales_tax
# print(f"The sales tax is" + str(sales_tax) + ".")
# print(f"Your grand total is" + str(grandtotal) + ".")

print(f"The sales tax is ${sales_tax:.2f}.")
print(f"Your grand total is ${grandtotal:.2f}.")