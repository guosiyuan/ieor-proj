f = open('toAmpl', 'r+')
#f.write('0123456789abcdef')

#variable 1: 1st month # of productions, p1m1pA = plant1's month 1's production of component A, p1m1pCom1 = plant1's month1's produtction of computer 1
#len = 15
variablesComponent1 = ['p1m1pA', 'p1m1pB', 'p1m1pC', 'p1m1pD', 'p1m1pE', 'p2m1pA', 'p2m1pB', 'p2m1pC', 'p2m1pD', 'p2m1pE',  'p3m1pA', 'p3m1pB', 'p3m1pC', 'p3m1pD', 'p3m1pE']
#len = 12
variablesComputer1 = ['p1m1pCom1', 'p1m1pCom2', 'p1m1pCom3', 'p1m1pCom4','p2m1pCom1', 'p2m1pCom2', 'p2m1pCom3', 'p2m1pCom4',, 'p3m1pCom1', 'p3m1pCom2', 'p3m1pCom3', 'p3m1pCom4']
#variable 2: 2st month # of productions, p1m2pA = plant1's month 2's production of component A, p1m2pCom1 = plant1's month2's produtction of computer 1
variablesComponent2 = ['p1m2pA', 'p1m2pB', 'p1m2pC', 'p1m2pD', 'p1m2pE', 'p2m2pA', 'p2m2pB', 'p2m2pC', 'p2m2pD', 'p2m2pE', 'p3m2pA', 'p3m2pB', 'p3m2pC', 'p3m2pD', 'p3m2pE']
variablesComputer2 = ['p1m2pCom1', 'p1m2pCom2', 'p1m2pCom3', 'p1m2pCom4','p2m2pCom1', 'p2m2pCom2', 'p2m2pCom3', 'p2m2pCom4', 'p3m2pCom1', 'p3m2pCom2', 'p3m2pCom3', 'p3m2pCom4']
#variable 3: 1st month # of things to sell, p1m1sA = plant1's month 1's sell of component A, p1m1sCom1 = plant1's month1's sell of computer 1
variablesComponent3 = ['p1m1sA', 'p1m1sB', 'p1m1sC', 'p1m1sD', 'p1m1sE', 'p2m1sA', 'p2m1sB', 'p2m1sC', 'p2m1sD', 'p2m1sE', 'p3m1sA', 'p3m1sB', 'p3m1sC', 'p3m1sD', 'p3m1sE']
variablesComputer3 = ['p1m1sCom1', 'p1m1sCom2', 'p1m1sCom3', 'p1m1sCom4','p2m1sCom1', 'p2m1sCom2', 'p2m1sCom3', 'p2m1sCom4','p3m1sCom1', 'p3m1sCom2', 'p3m1sCom3', 'p3m1sCom4']

#1. print variables
f.write('# variables')
#print variable 1
for i in range (15):
	f.write('var ' + variablesComponent1[i]+ ';\r')
for i in range (12):
	f.write('var ' + variablesComputer1[i]+ ';\r')
#print variable 2
for i in range (15):
	f.write('var ' + variablesComponent2[i]+ ';\r')
for i in range (12):
	f.write('var ' + variablesComputer2[i]+ ';\r')

#print variable 3
for i in range (15):
	f.write('var ' + variablesComponent3[i]+ ';\r')
for i in range (12):
	f.write('var ' + variablesComputer3[i]+ ';\r')


#2. objective function

#cost table of month 1, index 1 is the cost of producing plant1 of component 1, index 9 is plant2 production 1
costTableComponentsM1 = [6, 19, 4 ,11, 26,  5, 18, 5, 12, 24,  7, 20, 5, 12, 27]
costTableComputerM1 = [178, 228, 350, 420,175, 220, 360, 435, 180, 240, 370, 450]
#cost table of month 2:
costTableComponentsM2 = [6, 19, 4 ,11, 26,  5, 18, 5, 12, 24,  7, 20, 5, 12, 27]
costTableComputerM2 = [178, 228, 350, 420,175, 220, 360, 435, 180, 240, 370, 450]
for i in range(15):
	costTableComponentsM2[i] = costTableComponentsM2[i]*1.12
fos i in range(12):
	costTableComputerM2[i] = costTableComputerM2[i]*1.12
#print(costTableM2)
#profit table, index 9 is plant2's profic on selling component A
profitTableM1 = [10, 25, 9, 17, 35, 290, 380, 560, 650, 10, 25, 8, 17, 30, 360, 380, 560, 650, 12, 30, 14, 22, 35, 310, 420, 640, 720]

#writing constraints
myString = 'maximize totalProfit: '
for i in range(27):
#month1's number to sell * protfittable
	myString+= variables3[i]+ '*' + str(profitTableM1[i]) + '+'

#month2' number to sell * profittable
for i in range(27):
	myString += '(' + variables1[i]+ '-' + variables3[i] + '+'+ variables2[i] +')' + '*'+ str(profitTableM1[i])
	if i != 26:
		myString+= '+'
#month1's production cost
myString+= '-'
for i in range(27):
	myString+= variables1 + '*' + costTableM1[i] + '-'

#month2's production cost
for i in range(27):
	myString+= variables1 + '*' + costTableM1[i] + '-'

f.write(myString)







