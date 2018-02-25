n=int(input("Enter the n value\n"))


#Pattern_1
'''*
   * *
   * * *
   * * * *
   * * * * *'''
#Loop to generate the number sequence
for i in range(1,n+1):
    #Print the sequence number of times specified pattern
    print(i*'* ')

#Pattern_2
'''
         *
       * *
     * * *
   * * * *
 * * * * *
 '''
#Loop to generate the number sequence
for i in range(1,n+1):
    #To generate the print variable for each i value
    var_str=i*' *'
    #Printing the values with right justifying to achieve desired pattern
    print(var_str.rjust(n*2,' '))


#Pattern_3
'''
     *
    * *
   * * *
  * * * *
 * * * * *
'''
#To find the number of spaces variable
k=2*n-2
#To generate the sequence values
for i in range(1,n+1):
    #To generate the print variable for each i value
    var_str=str(k*' ')+'* '*i
    print(var_str)
    #decrementing k values for displaying next set of values
    k=k-1


#Pattern_4
'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''
var_str=''
#To generate the sequence values
for i in range(1,n+1):
    j=1
    #Inner while loop to formulate the var_str string
    while(j<=i):
        var_str=var_str+str(j)+' '
        j=j+1
    print(var_str)
    var_str=''

#Pattern_5
'''
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
'''
var_str=''
#One print variable for keeping the numbers count
count=0
for i in range(1,n+1):
    j=1
    while(j<=i):
        count=count+1
        var_str=var_str+str(count)+' '
        j=j+1
    print(var_str)
    var_str=''


#Pattern_6
'''
A
B B
C C C
D D D D
E E E E E
'''
#To get the ASCII value of alphabet A
var_init=ord('A')

var_str=''
#Loop variable to list the n values
for i in range(1,n+1):
       var_str=i*(chr(var_init)+' ')
       print(var_str)
       #Incrementing ASCII values
       var_init=var_init+1
       var_str=''


#Pattern_7
'''
A
B C
D E F
G H I J
K L M N O
'''

var_str=''
#To get the ASCII value of alphabet A and subtracting with 1
var_init=ord('A')-1

#Loop variable to list the n values
for i in range(1,n+1):
    j=1
    while(j <= i):
        #Incrementing ASCII values
        var_init=var_init+1
        var_str=var_str+chr(var_init)+' '
        j=j+1
    print(var_str)
    var_str=''
