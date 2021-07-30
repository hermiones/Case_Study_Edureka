#1.What is the output of the following code?
'''nums =set([1,1,2,3,3,3,4,4])
print(len(nums))'''

#ANS: 4

#2.What will be the output?
'''d ={"john":40, "peter":45}
print(list(d.keys()))'''


#Ans: ['john', 'peter']







#4: Write a for loop that prints all elements of a list and their position in the list
'''a = [4,7,3,2,5,9]
for i in a:
    print("element:",i,"position",a.index(i))'''


#5:Please   write   a   program   which accepts  a   string   from   console   and   print   the characters that have even indexes
string = input("Please enter your input")
for i in string:
    if (string.index(i))%2==0:
        print(i)
