f = open('toAmpl', 'r+')
#f.write('0123456789abcdef')

#variable 1: 1st month # of productions, p1m1pA = plant1's month 1's production of component A, p1m1pCom1 = plant1's month1's produtction of computer 1
#len = 15
variablesComponent1 = ['p1m1pA', 'p1m1pB', 'p1m1pC', 'p1m1pD', 'p1m1pE', 'p2m1pA', 'p2m1pB', 'p2m1pC', 'p2m1pD', 'p2m1pE',  'p3m1pA', 'p3m1pB', 'p3m1pC', 'p3m1pD', 'p3m1pE']
#len = 12
variablesComputer1 = ['p1m1pCom1', 'p1m1pCom2', 'p1m1pCom3', 'p1m1pCom4','p2m1pCom1', 'p2m1pCom2', 'p2m1pCom3', 'p2m1pCom4', 'p3m1pCom1', 'p3m1pCom2', 'p3m1pCom3', 'p3m1pCom4']
#variable 2: 2st month # of productions, p1m2pA = plant1's month 2's production of component A, p1m2pCom1 = plant1's month2's produtction of computer 1
variablesComponent2 = ['p1m2pA', 'p1m2pB', 'p1m2pC', 'p1m2pD', 'p1m2pE', 'p2m2pA', 'p2m2pB', 'p2m2pC', 'p2m2pD', 'p2m2pE', 'p3m2pA', 'p3m2pB', 'p3m2pC', 'p3m2pD', 'p3m2pE']
variablesComputer2 = ['p1m2pCom1', 'p1m2pCom2', 'p1m2pCom3', 'p1m2pCom4','p2m2pCom1', 'p2m2pCom2', 'p2m2pCom3', 'p2m2pCom4', 'p3m2pCom1', 'p3m2pCom2', 'p3m2pCom3', 'p3m2pCom4']
#variable 3: 1st month # of things to sell, p1m1sA = plant1's month 1's sell of component A, p1m1sCom1 = plant1's month1's sell of computer 1
variablesComponent3 = ['p1m1sA', 'p1m1sB', 'p1m1sC', 'p1m1sD', 'p1m1sE', 'p2m1sA', 'p2m1sB', 'p2m1sC', 'p2m1sD', 'p2m1sE', 'p3m1sA', 'p3m1sB', 'p3m1sC', 'p3m1sD', 'p3m1sE']
variablesComputer3 = ['p1m1sCom1', 'p1m1sCom2', 'p1m1sCom3', 'p1m1sCom4','p2m1sCom1', 'p2m1sCom2', 'p2m1sCom3', 'p2m1sCom4','p3m1sCom1', 'p3m1sCom2', 'p3m1sCom3', 'p3m1sCom4']
#variable 4: 2st month # of things to sell, p1m2sA = plant1's month 2's sell of component A, p1m2sCom1 = plant1's month2's sell of computer 1
variablesComponent4 = ['p1m2sA', 'p1m2sB', 'p1m2sC', 'p1m2sD', 'p1m2sE', 'p2m2sA', 'p2m2sB', 'p2m2sC', 'p2m2sD', 'p2m2sE', 'p3m2sA', 'p3m2sB', 'p3m2sC', 'p3m2sD', 'p3m2sE']
variablesComputer4 = ['p1m2sCom1', 'p1m2sCom2', 'p1m2sCom3', 'p1m2sCom4','p2m2sCom1', 'p2m2sCom2', 'p2m2sCom3', 'p2m2sCom4','p3m2sCom1', 'p3m2sCom2', 'p3m2sCom3', 'p3m2sCom4']
#variable 5: # of component/computer we reserve from month 1 to month 2
variablesComponent5 = ['p1reA', 'p1reB', 'p1reC', 'p1reD', 'p1reE', 'p2reA', 'p2reB', 'p2reC', 'p2reD', 'p2reE', 'p3reA', 'p3reB', 'p3reC', 'p3reD', 'p3reE']
variablesComputer5 = ['p1reCom1', 'p1reCom2', 'p1reCom3', 'p1reCom4','p2reCom1', 'p2reCom2', 'p2reCom3', 'p2reCom4','p3reCom1', 'p3reCom2', 'p3reCom3', 'p3reCom4']



#1. print variables ************************************************************************************
f.write('# variables\r')
#print variable 1
for i in range (15):
	f.write('var ' + variablesComponent1[i]+ ' >= 0;\r')
for i in range (12):
	f.write('var ' + variablesComputer1[i]+ ' >= 0;\r')
#print variable 2
for i in range (15):
	f.write('var ' + variablesComponent2[i]+ ' >= 0;\r')
for i in range (12):
	f.write('var ' + variablesComputer2[i]+ ' >= 0;\r')

#print variable 3
for i in range (15):
	f.write('var ' + variablesComponent3[i]+ ' >= 0;\r')
for i in range (12):
	f.write('var ' + variablesComputer3[i]+ ' >= 0;\r')
#print variable 4
for i in range (15):
	f.write('var ' + variablesComponent4[i]+ ' >= 0;\r')
for i in range (12):
	f.write('var ' + variablesComputer4[i]+ ' >= 0;\r')
#print variable 5
for i in range (15):
	f.write('var ' + variablesComponent5[i]+ ' >= 0;\r')
for i in range (12):
	f.write('var ' + variablesComputer5[i]+ ' >= 0;\r')

#2. objective function ********************************************************************************************

#cost table of month 1, index 1 is the cost of producing plant1 of component 1, index 9 is plant2 production 1
costTableComponentsM1 = [6, 19, 4 ,11, 26,  5, 18, 5, 12, 24,  7, 20, 5, 12, 27]
costTableComputerM1 = [178, 228, 350, 420,175, 220, 360, 435, 180, 240, 370, 450]
#cost table of month 2:
costTableComponentsM2 = [6, 19, 4 ,11, 26,  5, 18, 5, 12, 24,  7, 20, 5, 12, 27]
costTableComputerM2 = [178, 228, 350, 420,175, 220, 360, 435, 180, 240, 370, 450]
for i in range(15):
	costTableComponentsM2[i] = costTableComponentsM2[i]*1.12
for i in range(12):
	costTableComputerM2[i] = costTableComputerM2[i]*1.12
#print(costTableM2)
#profit table, index 9 is plant2's profic on selling component A
profitTableComponents = [10, 25, 9, 17, 35,  10, 25, 8, 17, 30,  12, 30, 14, 22, 35]
profitTableComputer = [290, 380, 560, 650,360, 380, 560, 650,310, 420, 640, 720]

#writing constraints
myString = 'maximize totalProfit: '
for i in range(15):
#month1's number to sell * protfittable
	myString+= variablesComponent3[i]+ ' * ' + str(profitTableComponents[i]) + ' + '
for i in range(12):
	myString+= variablesComputer3[i]+ ' * ' + str(profitTableComputer[i])+ ' + '

#month2' number to sell * profittable
for i in range(15):
#month1's number to sell * protfittable
	myString+= variablesComponent4[i]+ ' * ' + str(profitTableComponents[i]) + ' + '
for i in range(12):
	myString+= variablesComputer4[i]+ ' * ' + str(profitTableComputer[i])+ ' + '
#remove the last + sign
myString = myString[0: len(myString)-1]

#month1's production cost
myString+= '-'
for i in range(15):
	myString+= variablesComponent1[i] + ' * ' + str(costTableComponentsM1[i]) + ' - '
for i in range(12):
	myString+= variablesComputer1[i] + ' * ' + str(costTableComputerM1[i]) + ' - '

#month2's production cost
for i in range(15):
	myString+= variablesComponent2[i] + ' * ' + str(costTableComponentsM2[i]) + ' - '
for i in range(12):
	myString+= variablesComputer2[i] + ' * ' + str(costTableComputerM2[i]) + ' - '

#storage cost
costTableComponentsReservation = [6, 19, 4 ,11, 26,  5, 18, 5, 12, 24,  7, 20, 5, 12, 27]
costTableComputerReservation = [178, 228, 350, 420,175, 220, 360, 435, 180, 240, 370, 450]
for i in range(15):
	costTableComponentsReservation[i] = costTableComponentsReservation[i]*0.04
for i in range(12):
	costTableComputerReservation[i] = costTableComputerReservation[i]*0.04
#got reservation cost
for i in range(15):
	myString+= variablesComponent5[i] + ' * ' + str(costTableComponentsReservation[i]) + ' - '
for i in range(12):
	myString+= variablesComputer5[i] + ' * ' + str(costTableComputerReservation[i]) + ' - '
myString = myString[0: len(myString)-1]
# f.write(myString)
# f.write('\r')
myString+=';\r'
#3. constraints ********************************************************************************************
myString+='#constraints \r'
#(1) express var5, number of reserve at the end of month 1, using the first 3 variables.
myString+='#number of reservation at the end of month one is equal to number of production minous number of sell and other consumption \r'
#computer's case, easy
for i in range(12):
	myString+= variablesComputer5[i] + ' = ' + variablesComputer1[i] + ' - ' + variablesComputer3[i] + ';\r'
#components' case, more complicated, need to say explicitly
for k in range(3):# just loop over plant 1,2,3
	#i(component), j(computer) will help us target the correct plant
	i = k*5
	j = k*4
	#A's equation, SSD
	myString+= variablesComponent5[i] + ' = ' + variablesComponent1[i]+ ' - ' + variablesComponent3[i] + ' - 2 * ' + variablesComputer1[j+1] + ' - 2 * ' + variablesComputer1[j+3] + ';\r'
	#B's equation
	myString+= variablesComponent5[i+1] + ' = ' + variablesComponent1[i+1]+ ' - ' + variablesComponent3[i+1] + ' - 2 * ' + variablesComputer1[j] + ' - 2 * ' + variablesComputer1[j+2] + ';\r'
	#C's equation, every computer uses a CPU
	myString+= variablesComponent5[i+2] + ' = ' + variablesComponent1[i+2]+ ' - ' + variablesComponent3[i+2] + ' - ' + variablesComputer1[j] + ' - ' + variablesComputer1[j+1] + ' - ' + variablesComputer1[j+2] + ' - ' + variablesComputer1[j+3] + ';\r'
	#D's equation
	myString+= variablesComponent5[i+3] + ' = ' + variablesComponent1[i+3]+ ' - ' + variablesComponent3[i+3] + ' - 2 * ' + variablesComputer1[j] + ' - 2 * ' + variablesComputer1[j+1] + ';\r'
	#E's equation
	myString+= variablesComponent5[i+4] + ' = ' + variablesComponent1[i+4]+ ' - ' + variablesComponent3[i+4] + ' - 2 * ' + variablesComputer1[j+2] + ' - 2 * ' + variablesComputer1[j+3] + ';\r'
	#B's equation


f.write(myString)
f.write('hhhhhh')







