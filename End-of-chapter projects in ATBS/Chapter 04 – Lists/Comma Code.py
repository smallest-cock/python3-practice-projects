def addCommas(list):
    for item in range(len(list) - 1): # creates loop that iterates over the amount of items in the list minus 1 (because the last item should stay unaffected)
        print(str(list[item]) + ', ', end = "") # prints each iterated item in the list followed by a comma and space (and prints all iterations in the same line) 
    print("and " + str(list[-1]) + ".") # prints the last item in the list, preceded by "and " and followed by a period

randlist = ['tofu', 'food', 8, 'octopii', 'German', 16789, 'oreos']
addCommas(randlist)
