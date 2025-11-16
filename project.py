import pyfiglet
n = 2
object = [ 1 , 1 , 2 , 2 , 2 , 3 , 4 , 4 , 4 , 4 , 5 , 5 , 5 , 5 , 6 , 6 , 7 , 7 , 7 , 7 , 7 , 7]
list_for_elements = []
dictionary = {}
for i in range(len(object)):
    if object[i] in list_for_elements:
        continue
    count = 0 
    for j in range(len(object)):
        if object[i] == object[j]:
            count += 1
    list_for_elements.append(object[i])
    dictionary[object[i]] = count
for key , value in  dictionary.items():
    print(f" element {key} found {value} times")
print(pyfiglet.figlet_format("*" * 10))
sorted_dictionary = (sorted(dictionary.items() , key = lambda x : x[1], reverse= True))
most_reppeated = sorted_dictionary[:n]
for key , value in most_reppeated:
    print(f"{key} : {value}")


# This is much more better idea to perform the same task faster and easier by using the library colloctions
# must studty it 

'''
from collections import counter
import pyfiglet
n = 2
numbers = [1,1,2,2,2,3,4,4,4,4,5,5,5,5,6,6,7,7,7,7,7,7]

counts = Counter(numbers)   
for key, value in counts.items():
    print(f"element {key} found {value} times")

print(pyfiglet.figlet_format("*" * 10))


most_repeated = counts.most_common(n)

for key, value in most_repeated:
    print(f"{key} : {value}")
'''

    
    
