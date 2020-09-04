import json
"""This program is to generate a json file from the txt file beacause it is not avialable on the internet"""
# open txt file 
with open('diceware.txt','r') as file:
	# getall lines of file
	lines=file.readlines()
	json_data = {}
	# Make for loop 
	for i in lines:
		# remove all unnecessary things from the lime
		i= i.strip('\n')
		# split in 2 parts 
		# the use of try and except because there is two type of lines 
		# one which have space between them 
		# second type are have tab seperation between them
		try:
			a,b = i.split(' ',1)
		except :
			a,b = i.split('\t')

		# append in dict name json_data
		json_data[int(a)] = b
		# print(b)

	file.close()
	# print(json_data)

	# save all data of dict into new json file 
	with open('diceware.json','w') as f:
		json.dump(json_data,f ,indent=2)
		f.close()

