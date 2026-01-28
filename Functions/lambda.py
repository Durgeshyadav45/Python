# Normal Function
def squre(x):
    return x * x

#----- Use Lambda function----- 
squre = lambda x:x*x    #-----sort and One line code

# Main Use Lambda------
number = [1, 3, 2, 4, 5]
print(list(map(lambda x:x*2, number))) #------ do not write loop function

salary = [10000, 12000, 15000, 180000]
print(list(map(lambda x:x*1.1, salary)))


