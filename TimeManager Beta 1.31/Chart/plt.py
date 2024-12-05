import matplotlib.pyplot as plt

while(True):

    # Δεδομένα από τον Χρήστη
    try:
        quantity = int(input("Give me the quantity amount: "))
        if quantity<=0:
            raise ValueError("Quantity must be positive!")
        x1 = int(input("Give the 1st portion amount(x1): "))
        if(x1 > quantity or x1 < 0):
            raise ValueError("Input exceeded initial amount or negative amount!")
        x2 = int(input("Give the 2nd portion amount(x2): "))
        if(x2 > (quantity-x1) or x2 < 0):
            raise ValueError("Input and previous input exceeded total amount or negative amount!")
        x3 = quantity - x1 - x2
        break
    except ValueError as e:
        print(f"Error: {e}")
        continue


# Υπολογίζουμε τα ποσοστά
total = quantity
percentage1 = (x1 / total)*100
percentage2 = (x2 / total)*100
percentage3 = (x3 / total)*100

# Δεδομένα για την πίτα
data = [percentage1,percentage2,percentage3]
labels = ["x1","x2","x3"]

plt.figure(figsize=(8,8))
plt.pie(data,labels=labels,autopct='%1.1f%%',startangle=140)

# Τίτλος
plt.title('Percentage Breakdown (x1,x2,x3)')

# Show the plot
plt.show()