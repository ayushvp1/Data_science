c=[]

while True:

    print("menu..\n")
    print("1.add items\n")
    print("2.delete items\n")
    print("3.view items 4 to exit\n")
    ch=int(input("Enter the input: "))
    
    if ch == 1:
        item=input("Enter the item to add: ")
        c.append(item)
    elif ch == 2:
        c.pop()
        print("deleted")
    elif ch == 3:
        print(c)
    elif ch == 4:
        print("Exiting...")
        break