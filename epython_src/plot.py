import csv
import numpy as np
import matplotlib as plt

def countRows():
    with open('file_to_plot.csv', 'r') as f:
    	numberOfRows = len(list(f))
	return numberOfRows


def plot():
	noOfRows = countRows()
	csv_file = open("file_to_plot.csv","r+")
	csv_file = csv.reader(csv_file, delimiter=',')
	line_count = 0
	i = 0

	# To store the values of x and y
	x = np.zeros(noOfRows)
	y = np.zeros(noOfRows)

	for row in csv_file:
		# We jump over the first row because it's a string!
		#TODO add TypeIdentifier to check if it's a string before assigning the value
		if i >= 1:	
			x[i] = row[0]
			y[i] = row[1]
		i+=1
        
        
	print "First column from CSV", x
	print "Second column from CSV: ", y

plot()

