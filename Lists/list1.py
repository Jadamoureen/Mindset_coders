#find the index of Biscuts

#basket_list = ["chocolates","Biscuts","shoes","comb"]

#index method helps finding the index of an item
# item = basket_list.index("Biscuts")

# print(item)

#positive index
#negative index / reverse index

#would like to print comb using indexing

#print(basket_list[-1])

#using an append method to add pajamas to our initial list
# basket_list.append('pajamas')
# print(basket_list)

#basket_list = ["chocolates","Biscuts","shoes","comb"]
#nested data  ["socks", "tshirt", "pajamas"] add them to the list

#Solomon
#basket_list.append( ["socks", "tshirt", "pajamas"] )

#basket_list.extend( ["socks", "tshirt", "pajamas"] )

#using insert method add item toothbrush to the index 3 should be added to our initial list

#basket_list.insert(3, "toothbrush")


# using remove method clear the last item of the list

#basket_list.remove("comb")

#using reverse method, reverse the list
#basket_list.reverse()

#print(basket_list)

#what is the difference between append method and insert method

#lst = [1,2,2,3,4,5,6,6,7,8,9,2,4,3,5]

#using the count method, how many times does 2 occur

#print(lst.count(2))

#what is the sum of the list

# answer = sum(lst)

# print(answer)

# count = 0

# for number in lst:
#     count += number

# print(count)


#lst = [1,2,2,3,4,5,6,6,7,8,9,2,4,3,5]


#Dictionaries - paired key and value
# { }

#dict = {"name":"Solomon","school":"Ndejje","age":19,"study":"Python"}

# what is Solomon's age ?

#answer_2 = dict["age"]

#where does Solomon go to school

#answer = dict["school"]

#change the age from 19 to 16
#dict["age"]=16


#dict = {"name":"Solomon","school":"Ndejje","age":19,"study":"Python"}

#add a nested data of Solomon's work - "work":["UN","Standard chartered","Ndejje","State House"]

#dict["work"] = ["UN","Standard chartered","Ndejje","State House"]

#print(dict)

#lst = [1,2,2,3,4,5,6,6,7,8,9,2,4,3,5]

# pop method

# popped_item = lst.pop()
# print(popped_item)
# print(lst)

#lst = [1,2,2,3,4,5,6,6,7,8,9,2,4,3]
#using pop and index method remove interger 9

item = lst.index(9)

lst = [1,2,2,3,4,5,6,6,7,8,9,2,4,3,5]

#looking for the position of 9
num = lst.index(9)

#removing the interger 9
item = lst.pop(num)

print(lst, item)
print(lst)

#print(item)



