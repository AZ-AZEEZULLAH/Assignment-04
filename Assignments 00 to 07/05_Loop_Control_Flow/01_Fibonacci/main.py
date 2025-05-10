## Fibonacci


MAX_VALUE :int = 1000


def fibonacci():
    a , b = 0 , 1 
    print(a ,b , end= " ")


    while True :
        c = a + b 

        if c > MAX_VALUE:
            break
        print(c , end= " ") 
        a , b = b , c 




if __name__ == "__main__":
    fibonacci()