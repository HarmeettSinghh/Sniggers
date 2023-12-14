
str=input('enter; ')
rev=""
a=len(str)
for i in range( 0,a-1):
    rev=str[i]+rev
print(rev)