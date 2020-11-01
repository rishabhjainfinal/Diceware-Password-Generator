from DicewarePasswordGenerator import main as password 
import pyperclip	# pip install pyperclip

def main():
	paslist=password().split(' ')
	lastword = []
	for i in paslist:
		lastword.append(i[0])

	paslist.append(''.join(lastword))
	return " ".join(paslist)


if __name__ == '__main__':
	a=main()
	print("Your new and secure password is :",a)
	print('\n\tYour password is copied to clipboard without spaces\n')
	pyperclip.copy(a.replace(' ',''))
