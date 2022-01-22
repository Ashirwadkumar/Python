i=0
result=0
n = int(input("please give a number : "))#taking input form the user 
number1 = n
temp = n
while n!=0:                              #loop 
    n = (n//10)
    i=i+1;
while number1!=0:                        #loop_2
    n=number1%10
    result=result+pow(n,i)
    number1=number1//10
if temp==result:                         #if_else
    print("number is armstrong")
else:
    print("number is not armstrong")
