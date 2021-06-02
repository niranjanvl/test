"""
Covid Statistics

    ref : https://covid19.who.int/table
"""
def generate_report(cases, country, title):
    lables = []
    total = 0

    for case in cases:
        total += case

    i = 0
    case_pc = []

    while i < len(country):
        pc = cases[i]*100.0 / total
        pc = round(pc, 2)
        case_pc.append(pc)
        lables.append("{0} ({1})".format(country[i], pc))
        i = i+1

    """
    import matplotlib.pyplot as plt
    plt.pie(cases, labels = lables)
    #plt.legend(title = title)
    plt.show() 
    """
    i = 0
    while i < len(country):
        #TODO : Lets make it prettier : Align them
        print("{0} : {1} : {2}".format(country[i], cases[i], case_pc[i]))
        i += 1


country = ["Americas", 
            "Europe", 
            "South East Asia", 
            "Eastern Mediterranean"]

cases = [67472965, 
        54288252, 
        31923614, 
        10134399]


generate_report(cases, country, "Countries")

#TODO 
# Add more entries including India from the WHO website
#  ref : https://covid19.who.int/table
#

