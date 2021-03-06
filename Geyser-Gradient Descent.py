#!/usr/bin/env python
# coding: utf-8

# In[11]:


# 1) Automatically stop the code once your gradient descent process reaches the minimum point

# 2) Select the optimal alpha value using multiple values of alpha.
# Used Raw formula for gradient decesnt- have used only SLR due to complexity. this wil be extended further adding input variables
#Reference-https://www.saedsayad.com/gradient_descent.htm
#https://www.geeksforgeeks.org/gradient-descent-in-linear-regression/

import csv



def predict(new_X,betas):

    return betas[0]+new_X*betas[1]



def calculate_rss(betas):

    rss = 0



    for idx in range(0,len(X)):

        pred_Y = predict(X[idx],betas)

        actual_Y = Y[idx]



        error = actual_Y - pred_Y
        
        print("iterations",iterations,error,actual_Y,pred_Y)



        rss = rss + (error*error)



    return rss



f = open("C:/Users/573380/Desktop/geyser.csv",'r')



reader = csv.reader(f)



X = []

Y = []



for row in reader:

    if row[1] != "eruptions":

        X.append(float(row[1]))

        Y.append(float(row[2]))



f.close()



# Alpha Value

learning_rate = 0.005



# Maximum steps

MAX_ITERATIONS = 0



# Have your Gradient Descent Reached to Minimum value of Cost Function or max_iterations (steps) are crossed

converge = False



# Initial Beta (coefficient) values

betas = [0,0]



# Number of Rows 

n = len(X)
print("no of rows",n)



# Number of steps gradient descent process has taken

iterations = 0



while (not converge):




    rss = calculate_rss(betas)



    print("\n\n\nRSS Before Step:",rss)



    summation_beta_0 = 0

    summation_beta_1 = 0

    for i in range(len(X)):

        summation_beta_0 = summation_beta_0 + (predict(X[i],betas) - Y[i])

        summation_beta_1 = summation_beta_1 + ((predict(X[i],betas) - Y[i])*X[i])

    

    partial_derivative_wrt_beta_0 = (1/n)*summation_beta_0

    partial_derivative_wrt_beta_1 = (1/n)*summation_beta_1





    betas[0] = betas[0] - (learning_rate*partial_derivative_wrt_beta_0)

    betas[1] = betas[1] - (learning_rate*partial_derivative_wrt_beta_1)



    print("\nBeta Values after Step:",betas)



    print("\nRSS after Step:",calculate_rss(betas))

    print("========================================================")



    if iterations == MAX_ITERATIONS:

        converge = True



    iterations = iterations + 1 


# In[ ]:




