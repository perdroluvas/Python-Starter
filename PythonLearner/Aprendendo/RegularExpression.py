import re

print(re.match('www', 'www.huawei.com').span()) #match from start of the text
print(re.match('com', 'www.huawei.com')) #cannot match from middle of the text
print(re.search('com','www.huawei.com').span())


line = "Cats are smarter than Fish"
searchObj = re.search( r'(.*) are smarter than (.*)', line)
if searchObj:
    print("searchObj.group(): ", searchObj.group())
    print("searchObj.group(1): ", searchObj.group(1))
    print("searchObj.group(2): ", searchObj.group(2))
else:
    print("Nothing found!!!!")

print(" ")
#re.compile(pattern).search(text) é equivalente a re.search(pattern,text)

pattern = re.compile(r'\d+')
n = pattern.match('one12twothree34four')
print(n)

#search from start, found 12
m = pattern.search('one12twothree34four')
print(m)
print(m.group())

phone = "2020-0101-000 # this is a phone number"
#remove the sign # and everything behind it
num = re.sub(r'#.*', "", phone)
print("phone number : ", num)
#remove tudo que não é dígito
num = re.sub(r'\D', "", phone)
print("phone number : ", num)

#ache todos os numeros no texto

text = "Tomorrow is 2022/2/31, today is 2022/2/30"
num1 = re.findall(r'\d+', text)
num2 = re.findall(r'[0-9]{2,5}', text)
print(num1)
print(num2)

#ache o alfabeto
s = re.findall(r'[a-zA-z]+', text)
print(s)

#ache todos os simbolos
s = re.findall(r'\W+', text)
print(s)

s = re.findall(r'[A-Za-z0-9]', text)
print(s)

text = "my email adress is: abc456@def.com"
s = re.findall(r'[A-Za-z0-9]+@[A-Za-z0-9]+\.com', text)
print(s)
text = "python home page: https://www.python.org"
s = re.findall(r'https?://.*', text)
print(s)
