# python code to generate acronym
userinput = input('enter your sentence: ')
splitedtext = userinput.split(' ')
acronym = ""
for i in splitedtext:
    acronym += i[0].upper()

print(acronym)

# python code to get image name from url
url = 'https://prashantmalla.com.np/me.jpg'
# url = input('enter a url which have have image: ')
imagename = url.split('/')[-1]
print(imagename)

# python code to extract text befor last slash usin rsplit 
path = url.rsplit('/', 1)[0]
output = ''
for i in path:
    output += i
print(output)