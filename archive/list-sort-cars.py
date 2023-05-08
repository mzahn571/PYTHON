from __future__ import print_function

#Sorting a List with sort() Method
cars = ['bmw', 'audi', 'toyota', 'subaru']
output = []
#cars.sort()
#print(cars)
for car in cars:
	if cars[0] == 'bmw':
		print('BMW Down')
	else :
		print('BMW UP')

'''lst = [['a','b','c'], [1,2,3], ['x','y','z']]
outputlist = []
for values in lst:
    outputlist.append(values[0])

print(outputlist) 

for item in my_list:
   if not my_condition(item):
      break    # one item didn't complete the condition, get out of this loop
else:
   # here we are if all items respect the condition
   do_the_stuff(my_list)'''