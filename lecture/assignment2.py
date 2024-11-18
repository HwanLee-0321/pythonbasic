front = 0
end = 1
n = int(input("max_num="))
while(n >= front):
    print(front, end=" ")
    front, end = end, end + front