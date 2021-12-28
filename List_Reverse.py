a = [10,3,3,4,1,3,5,6,78,21]
a.sort()

print(a)


print(a[::-1])


number_list = []
n = int(input("Enter the list size : "))
print("\n") #new line character
for i in range(0,n):
    print("Enter number at index : ")
    item = int(input())
    number_list.append(item)
    reverse_number_list = number_list[::-1]
print("user_list", number_list,reverse_number_list)



