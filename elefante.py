def incomodam(n):
    if n == 1:
        return str(("incomoda") * n)
    else:
        return str(("incomodam ") * n)

def elefante(n):
    i = 1
    while i < n:
        if i == 1:
            print("Um elefante muita gente")
            i=i+1
        else:
            print(str(i) + " elefantes  " + incomodam(i) + " muito maaais")
            print(str(i) + " elefantes muita gente")
            i = i + 1
        if i == n:
            return str(i) + " elefantes  " + incomodam(i) + " muito maaais"

print(elefante(5))