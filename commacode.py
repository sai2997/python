print("Name:A sai ganesh")
print("USN: 1AY24AI001")
print("Section: M")
items = ['apples', 'bananas', 'tofu', 'cats']
result = ''

for i in range(len(items)):
    if i == len(items) - 1 and len(items) > 1:
        result += 'and ' + items[i]
    elif i == len(items) - 1:
        result += items[i]
    else:
        result += items[i] + ', '

print(result)
