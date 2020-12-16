def isYearLeap(año):
    if año>=1582:
        if año%4 != 0:
            return (0)
        elif año%100 != 0:
            return (1)
        elif año%400 != 0:
            return (0)
        else:
            return (1)

testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = isYearLeap(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Error")