import sys
import crypt

def main():
	salt = "$y$j9T$5LImmws2fco9AeRmLSB2j0"
	hashed = crypt.crypt(sys.argv[1], salt)
	print(hashed, end='')
	

if __name__ == "__main__":
	main()
