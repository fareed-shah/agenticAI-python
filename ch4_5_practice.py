
#Q1

# lst = [1,2,3,4,5,6]


# print("****** Q1 *******")

# print("total number of elements in list are :",len(lst))
# print("sum of list is :",sum(lst))
# print("smallest number is :",min(lst))

# print("")
# print("****** Q2 *******")


# Q2. 
# lst_index = [10, 20, 30, 40, 50]
# print("elements from index 1 to 3 :",lst_index[1:4])

#Q3.
# print("")
# print("****** Q3 *******")

# lst_name = ['fareed','naveed','usama','ali','junaid']
# print("original name list before append : ",lst_name)
# lst_name.append("zeeshan")
# lst_name.append("qazi")
# print("name list after append : ",lst_name)
# lst_name.sort()
# print("alphabetically sort list : ",lst_name)
# lst_name.pop(-1)
# print("list sorted and last indexd name remove using pop :",lst_name)

#Q4. 
# print("")
# print("****** Q4 *******")

# tup_obj = ('obj1','obj2','obj3','obj4')
# print("length of tupple :",len(tup_obj))
# tup_obj[0] = "changeobject"
# print(tup_obj)
# print("tupple is Immutable and it's value can not be updated aur added after creatopm")


#Q5. 

# print("")
# print("****** Q5 *******")

# tuple_number = (1,2,10,4,10)
# print("first number from tupple : ",tuple_number[0])
# print("last number from tupple : ",tuple_number[-1])
# print("count of 10 in the tupple :",tuple_number.count(10))


# print("")
# print("****** Q6 *******")

# Q6. 

# dict_student={
#     "saad":60,
#     "hassan":90,
#     "murtaza":40
# }
# print("student dictionary keys :",dict_student.keys())
# print("student dictionary values :",dict_student.values())
# print("saad marks :",dict_student["saad"])

#Q7. 

# dict_fruit={
#     "orange":200,
#     "banana":50,
#     "mango":400
# }

# fruit_price=input(" Enter fruit Name  to check it's price :")

# print(dict_fruit.get(fruit_price,"Not available"))

#Q8. 
# Make a set of 5 numbers. Print its length,
#  add one new number using add(), and remove one number using remove(). 
# Print the set after each step.

# set_numbers = {5,10,15,20,25}
# print(" len of set ",len(set_numbers))
# set_numbers.add(45)
# print(" set after adding new number using add ",set_numbers)
# set_numbers.remove(45)
# print(" set after removing  number using add ",set_numbers)



#Q9.
#  Make a list [1, 2, 2, 3, 3, 3, 4].
#  Convert it into a set, print the unique values, and print the count of unique values.

# lst_n = [1, 2, 2, 3, 3, 3, 4]
# set_list=set(lst_n)
# print(type(set_list))

#Q10. Ask the user for 5 numbers one by one,
#  store them in a list, 
# then print the list in sorted order and also print the list reversed.

# lst_n1 = int(input("enter first number "))
# lst_n2 = int(input("enter first number "))
# lst_n3 = int(input("enter first number "))
# lst_n4 = int(input("enter first number "))
# lst_n5 = int(input("enter first number "))
# new_lst=[lst_n1,lst_n2,lst_n3,lst_n4,lst_n5]
# print(new_lst)
# new_lst.sort()
# print(new_lst)
# new_lst.reverse()
# print(new_lst)