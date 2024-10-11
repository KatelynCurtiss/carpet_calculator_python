# Katelyn Curtiss
# October 11 2024
# Carpet Calculater Project


# Input
length = int(input("Enter the length of the room: " ))
width = int(input("Enyter the width of the room in feet: "))
price = float(input("Enter the price per square yard of carpet"))
salestax_rate = 0.06

square_yards = (length * width) / 9
print(f"You need" + str(square_yards) + " square yards of carpet.")

subtotal = square_yards * price
print(f"Your subtotal is" + str(subtotal)+ ".")

sales_tax = salestax_rate

grandtotal = subtotal