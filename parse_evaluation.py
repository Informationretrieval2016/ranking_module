import csv
import pandas as pd
from os import listdir
from os.path import isfile, join

class Parse_Evaluation:
	def __init__(self):
		self.path = "/Users/wesleyquispel/Downloads/evaluation_data-master"

	def read_csv(self, fname):
		res = []
		res2 = []
		flocation = self.path+'/'+fname
		print "File: "+fname
		with open(flocation, 'rb') as eval_csv:
			csv_reader = csv.reader(eval_csv, delimiter=',', quotechar = '"')
			for row in csv_reader:
				for item in row:
					item = item.split("'")[1:2]
					strippedstring = str(item).strip('[]')
					string = strippedstring.replace("/home/wb/Documents/furniture/", "")
					res.append(string)
		for filename in res:
			if filename == '':
				pass
			else:
				res2.append(filename)

		res2 = list(set(res2))
		return res2

	def load_all_documents(self):
		'''
		@usage: load all furniture files into list
		@return: list of file names
		'''
		#load all file names from file path
		file_names = [f for f in listdir(self.path) if isfile(join(self.path, f))]
		return file_names


pe = Parse_Evaluation()
files = pe.load_all_documents()
for file in files:
	evaluationset = pe.read_csv(file)
	res = pd.DataFrame({file: evaluationset})
	saveloc = pe.path+'/processed_'+file
	res.to_csv(saveloc, spec = ",")