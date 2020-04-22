def openOrSenior(data):
    a = []
    for i in data:       
        if i[0] > 54 and i[1] > 7:
            a.append("Senior")
        else:
            a.append("Open")
    return a

print((openOrSenior([[45, 12],[55,21],[19, -2],[104, 20]])))

#['Open', 'Senior', 'Open', 'Senior']
