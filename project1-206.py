# Grace Badagliacca Project 1 
# Testing for commits
import os
import filecmp
from dateutil.relativedelta import *
import csv
from datetime import date
import datetime


def getData(file):

# get a list of dictionary objects from the file
#Input: file name
#Ouput: return a list of dictionary objects where
#the keys are from the first row in the data. and the values are each of the other rows
	inFile = open(file, 'r')
	lines = inFile.readlines()
	inFile.close()
	dictList = []
	for line in lines:
		dataDict = {}
		values = line.split(',')
		First = values[0]
		Last = values[1]
		Email = values[2]
		class_status = values[3]
		DOB = values[4]
		dataDict['First'] = First
		dataDict['Last'] = Last
		dataDict['Email'] = Email
		dataDict['Class'] = class_status
		dataDict['DOB'] = DOB
		dictList.append(dataDict)
	return dictList
	# pass

def mySort(data,col):
	sorted_lst = sorted(data, key = lambda k: k[col])
	first = sorted_lst[0]['First']
	last = sorted_lst[0]['Last']
	return first + ' ' + last
	
	
# Sort based on key/column
#Input: list of dictionaries and col (key) to sort on
#Output: Return the first item in the sorted list as a string of just: firstName lastName

	# pass


def classSizes(data):
	fresh = 0 
	soph = 0 
	jr = 0 
	senior = 0 
	for student in data:
		if student['Class'] == 'Freshman':
			fresh += 1 
		elif student['Class'] == 'Sophomore':
			soph += 1
		elif student['Class'] == 'Junior':
			jr += 1 
		elif student['Class'] == 'Senior':
			senior += 1
	students_class = [('Freshman', fresh), ('Sophomore', soph), ('Junior', jr), ('Senior', senior)]
	return sorted(students_class, key = lambda k: k[-1], reverse = True)
	# sorted_classes = sorted(dictList.items(), key = lambda x: x[1], reverse = True)
# Create a histogram
# Input: list of dictionaries
# Output: Return a list of tuples sorted by the number of students in that class in
# descending order
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

	# pass


def findMonth(a):
	dict_month = {}
	for student in a:
		birth = student['DOB']
		split_birth = birth.split('/')
		month = split_birth[0]
		if month in dict_month:
			dict_month[month] += 1 
		else:
			dict_month[month] = 1 
	sort_month = sorted(dict_month, key = lambda k: dict_month[k], reverse = True)
	return int(sort_month[0])

# Find the most common birth month form this data
# Input: list of dictionaries
# Output: Return the month (1-12) that had the most births in the data

	# pass

def mySortPrint(a,col,fileName):
	new_lst = []
	sort_lst = sorted(a, key = lambda k: k[col])
	for i in sort_lst:
		new_lst.append(i['First'] + ',' + i['Last'] + ',' + i['Email'] + '\n')
	final_file = open(fileName, 'w')
	for x in new_lst:
		final_file.write(x)
#Similar to mySort, but instead of returning single
#Student, the sorted data is saved to a csv file.
# as first,last,email
#Input: list of dictionaries, col (key) to sort by and output file name
#Output: No return value, but the file is written

	# pass

def findAge(a):
	age_lst = []
	yearToday = (datetime.datetime.today().strftime('%m/%d/%Y'))
	for d in a[1:]:
		year = d['DOB']
		dateToday = yearToday.split('/')
		bday = year.split('/')
		age = int(dateToday[2]) - int(bday[2])
		if int(bday[0]) >= int(dateToday[0]):
			age = int(dateToday[2]) - int(bday[2]) - 1
		if int(bday[0]) == int(dateToday[0]) and int(bday[1]) > int(dateToday[1]):
			age = int(dateToday[2]) - int(bday[2]) - 1
		age_lst.append(age)
	total = 0 
	for x in age_lst:
		total += x 
	avg = float(total / len(age_lst))
	return round(avg)

	
	# current = datetime.now()
# def findAge(a):
# Input: list of dictionaries
# Output: Return the average age of the students and round that age to the nearest
# integer.  You will need to work with the DOB and the current date to find the current
# age in years.

	pass


################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ", end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB2.csv')
	total += test(type(data),type([]),50)

	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',25)
	total += test(mySort(data2,'First'),'Adam Rocha',25)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',25)
	total += test(mySort(data2,'Last'),'Elijah Adams',25)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',25)
	total += test(mySort(data2,'Email'),'Orli Humphrey',25)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],25)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],25)

	print("\nThe most common month of the year to be born is:")
	total += test(findMonth(data),3,15)
	total += test(findMonth(data2),3,15)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,20)

	print("\nTest of extra credit: Calcuate average age")
	total += test(findAge(data), 40, 5)
	total += test(findAge(data2), 42, 5)

	print("Your final score is " + str(total))

# Standard boilerplate to call the main() function that tests all your code
if __name__ == '__main__':
    main()
