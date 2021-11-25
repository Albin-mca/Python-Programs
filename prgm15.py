#Display the appropriate messages as per the colour of signal at the roaad crossing
print("Enter the signal :")
signal=str(input())
if(signal=="Red" or signal=="RED" or signal=="red"):
    print("Stop")
elif(signal=="Green" or signal=="GREEN" or signal=="green"):
    print("Go")
elif(signal=="Orange" or signal=="ORANGE" or signal=="orange"):
    print("Go Slow")
else:
    print("Invalid input")
