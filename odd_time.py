from datetime import datetime

if datetime.today().minute % 2 == 0:
    print ("This is not an odd minute")
else:
    print ("This is an odd minute")

print "\n"
print "Minute right now:", datetime.today().minute