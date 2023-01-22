
def incomodam(n):
    if n == 1:
        return str(("incomoda") * n)
    else:
        return str(("incomodam ") * n)


def elefantes(n, num=1):
    if num <= 0 or n <= 0:
        return ""
    if num == 1 :
        print("Um elefante " + incomodam(num)+ " muita gente")
        return elefantes(n-1,num+1)
    else:
        print(str(num) + " elefantes  " + incomodam(num) + " muito maaais")
        print(str(num) + " elefantes muita gente")
        if n == 1:
            return str(num) + " elefantes  " + incomodam(num) + " muito maaais"
    return elefantes(n-1,num+1)

elefantes(5)