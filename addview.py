import requests

print("Add viewcount for github profile via multi HTTP requests")

print("Use: ![](https://visitcount.itsvg.in/api?id=yourusername) on README.md")

print()

usr = input("Your Github username: ")

# default for me
if usr == '':
	usr = 'lucthienphong1120'

num = input("Number of views to add: ")

# default is 10 requests
if num == '':
	num = 10

print()

url = 'https://visitcount.itsvg.in/api?id=' + usr

for i in range(1, int(num) + 1): 
	req = requests.get(url)
	print("[+] Done " + str(i) + " requests!")
