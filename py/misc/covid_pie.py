#pip install matplotlib
import matplotlib.pyplot as plt


def draw_pie_chart(values, lables, title):
    plt.pie(values, labels = lables)
    #plt.legend(title = title)
    plt.show() 

country = ["Americas", 
            "Europe", 
            "South East Asia", 
            "Eastern Mediterranean"]

cases = [67472965, 
        54288252, 
        31923614, 
        10134399]

lables = []
i = 0
while i < len(country):
    lables.append("{0} ({1})".format(country[i], cases[i]))
    i = i+1

draw_pie_chart(cases, lables, "Countries")

#TODO 
# Show percentage instead of absolute numbers in the lable
# Add more entried incling India from the WHO website
#  ref : https://covid19.who.int/table
#

