
inputStr = list("hkypdukidpdufbnkaopektpkktpdswtrgtsktpacfiwdt")
frequencyTable = {}

for i in range(0, len(inputStr)):
    if inputStr[i] in frequencyTable:
        newVal = frequencyTable.get(inputStr[i]) + 1
        frequencyTable.update({inputStr[i] : newVal})
    else: #add new key value if char has not been seen yet.
        frequencyTable.update({inputStr[i] : 1})

#prints frequency table in value sorted order.
for key, val in sorted(frequencyTable.items(), key=lambda item: item[1]):
    print("%s: %s" % (key, val))