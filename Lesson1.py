#Переменные и типы данных

#Числа
#
# a = 5
# b = 5.0
#
# print (a)
#
# str_1 = "Text"
# str_2 = 'Text'
#
# str_3 = str_1.replace("xt", "t")
#
# print(str_3)
#
# print(str_3.replace("t", "T"))
#
# #Лист List
#
# a_list = list()
# b_list = []
#
# print(type(a_list))
# print(type(b_list))
#
# b_list.append(1)
# b_list.append(2)
# b_list.append(3)
# print(b_list)
#
# b_list.extend([1, 2, 3])
# print(b_list)
#
# b_list.reverse()
# print(b_list)
#
# b_list.remove(1)
# print(b_list)
#
# b_list.pop(0)
# print(b_list)
#
# #dict
#
# a_dict = dict()
# b_dict = {}
# c_dict = {"key": 12}
#
# #set
#
# a_set = set()
#
# #bool
#
# a_bool = True
# b_bool = False
#
# #tuple
#
# a_tuple = tuple ()


#task_1
name = input("How is your name?")
print("Hello,", name, "!")

a = int(input("Add side of square1:"))
square = a ** 2
print("Square ={}".format(square))