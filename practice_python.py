#practice
# unique subjects

# sub = set()

# while True:
#     print("=== MENU ===\n")
#     print(" 1.Add")
#     print(" 2.Remove")
#     print(" 3.Display all")
#     print(" 4.Total count")
#     print(" 5.Exit")
#     ch=int(input("Enter the choice: "))

#     if ch == 1 :
#         s = input("Enter the subject to add: ")
#         sub.add(s)
#         print("\nSubject added!")
#     elif ch == 2 :
#         s = input("Enter the subject to delete: ")
#         sub.remove(s)
#         print("Subject deleted!")
#     elif ch == 3 :
#         print("Displaying all subjects: ",sub)
#     elif ch == 4 :
#         count=0
#         for i in sub:
#             count=count+1
#         print("Total count of unique subject: ",count)
#     elif ch == 5 :
#         print("Exiting...")
#         break
#     else:
#         print("Invalid Choice. Try again...!")



# Common Hobbies

# student_1 = {"painting","playing","gambling","watching movies"}
# student_2 = {"painting","reading","cycling","cooking","playing"}
# hobby = set()
# for i in student_1:
#     for j in student_2:
#         if i == j:
#             hobby.add(i)
# print("Common hobbies are: ",hobby)

# unique_list=set()
# for i in student_1:
#     for j in student_2:
#         if i not in student_2 :
#              unique_list.add(i)
# print("Unique hobbies are: ",unique_list)

# union=[]

# for i in student_1:
#     union.append(i)
# for j in student_2:
#     union.append(j)
    
# print("Union of hobbies are: ",union)


#Check Membership

# fruits = {"logan","rambutan","grapefruit","dragonfruit","avocado"}

# f = input("Enter the fruit name to check: ")
# count=0
# for i in fruits:
#     if f in fruits:
#         count =count+1
#     else:
#         None

# if count == 0:
#     print(f," is not present.")
# else:
#     print(f," is present!")

#---------Tuple problems----------

#student marks

# marks = (100,98,99,67,89)
# highest=marks[0]
# lowest=marks[0]
# for i in marks:
#    if i > highest:
#             highest=i
#    if i < lowest:
#          lowest=i
            
# print("Highest marks: ",highest)
# print("Lowest marks: ",lowest)

#Days of the week

# week = ("monday","tuesday","wednesday","thursday","friday","saturday","sunday")
# print("Printing first three days: ",week[:3])
# print("Print the weekend days (last two): ",week[-2:])
# count=0
# for i in week:
#     if i == "friday":
#         count=count+1
#     else:
#         None
# if count > 0:
#     print("Friday does exist.")
# else:
#     print("Friday doesn't exist.")

# 3. Tuple of Names

# Create a tuple of 5 student names.

# Find the position of a given name using index().

# Count how many times a name appears using count().
# students = ("Asher","Amaya","Govind","Safna","Raashid","Safna","Sourav")

# n = input("Enter a name to find position: ")
# print("Position if the name is at ",students.index(n))
# print("Count of the name: ",students.count(n))


