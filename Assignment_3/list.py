'''Question 1: Given the list fruits = ['apple', 'banana', 'cherry'], 
   how can you add the item 'orange' to the end of the list?'''

fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')
print(fruits)



'''Question 2: If you have the list numbers = [1, 2, 3, 4, 5], what method
would you use to remove the item 3 from the list?'''

numbers = [1, 2, 3, 4, 5]
numbers.remove(3)
print(numbers)



'''Question 3: You have the list colors = ['red', 'green', 'blue']. How can
you insert the item 'yellow' at the second position in the list?'''

colors = ['red', 'green', 'blue']
colors.insert(1, 'yellow')
print(colors)




'''Question 4: If you have the list letters = ['a', 'b', 'c', 'a', 'd'], how many
occurrences of the letter 'a' are there in the list?'''

letters = ['a', 'b', 'c', 'a', 'd']
letter = 'a'
count = letters.count(letter)
print(f"The letter '{letter}' occurs {count} times in the list")




'''Question 5: Given the list data = [10, 20, 30, 40, 50], which method can
you use to remove and return the last item from the list?'''

data = [10, 20, 30, 40, 50]
last_item = data.pop()
print(last_item)
print(data)



'''Question 6: If you want to sort the list values = [4, 1, 7, 3, 9] in ascending
order, which method would you use?'''

values = [4, 1, 7, 3, 9]
sorted_values = sorted(values)
print(sorted_values)



'''Question 7: You have the list cities = ['New York', 'Los Angeles', 'Chicago',
'Houston']. How can you find the index of the item 'Chicago'?'''

cities = ['New York', 'Los Angeles', 'Chicago', 'Houston']
index_num = cities.index('Chicago')
print(index_num)



'''Question 8: Given the list animals = ['dog', 'cat', 'elephant', 'lion'], how can
you replace 'elephant' with 'tiger' and return the last item from the list?'''

animals = ['dog', 'cat', 'elephant', 'lion']
ani_list = animals[2].replace("elephant", "tiger")
print(ani_list)




'''Question 9: If you have the list numbers = [5, 2, 8, 2, 1], what method can
you use to count the number of occurrences of the value 2?'''

list = [5, 2, 8, 2, 1]
list_new = list.count(2)
print(list_new)



'''Question 10: You have the list fruits = ['apple', 'banana', 'cherry']. How can
you reverse the order of the items in the list? can you use to remove and
return the last item from the list?'''

fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)

fruits = ['apple', 'banana', 'cherry']
last_item = fruits.pop()
print(last_item)
print(fruits)  





