num = int(input("Enter a number:"))
while num != 0:
    if num % 2 == 0:
        print(num,"is even.")
    else:
        print(num,"is odd")
    num= int(input("Enter another number( or 0 to exit):"))
    print("goodbye!")

output:Enter a number:55
55 is odd
Enter another number( or 0 to exit):0
goodbye!



numbers_list = []
i = 1
while i <=5:
    j=1
    while j <= i:
        print("* ",end="")
        j += 1
    print() 
    i += 1


output:
*
* *
* * *
* * * *
* * * * *
    
    
    
numbers_list = []
num = 1
while num <= 20:
    numbers_list.append(num)
    num += 1
print(numbers_list)


output:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

 
 
 numbers = []
num = 20
while num >= 1:
    numbers.append(num)
    num -= 1
print(numbers)

output:[20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]




for i in range(1, 6):
    if i == 3:
        break 
    print(i)

for i in range(1, 6):
    if i == 3:
        continue  
    print(i)

output:1
2
1
2
4
5
1
2
4
5


for i in range(1, 6):
    if i == 3:
        pass  
    else:
        print(i)
