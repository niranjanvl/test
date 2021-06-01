#pip install matplotlib
import matplotlib.pyplot as plt

quantity = [35, 25, 25, 15]
fruits = ["Apples", "Bananas", "Cherries", "Dates"]
lables = []
i = 0
while i < len(fruits):
    lables.append("{0} ({1})".format(fruits[i], quantity[i]))
    i = i+1

plt.pie(quantity, labels = lables)
plt.legend(title = "Four Fruits:")
plt.show() 
