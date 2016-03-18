import numpy as np

def calculate_vector_space(queryVector, docVector):
	return (np.dot(queryVector,docVector)/(np.linalg.norm(docVector)*np.linalg.norm(queryVector)))

def calculate_vector_space_ranking(queryVector, docTable):
	vector_space_ranking = {}
	for docs in docTable:
		docVector = docTable[docs]
		vector_space_ranking[docs] = calculate_vector_space(queryVector,docVector)
	# vector_space_ranking.sort(reverse=True)
	print vector_space_ranking

queryVector=[1,1,1,1]
doc_table=np.matrix([[1,1,1,1],[0,0,1,0],[0,0,1,0]])
calculate_vector_space_ranking(queryVector, doc_table)