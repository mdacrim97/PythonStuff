import csv 

csvPath = input("Enter path to csv file:   ")

with open(csvPath, 'r') as f:
	reader = csv.reader(f)
	next(reader)
	
	ofileName = input("Entername of 301 file:   ")
	ofile = open(ofileName, 'w')

	title = input("Enter the 301 title:   ")
	ofile.write(title + "\n")	

	for row in reader:
		redirect = "301 redirect " + row[1][19:] + " " + row[2] + "\n"
		print(redirect)
		
		ofile.write(redirect)
	
	ofile.close()	
