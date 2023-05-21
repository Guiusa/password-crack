import argparse
import crypt
#import os
import itertools

def yescrypt(passwd, salt):
	if(salt == ""):
		print("Salt not given")
		return 0
	hash = crypt.crypt(passwd, salt)
	return hash

def bruteForce(passwd, salt):
	chars = [chr(i) for i in range(32, 126)]
	size = 1

	while(True):
		strings = [''.join(comb) for comb in itertools.product(chars, 
		repeat=size)]
		for password in strings:
				if(yescrypt(password, salt) == passwd):
					print("A senha é: "+password)
					return 1
		size+=1
		if (size == 3):
			print("nao achei")
			return 0
def main():
	parser = argparse.ArgumentParser(description="breaks an /etc/shadow entry")
	parser.add_argument('-entry', "--entry", dest="entry", default="",
	help="File containing an /etc/shadow entry to be broken")

	
	args = parser.parse_args()
	fileN = args.entry
	if(fileN==""):
		print("Entry file not given")
		return 1
	with open(fileN) as f:
		entry = f.read()

	#gets the salt in the entry#################################################
	entryArr = entry.split("$")
	salt = "$"+entryArr[1]+"$"+entryArr[2]+"$"+entryArr[3]
	print(entry+"\n"+salt+"\n")
	bruteForce(entry, salt)

	return 0
	

if __name__ == "__main__":
	main()
