import requests
import hashlib

mode = input("[E]/[D]\n")

if mode == "E":
  inp = input("What do you want to hash:  \n")

  input = b""
  for i in inp:
    input += bytes(i.encode("utf-8"))

  md5hasher = hashlib.md5(input)
  print(md5hasher.hexdigest())

elif mode == "D":
  url = "https://md5.gromweb.com/?md5="
  hash = input("Insert hash:\n\n")

  url += hash

  r = requests.get(url)

  string = 6680
  string2 = r.text.find("<p>Feel free to provide some other MD5 hashes you would like to try to reverse.</p>")

  s = ""

  for i in range(string, string2):
    s += r.text[i]

  s=s.replace("</em></p>","")
  print(f"\nThe result is: \n\n{s}")


else:
  print("[!] Invalid Mode")
  exit()
