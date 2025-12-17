# recursive function

def show(n):
    if (n == 0):
        return
    print(n) #
    show(n-1)
    
show(5)
    
    
#---using factorial function in recursion-------
def fact(n):
    if (n == 0 or n == 1):
        return 1
    return fact(n-1)*n

print(fact(6))


#Q1----- Write a recursive function to calculate the sum of frist n natural numbers.
def calc_sum(n):
    if (n == 0):
        return 0
    return calc_sum(n-1) + n

sum = calc_sum(5)
print(sum)

#Q2 --- Write a recursive function to print all element in a list
        # Hint: use list & index as parametar
        
def print_list(list, idx=0):
    if (idx == len(list)):
        return
    print(list[idx]) 
    print_list(list, idx+1)
    
fruits = ["manago", "apple", "banana", "orange", "litchi"]
print_list(fruits)