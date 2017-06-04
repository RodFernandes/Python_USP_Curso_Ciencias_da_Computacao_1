def maximo(x,y,z):
    if(x<=y) and (y<z):
        return z
    elif(x<=y) and(y>z):
        return y
    elif(x>y)and (y>=z):
        return x
    elif(x>y) and (x>z):
        return x
    elif(x>y) and (y<z):
        return z
    elif(x==y) and (y==z):
        return x