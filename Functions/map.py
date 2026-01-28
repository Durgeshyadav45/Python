# create a map function
#---Reusability (function )
def squre(x):
    return x * x

number = [1, 4, 3, 2, 6, 7]
result = map(squre, number)
print(list(result))

# #Real life examples discount apply with lambda function------
# price = [120, 140, 180, 230, 450]

# discount = list(map(lambda x:x-20, price))

# # -------- without map()----------
# numbers = [1, 2, 4, 5, 6, 7]
# result = []

# for i in numbers:
#     result.append(i*2) 
# print(result)

# #------ using Map():----------
# numbers = [1, 2, 3, 4, 5]

# result = list(map(lambda x:x *2, numbers))
# print(result)


#----- Multiple iterables-----
 

     