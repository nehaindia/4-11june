#!/usr/bin/python2

def factorial(num):
	if num==1:
		return num
	else:
		return num*factorial(num-1)



num=input("enter number")

if num<0:
	print("fact cannt be of negative number")

elif num==0:
	print("fact is 1")

else :
	print("factorial of givn number is" , factorial(num))

 

