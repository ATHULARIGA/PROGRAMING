
'''
def factorial(n):
    sum=1
    for i in range(1,n+1) :
        sum=i*sum
    print(sum)

        
        
    
factorial(5)
        
'''
def factorial(n):  
        if(n==0)or(n==1):
            return 1
        else:
            return factorial(n-1)*n

        
        
    
factorial(5)
print(factorial(5))
    
