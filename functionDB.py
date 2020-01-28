#!/usr/bin/python3

import mysql.connector
from collections import Counter


mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="Oralepues123",
	database="student"
)


def main():

	# excercise 1
	myQ = mydb.cursor()
	myQ.execute("SELECT * FROM employee")
	resultQ = myQ.fetchall()
	for x in resultQ:
		print("| %-10s| %-25s| %s\n" % (x[0],x[1],x[2]))
	




	# excercice 2
	input=['may','student','students','dog','studentssess','god','cat','act','tab','bat','flow','wolf','lambs','amy','yam','balms','looped','poodle'] 
    	dict={}

	for word in input:
		wordDic = Counter(word)
		print(wordDic)
		
		key = wordDic.keys()
		print(key)

		key = sorted(key)
		print(key)
		
		key = ''.join(key)
		print key

		if key in dict.keys():
			dict[key].append(word)
		else:
			dict[key]=[]
			dict[key].append(word)

	for (key ,value) in dict.iteritems():
		print(dict[key]) 
		print','.join(dict[key])





if __name__ == '__main__':
	main()
