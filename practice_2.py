# #
# items = ["apple","banana","milk"]
# # print(items)
# # print(items[0])
# # print(items[1:3])

# items.append("mango")
# # print(items)


# # if "mango" in items:
# #     print("Item is available")
# # else:
# #     print("item is not available")
# # items.remove("banana")
# # print("items: ",items)

# for i in items:
#     print(i)

# while True: 
#     print("\n")
#     print("1.Add")
#     print("2.View")
#     print("3.listed view")
#     print("4.Remove")
#     print("5.Exit")
#     ch = int(input("Enter the input: "))
    
#     if ch == 1:
#         print("Adding items...")
#         it=input("Enter the item to add: ").strip()
#         if it: 
#             items.append(it)
#             print("Added: ",it)
#         else:
#             print("Empty input ignored.")        
#     elif ch == 2:
#         print("Viewing...\n")
#         print("items :",items)
#     elif ch== 3:
#         print("listed Viewing...\n")
#         for i,it in enumerate(items,start=1):
#             print(i,it)
    
#     elif ch == 4 :
#         print("For Deleting element...")
#         it = input("Enter item to remove: ").strip()
#         if it: 
#             items.remove(it)
#             print("\nitem removed")
#         else:
#             print("Empty input ignored.") 
#     elif ch == 5:
#         break
#     else:
#         print("Invalid input. Please try again...")


inventory = {}

inventory["apple"] = {"price": 50, "quantity": 10}
inventory["banana"] = {"price": 30, "quantity": 20}
inventory["milk"] = {"price": 25, "quantity": 5}
while True: 
    print("\n")
    print("1.Add")
    print("2.View")
    print("3.listed view")
    print("4.Remove")
    print("5.Discount apply")
    print("6.Exit")
    ch = int(input("Enter the input: "))
    
    if ch == 1:
        print("Adding items...")
        name=input("Enter the item name to add: ").strip()
        price=int(input("Enter the price to add: "))
        quantity=input("Enter the quantity to add: ").strip()
        if name: 
            inventory[name] = {"price": price, "quantity": quantity}
            print("Added: ",inventory)
        else:
            print("Empty input ignored.")        
    elif ch == 2:
        print("Viewing...\n")
        print("inventory :",inventory)
    elif ch== 3:
        print("listed Viewing...\n")
        for i,it in enumerate(inventory,start=1):
            print(i,it)
    
    elif ch == 4 :
        print("For Deleting element...")
        name = input("Enter item to remove: ").strip()
        if name: 
            del inventory[name]
            print("\nitem removed")
        else:
            print("Empty input ignored.") 
    elif ch == 5:
        dis = float(input("Enter discount percentage: "))
        for item in inventory:
            inventory[item]["price"] = inventory[item]["price"] * (1 - dis / 100)

        print("Discount applied successfully.")

    elif ch == 6:
        break
    else:
        print("Invalid input. Please try again...")