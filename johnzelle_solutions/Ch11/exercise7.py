def innerProd(X, Y):
    innerProd = 0.0
    for i in range(len(X)):
        innerProd = innerProd + X[i]*Y[i]
    return innerProd

def main():
    X = [1,2,1]
    Y = [1,1,3]
    P = innerProd(X,Y)
    print("The innerproduct of X and Y is ", P)


main() 
