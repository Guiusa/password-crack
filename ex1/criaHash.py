import hashlib
import sys

def main():
	if len(sys.argv) == 1:
		print("Give me a word")
		return 1
	
	hashed = hashlib.md5(bytes(sys.argv[1], "utf-8"))
	print(hashed.hexdigest())
	return 0
	
if __name__ == "__main__":
	main()
