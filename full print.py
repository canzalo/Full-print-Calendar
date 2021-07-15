# Program to display calendar of the given  year and month

# importing calendar module
import calendar

print(" Enter 1 To view the whole year or Enter 2  to view a single month \n")

validate=int(input("Enter a number :"))

#Condition to determine the output 

if (validate==1):
	year=int(input("Enter the Year: "))	
# display the whole year of calendar
	print(calendar.calendar(year))
	
elif(validate==2):
	
	#Inputing the year
	
	year=int(input("Enter year: "))
	
	#Inputing the month
	
	month=int(input("Now! Enter the month: "))

		#printing a single month
		
	print(calendar.month(year,month))
	
else:
	print("Invalid input, Try Again")
