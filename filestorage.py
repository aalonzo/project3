import io
import csv
import os.path

GLOBAL_PATH = os.getcwd()

class Classbook:
	def __init__(id):
		if not os.path.exists(GLOBAL_PATH + "/gradebooks/" + id + "/weights.csv"):
			file = open(self.fp = GLOBAL_PATH + "/gradebooks/" + id + "/weights.csv", "w+")
			file.close()
		if not os.path.exists(GLOBAL_PATH + "/gradebooks/" + id + "/grades.csv"):
			file = open(self.fp = GLOBAL_PATH + "/gradebooks/" + id + "/grades.csv", "w+")
			file.close()
			
		self.fp = GLOBAL_PATH + "/gradebooks/" + id 


	def writeweight(name,weight):
		file = open(self.fp + "/weights.csv", "a")
		writer = csv.writer(file)
		writer.writerow([name,weight])
		
	def writegrade(name,category,grade):
		file = open(self.fp + "/grades.csv", "a")
		writer = csv.writer(file)
		writer.writerow([name,category,grade])

	def read(fileoption):
		file = open(self.fp, + "/" + fileoption + ".csv")
		reader = csv.reader(file)
		output = []
		for row in reader:
			output.append(row)
		return output
		


	