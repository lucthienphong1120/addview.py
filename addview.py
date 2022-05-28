import requests

def addview(usr, num):

	url = 'https://visitcount.itsvg.in/api?id=' + usr

	for i in range(1, int(num) + 1): 
		req = requests.get(url)
		print("[+] Done " + str(i) + " requests!")

def usage():
	print("Increase github profile views via multi HTTP requests")
	print("Use: ![](https://visitcount.itsvg.in/api?id=yourusername) on README.md")
	print()

if __name__ == "__main__":
	usage()

	usr = input("Your Github username: ")

	if requests.get('https://github.com/' + usr).status_code == 404:
		print("Username not found!")
		exit()

	num = input("Number of views to increase (default=10): ")

	if num == '':
		num = 10

	addview(usr, num)
