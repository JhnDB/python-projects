rate = input("Enter Rate:")
try:
    frate = float(rate)
except:
    print("Error, enter a valid score")
    quit()

if frate > 1.0 or frate < 0.0:
    print("Error, enter a score between 0.0 and 1.0")
elif frate >= 0.9:
    print("A")
elif frate >= 0.8:
    print("B")
elif frate >= 0.7:
    print("C")
elif frate >= 0.6:
    print("D")
else:
    print("F")