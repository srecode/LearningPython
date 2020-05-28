#this script is to count characters in give string

import pprint
def countChar():
    givenString = "This is some epic shit aaaaa"

    countDict = {}
    for char in givenString:
        countDict.setdefault(char, 0)
        #everytime same letter comes we are adding +1 to it
        countDict[char] = countDict[char] + 1
    
    pprint.pprint(countDict)
    # pprint.pformat(countDict)

countChar()
    