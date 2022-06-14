# control logic

from urllib.request import urlopen
def get_condition(city):
    url = "http://wttr.in/" + city + "?format=%C"
    page = urlopen(url)
    raw = page.read()
    condition = raw.decode("utf-8")
    return condition

city = input('City: ')
condition = get_condition(city)
if condition == "clear":
    print('no umbrella needed')
else: 
    print("bring umbrella")
# if condition:
# if condition: else
# if condition: elif condition: elif condition: else

# while condition:
#     # coe
#     # increment
