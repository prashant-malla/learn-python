# 1st way: using split
# email = 'hello@prashantmalla.com.np'
# email = input('enter your email: ')
# output = email.split('@')

# print('your username is: ', output[0])
# print('your domainname is: ', output[1])

# 2nd way
email = 'hello@prashantmalla.com.np'.strip()
username = email[:email.index('@')]
domainname = email[email.index('@')+1:]
print(f"your user name is {username}. And your domain name is {domainname}")
