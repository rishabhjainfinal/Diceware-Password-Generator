import random
import json

def main(sample_space = [1,2,3,4,5,6]):
	def rand_digit(List=sample_space):
		"""funtion for geting sudo random numbers"""
		# there are 2 method of doing this 
		# 1. 
		# random.randint(1,6)

		# 2.
		return random.choice(List)

	def digit_generator():
		# create a empty list
		digit = []
		# running a for loop to generate a random number
		for _ in range(5):
			digit.append(str(rand_digit()))

		# joining all number element of list
		digit= ''.join(digit)

		return int(digit)

	def get_password( words_in_pass=5 ):
		password = [] 
		# TOTAL WORD COUNT IN PASSWORD
		# print(words_in_pass)

		# LOAD FILE TO LOAD PASSWORD values
		with open('diceware.json','r') as file:
			diceware = json.load(file)
			file.close()

		# CREATE A LOOP TO GET password of length UPTO WORD COUNT PASSWORD
		for i in range(words_in_pass):
			num= digit_generator()
			# print(num)
			# print(diceware[f'{num}'])
			password.append(diceware[f'{num}'])

		# return as a string
		return ' '.join(password)

	# return the the password  
	return get_password()

# this is the nmber of tries take to bruteforce all possiblle password 
# print(2**64)


# for i in range(10):
	# print(main())

if __name__ == '__main__':
	a=main()
	print("Your new and secure password is :",a)
