#lets start with all the basic step of understanding python

#1
print('hello world ')

#2
#variable 

x=4 # int integer
y=3.14 #float
a= 'a' #char
b='Hello' #string

liste = ["alo",46,3.25,'t'] #list  liste : can be modified
ens = {"clos",55,"n"} #set cant be modified 

print('------------------------------- all variable type --------------------------------')
print(x,"\n",y,"\n",a,"\n",b,"\n",liste,"\n",ens)
print('here was all the value')

#3
#insert value  spreadout
print('------------ Get Value example -------------------------')
user_value = input('what s you name : ')
print(f'So your name is {user_value}')

print(' ------ for the number')

user_age = int(input(" Give me your age : :"))
print(f'you are {user_age} years old ')
print('------------------------------------------------------------')

#4
#conditionnal

if user_age >= 18 : 
    print('vous etes majeur')
elif 0< user_age < 18 :
    print('vous etes mineur')
else :
    print('Value Error')

print("  <=    >=    <   >    ==  ")
print('-------------------- you saw conditionnal ----------')
