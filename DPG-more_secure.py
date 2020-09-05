from DicewarePasswordGenerator import main as password 


def main():
	paslist=password().split(' ')
	lastword = []
	for i in paslist:
		lastword.append(i[0])

	paslist.append(''.join(lastword))
	return " ".join(paslist)


if __name__ == '__main__':
	print("Your new and more secure password is :",main())
