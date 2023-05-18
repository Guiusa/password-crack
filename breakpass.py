import hashlib
import argparse

def main():
	parser = argparse.ArgumentParser(description="Breaks a md5 hash password by\
	iterating over a dictionary")

	parser.add_argument('-d', "--dictionary", dest="dic", default="dic.txt",
	help="path to the dictionary file")
	
	parser.add_argument('-s', "--size", dest="size", default="0",
	help="size of the password, if not know it'll iterate over every word")	
	
	parser.add_argument('-p', "--password", dest="password", default="pass",
	help="Path of hashed password text file")
	
	args 	= parser.parse_args()
	fileN	= args.dic
	passN	= args.password
	size	= int(args.size)
   
	with open(fileN) as f:
		dic = f.read()
	with open(passN) as p:
		password = p.read()

	if(size==0):
		for word in dic.split('\n'):
			hashed = hashlib.md5(bytes(word, "utf-8"))
			if(hashed.hexdigest() == password):
				print("A senha é: "+word)
				return 0
	else:
		for word in dic.split('\n'):
			if(len(word) == size):
				hashed = hashlib.md5(bytes(word, "utf-8"))
				if(hashed.hexdigest() == password):
					print("A senha é: "+word)
					return 0

	print("Não achei")
	return 1	


if __name__ == "__main__":
	main()
