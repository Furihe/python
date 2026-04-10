def factorial(n):
        if n == 1 :
            return(1)
        else:
            return n * factorial(n-1)

def fact(n):
     fact = 1 
     for i in range(1,n+1):
          fact *=i
     return fact 

n = eval(input("정수를 입력하시오:"))
print(n, "!= ", factorial(n))
print(n, "!= ", fact(n) )
