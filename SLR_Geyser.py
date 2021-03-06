# Linear Regression Raw Formula...Scikit learn or any readymade library not used.
# have used direct mathematical formula in plain cobol program
# Refernce: https://www.geeksforgeeks.org/linear-regression-python-implementation and #https://www.amherst.edu/system/files/media/1287/SLR_Leastsquares.pdf
#https://www.saedsayad.com/gradient_descent.htm

import csv
import numpy as np

def slr(X,Y):
    X_bar = np.mean(X)
    Y_bar = np.mean(Y)

    # Xi-X_bar, Yi-Y_bar
    Xi_Xbar = []
    Xi_Xbar_2 =[]
    Xi_Xbar_mul_Yi_Ybar = []

    for i in range(0,len(X)):
        Xi_Xbar.append( X[i] - X_bar )
        Xi_Xbar_2.append((X[i] - X_bar)*(X[i] - X_bar))
        Xi_Xbar_mul_Yi_Ybar.append((X[i] - X_bar) * (Y[i] - Y_bar))


    final_numerator = np.sum(Xi_Xbar_mul_Yi_Ybar)

    final_denominator = np.sum(Xi_Xbar_2)

    beta_1 = final_numerator/final_denominator

    print(beta_1)

    beta_0 = Y_bar - beta_1 * X_bar

    print(beta_0)     
    # return the beta_0,beta_1 values 
    return(beta_0,beta_1)

# reg_line prediction function 
def reg_line(pred):
    for i in range(0,len(X)):
        y_pred=pred[0] +  pred[1] * X[i]
        print(y_pred)


f = open("C:/Users/573380/Desktop/geyser.csv",'r')

reader = csv.reader(f)

X = []
Y = []

for row in reader:
    if row[1] != "eruptions":
        X.append(float(row[1]))
        Y.append(float(row[2]))

f.close()

pred=slr(X,Y)

#create a reg_line function to use logic prediction=beta_0 + beta_1 * x
reg_line(pred)


