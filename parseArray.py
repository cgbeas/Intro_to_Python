
def parseArray(arr, char):
	my_dict = {}
	count = 0
	for el in arr:
		if(char in el):
			my_dict[el] = 'True'
			count += 1
		else:
			my_dict[el] = 'False'

	return count, my_dict
        

cities = ['Anchorage', 'Boston', 'Chicago', 'Denver',
         'El Paso', 'Fairfax', 'Georgia', 'Irvine']

count_result, dict_resut = parseArray(cities, 's')

print(count_result)
print(dict_resut)
