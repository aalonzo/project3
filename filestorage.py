import io
import csv
import os.path

GLOBAL_PATH = os.getcwd()

class Classbook:
	def __init__(self, id):
		if not os.path.exists(GLOBAL_PATH + "/gradebooks/" + id + "/weights.csv"):
			file = open(self.fp = GLOBAL_PATH + "/gradebooks/" + id + "/weights.csv", "w+")
			file.close()
		if not os.path.exists(GLOBAL_PATH + "/gradebooks/" + id + "/grades.csv"):
			file = open(self.fp = GLOBAL_PATH + "/gradebooks/" + id + "/grades.csv", "w+")
			file.close()
			
		self.fp = GLOBAL_PATH + "/gradebooks/" + id 
		self.grades = read("grades")
		self.weights = read("weights")

	def writeweight(self, name,weight):
		file = open(self.fp + "/weights.csv", "a")
		writer = csv.writer(file)
		writer.writerow([name,weight])
		
	def writegrade(self, name,category,grade):
		file = open(self.fp + "/grades.csv", "a")
		writer = csv.writer(file)
		writer.writerow([name,category,grade])

	def read(self, fileoption):
		file = open(self.fp, + "/" + fileoption + ".csv")
		reader = csv.reader(file)
		output = []
		for row in reader:
			output.append(row)
		return output
		
	def calculate_grade(self):
		self.grades = read("grades")
		self.weights = read("weights")
		weightlist = []
		calc_grades = []
		for item in self.weights:
			weightlist.append(item[0])
			calc_grades.append([])
		for item in self.grades:
			calc_grades[self.weightlist.index(item[1])].append(item[2])
		final = 0
		sums = []
		colsum = 0
		for cat in calc_grades:
			for assignment in cat:
				colsum += assignment
			sums.append(colsum)
			colsum = 0
		for x in range(len(sums)):
			final += sums[x] * self.weights[x][1]
		return final

	