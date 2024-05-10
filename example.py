import re

# . any char
# \w word char
# \d digit
# \s whitespace
# + 1 or more
# * 0 or more

string = "called piiig"
pat = re.compile("iiig")
result = pat.search(string)
print(result)
print(result.group())

pat = re.compile("..g")
result = pat.search(string)
print(result.group())

string = "called piiig much better: xyzg"
pat = re.compile("..g")
result = pat.findall(string)
print(result)

string = "called piiig ..l"
pat = re.compile("\.l")
result = pat.search(string)
print(result.group())

string = "blah blah :lths123 blah blah"
pat = re.compile(":\w\w\w\w")
result = pat.search(string)
print(result.group())

pat = re.compile(":\w+")
result = pat.search(string)
print(result.group())

string = "1 2 3"
pat = re.compile("\d\s\d\s\d")
result = pat.search(string)
print(result.group())

string = "1    2    3"
pat = re.compile("\d\s+\d\s+\d")
result = pat.search(string)
print(result.group())

# Extract an email address
string = "blah blah alopez339@cps.edu blah blah"
pat = re.compile("[\w.]+@[\w.]+")
result = pat.search(string)
print(result.group())

# groups
pat = re.compile("([\w.]+)(@[\w.]+)")
result = pat.search(string)
print(result.group(1))
print(result.group(2))

string = "blah blah alopez339@cps.edu blah blah foo@bar.com"
pat = re.compile("[\w.]+@[\w.]+")
result = pat.findall(string)
print(result)

string = "Number: 1234123412341234 Name: Alan Lopez CVV: 123"
pat = re.compile("Number: (?P<number>\d{15,16}) Name: (?P<name>\w+ \w+) CVV: (?P<cvv>\d{3})")
result = pat.search(string)
print(result.group("number"))
print(result.group("name"))
print(result.group("cvv"))