#Indra Ratna
#CS-UY 1114
#13 Sept 2018
#Homework 1

quarters = int(input("Enter the number of quarters"))
dimes = int(input("Enter the number of dimes"))
nickels = int(input("Enter the number of nickels"))
pennies = int (input("Enter the number of pennies"))
quarters = quarters*25
dimes = dimes*10
nickels = nickels*5
totalValue = quarters+dimes+nickels+pennies
dollarValue = int(totalValue/100)
centValue = totalValue%100
print("The total is "+str(dollarValue)+" dollars and "+str(centValue)+" cents")

