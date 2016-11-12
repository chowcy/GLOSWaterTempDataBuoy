'''
Program written by:
Cathy Chow (chowcy@umich.edu)
Vanessa Rychlinski (vanrych@umich.edu)
Nov 12 2016

Input a date and this program prints and can save min/max/mean Water Temperature at Surface data 
for the following buoys:
crib
leash
leavon
leelyria
lementor
lemrbhd
leoc
leorgn
The station/buoy name must be in the first column, the date in the second, and the temperature in the fourth.
Original data found through GLOS portal, combined and cleaned up by other members of the GLOS Data Dive 2016 team.

'''
import csv

#change file name of data here if using a different data file
file_name ="alldata.csv"
print 'This program gets Water Temperature at Surface data (min/max/avg) for buoys with an option to save to a csv'

#opening csv file
with open(file_name,"rU") as csvfile:
	reader = csv.reader(csvfile)
	reader = list(reader)
	
	date = str(raw_input("Please enter a date for the data you want to retrieve. Format: MM/DD/YYYY  "))

	buoy_names = []

	#store buoy names
	for row in reader:
		#omit first row, which is the header
		if row[0] not in buoy_names and row != reader[0]:
			buoy_names.append(row[0])

	for buoy in buoy_names:
		#create list of temps for this date
		temps = []
		for row in reader:
			#row[0] is the buoy name column
			if row[0] == buoy:
				#row[1] is the date column
				if date in row[1]:
					#row[3] is the Water Temperature at Surface column
					temps.append(float(row[3]))
		#if there is no data for this buoy at this date			
		if temps == []:
			print 'Sorry, ' + buoy + ' does not have data for this date'
		else:
			print '================DATA AT ' + buoy + ' ======================'
			print "Lowest temperature for " + date + ' is ' + str(min(temps)) + " degrees Celsius"
			print "Highest temperature for " + date + ' is ' + str(max(temps)) + " degrees Celsius"
			print "Average temperature for " + date + ' is ' + str(float(sum(temps)/len(temps))) + " degrees Celsius"
			print

	response = raw_input('Would you like to save this information into a csv? Type "Y" to save, anything else to quit:')
	if response == 'Y':
		results_file = raw_input("What should the name of the file be? (No file extension, only valid file names)")
		
		#open file and write the header row
		target = open(results_file + '.csv', 'w')
		target.write('Buoy,Date,MinTemp,MaxTemp,AvgTemp')
		target.write('\n')

		#fill in the rest of the data
		for buoy in buoy_names:
			temps = []
			#write first and second column
			target.write(buoy + ',' + date + ',')

			for row in reader:
				#row[0] is the buoy name column
				if row[0] == buoy:
					#row[1] is the date column
					if date in row[1]:
						#row[3] is the Water Temperature at Surface column
						temps.append(float(row[3]))
			#if there is no data for this buoy at this date			
			if temps == []:
				target.write(',,')
				target.write('\n')

			else:
				avg = str(float(sum(temps)/len(temps)))
				target.write(str(min(temps)) + ',' + str(max(temps)) + ',' + avg )
				target.write('\n')

		target.close()
		print 'The data have been written into file ' + results_file + '.csv'
