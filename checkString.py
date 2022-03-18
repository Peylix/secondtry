def checkStr():
    listo = []
    target_str = str(input("Give me your string: "))
    for i in target_str:
        listo = listo + [i]
    upper = 0
    lower = 0
    digit = 0
    other = 0
    for i in listo:
        if i.isupper == True:
            upper += 1
        elif i.islower == True:
            lower += 1
        elif i.isdigit == True:
            digit += 1
        else:
            other += 1
    print("Upper total: ", upper, "Lower total: ", lower, "Digit total: ", digit, "Others total:", other)
checkStr()


'''
def checkStr_old():
    target_str = str(input("Give me your string: "))
    listo = target_str.split()
    list_upper = []
    list_lower = []
    list_digit = []
    list_other = []
    for i in range(len(listo)):
        if listo[i].isupper == True:
            list_upper.append(listo[i])
        elif listo[i].islower == True:
            list_lower.append(listo[i])
        elif listo[i].isdigit == True:
            list_digit.append(listo[i])
        else:
            list_other.append(listo[i])
        len_upper = len(list_upper)
        len_lower = len(list_lower)
        len_digit = len(list_digit)
        len_other = len(list_other)
    print("Upper total: ", len_upper, "Lower total: ", len_lower, "Digit total: ", len_digit, "Others total:", len_other)
'''