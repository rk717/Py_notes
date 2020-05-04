You work in the best consumer electronics corporation, and your boss wants to find out which three products generate the most revenue. Given 3 lists of the same length like these:

products: ["Computer", "Cell Phones", "Vacuum Cleaner"]
amounts: [3, 24, 8]
prices: [199, 299, 399]
return the three product names with the highest revenue (amount * price).

Test.assert_equals(top3(["Computer", "Cell Phones", "Vacuum Cleaner"], [3,24,8], [199,299,399]), ["Cell Phones", "Vacuum Cleaner", "Computer"])
Test.assert_equals(top3(["Cell Phones", "Vacuum Cleaner", "Computer", "Autos", "Gold", "Fishing Rods", "Lego", " Speakers"], [5, 25, 2, 7, 10, 3, 2, 24], [51, 225, 22, 47, 510, 83, 82, 124]), ['Vacuum Cleaner', 'Gold', ' Speakers'])
Test.assert_equals(top3(["Cell Phones", "Vacuum Cleaner", "Computer", "Autos", "Gold", "Fishing Rods", "Lego", " Speakers"], [0, 12, 24, 17, 19, 23, 120, 8], [9, 24, 29, 31, 51, 8, 120, 14]), ['Lego', 'Gold', 'Computer'])

def top3(products, amounts, prices):
    all1 = []
    obj1 = {}
    final = []
    for i in range (len(amounts)):
        obj1[products[i]] = amounts[i]*prices[i]
        all1.append(amounts[i]*prices[i])
    all1.sort()
    all1.reverse()
    all1 = all1[0:3]
    for x in all1:
        for c in obj1:
            if x == obj1[c]:
                final.append(c)
    return final[0:3]

print(top3(["Computer", "Cell Phones", "Vacuum Cleaner"], [3,24,8], [199,299,399]))

#["Cell Phones", "Vacuum Cleaner", "Computer"]


#############################################################
如何返回一个 字典 列表， how to return a dictionary list
def namelist(names):
    namelist = [name['name'] for name in names]
    return namelist

print(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'}]))
#['Bart', 'Lisa', 'Maggie']
#############################################################
def namelist(names):
    namelist = [name['name'] for name in names]
    if len(namelist) <= 1:
        return "".join(namelist)
    else:
        lastTwo = " & ".join(namelist[-2:])
        first = [n + ',' for n in namelist[:-2]]
        first.append(lastTwo)
        return " ".join(first)

print(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'}]))
# Bart, Lisa & Maggie
