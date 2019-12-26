# Input for required variables
x = [int(x) for x in input("enter array seprated by one space in each element").split()]
y = int(input("enter variable y"))

# Function to manipulate variables to get desired result
def fun(x,y):
    flag = 'false'
    for i in range(len(x)):
        for item in x:
            index = x.index(item)
            if sum(x[index:index+i+1])>y:
                print(x[index:index+i+1])
                flag = 'true'
                break
        if flag == 'true':
            break
    if flag == 'false':
        print ('no result')

# Calling of Function
fun(x,y)
