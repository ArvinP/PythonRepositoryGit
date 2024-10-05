import re
def plindrom(str):
    new = str.replace(" ","").replace("-","").replace(",","").replace(".","").replace("'","").lower()
    return new==new[::-1]

res = plindrom("Go hang a salami - I'm a lasagna hog.")
print(res)


def palindrom2(phrase):
    forwards = ''.join(re.findall(r'[a-z]+',phrase.lower()))
    backwards = forwards[::-1]
    return backwards== forwards
res = palindrom2("Go hang a salami - I'm a lasagna hog.")
print(res)

