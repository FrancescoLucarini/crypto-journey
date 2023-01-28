from pycipher import Caesar
import sys

print("python3 caesar_fuzz.py string key")
#This actually bruteforce until a certain key the string
#quite useless imho the caesar implementation is maybe used in ctf baby challs 

stringa = sys.argv[1]
k = int(sys.argv[2])

for i in range(1, k+1):
	print(f"######{i}#####")
	dec = Caesar(key=i).decipher(stringa)
	print(dec)
	print("\n\n")
