f = open('pars.txt')
d = str(f)
#f = 'fhf56547ghrt5::6'
numbers = "1234567890:"
count = 0
for i in d:
  if numbers in i:
    i.replace(numbers, '')
    count += 1
    
print(count)



 