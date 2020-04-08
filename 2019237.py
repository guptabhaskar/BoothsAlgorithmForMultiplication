import time

'''
Input Type- Int,Int
Return Type- String
This function takes two integers num and n where num is the integer whose binary number
of length n is to be returned but if the integer n is negative its twos_complement is to be returned.
'''
def binary(num,n):
	if(num>=0):
		s=bin(num)[2:]
		s=(n-len(s))*'0'+s
		return s
	else:
		return twos_negative(num,n)


'''
Input Type- String
Return Type- String
This function performs arithmetic right shift operation on the input given string and returns the new string. 
'''
def right_shift(s):
	return s[0]+s[0:-1]


'''
Input Type- Int,Int
Return Type- String
This function takes two integers num and n where num is a negative integer whose twos_complement
of length n is to be returned.
'''
def twos_negative(num,n):
	s=bin(abs(num))[2:]		
	s=(n-len(s))*'0'+s
	c=''
	for i in range(n):
		if(s[i]=='0'):
			c+='1'
		else:
			c+='0'	
	s=add_binary(c,'0'*(n-1)+'1')
	return s


'''
Input Type- String,String
Return Type- String
This function uses 2 strings as an argument then return the final string made using 
these 2 binary strings. This also neglects the extra bit in case of overflow.
'''
def add_binary(s1,s2): 
	n=len(s1)
	final=bin(int(s1,2)+int(s2,2))
	final=final[2:]
	if(len(final)>n):
		d=len(final)-n
		return final[d:]
	elif(len(final)<n):
		d=n-len(final)
		final='0'*d+final
		return final
	else:
		return final


'''
Input Type- String
Return Type- String
This function takes a binary string and returns a string containing its twos complement. 
'''
def twos_complement(b):
	n=len(b)
	c=''
	for i in range(n):
		if(b[i]=='0'):
			c+='1'
		else:
			c+='0'										
	b=add_binary(c,'0'*(n-1)+'1')
	return b

	
'''
Input Type- Int,Int
Return Type- Int, String
This function multiples two integers n1 and n2 using booth's algorithm for multiplication 
and returns answer in its integer and binary form.
'''
def multiplication(n1,n2):
	n=8
	acc='0'*n
	q0='0'
	m1=n1
	m2=n2
	if(n1<=0 and n2<=0 and n1>n2):
		m1=n2
		m2=n1
	elif(n1>=0 and n2>=0 and n1<n2):
		m1=n2
		m2=n1
	elif(n1<=0 and n2>=0 and abs(n1)<n2):
		m1=n2
		m2=n1
	elif(n1>=0 and n2<=0 and n1<abs(n2)):
		m1=n2
		m2=n1
	multiplicand=binary(m1,n)
	negmultiplicand=binary(-m1,n)
	multiplier=binary(m2,n)
	for i in range(n):
		s=multiplier[-1]+q0
		if(s=='10'):
			acc=add_binary(acc,negmultiplicand)
		elif(s=='01'):
			acc=add_binary(acc,multiplicand)
		s=acc+multiplier+q0
		acc=right_shift(s)[:n]
		multiplier=right_shift(s)[n:n*2]
		q0=right_shift(s)[n*2]
	if(acc[0]=='0'):
		dec=int(acc+multiplier,2)
	else:
		dec=-int(twos_complement(acc+multiplier),2)
	return dec,acc+multiplier

flag=True
while(flag):
	print("Enter two numbers -")
	a,b=map(int,input().split())												
	dec,_bin=multiplication(a,b)
	print("Result of Multiplication as Integer - "+str(dec))
	print("Result of Multiplication as binary - "+_bin)
	if(int(dec)!=a*b):
		print(a,b,a*b,dec)
		print("ERROR")
	print("Do you want to try again?")
	s=str(input())
	if(s=='no' or s=='n' or s=='No' or s=='NO'):
		flag=False
print("Do you want to test the program?(Y/N)")
s=str(input())
if(s=='Y'):
	start_time=time.time()
	print("This will take time if range is large.")
	print("Enter range for multiplicand:")
	a1,a2=map(int,input().split())
	print("Enter range for multiplier:")
	b1,b2=map(int,input().split())
	flag1=True
	count=1
	for i in range(a1,a2+1):
		if(flag1==False):
			break;
		for j in range(b1,b2+1):
			dec,_bin=multiplication(i,j)
			if(i*j!=dec):
				print("Failed for multiplication of "+str(i)+" "+str(j))
				flag1=False
				break;
			else:
				print("Test "+str(count)+": Passed")
				count+=1
	if(flag1):
		print("---Time taken is %s seconds---" % (time.time() - start_time))
		print ("Passed")
	else:
		print("Failed")