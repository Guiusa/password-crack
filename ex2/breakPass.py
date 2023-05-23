import argparse
import crypt

def yescrypt(passwd, salt):
	hash = crypt.crypt(passwd, salt)
	return hash


def main():
	parser = argparse.ArgumentParser(description="Breaks an yescrypt hashed pass by iterating over a dictionary")

	parser.add_argument('-d', "--dictionary", dest="dic", default="dic.txt",
	help="path to the dictionary file")
	
	parser.add_argument('-p', "--password", dest="password", default="pass",
	help="path of hashed password text file")

	args 	= parser.parse_args()
	fileN 	= args.dic
	passN 	= args.password

	with open(fileN) as f:
		dic = f.read()
	with open(passN) as p:
		password = p.read()
		entryArr = password.split('$')
		salt = "$"+entryArr[1]+"$"+entryArr[2]+"$"+entryArr[3]

	for word in dic.split('\n'):
		if(yescrypt(word, salt) == password):
			print("A senha é: "+word)
			return 0
	return 1

if __name__ == "__main__":
	main()
