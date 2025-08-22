lib=()

while True:
    print("=== Library Book Tracker ===\n")
    print("1. Add item")
    print("2. Delete item")
    print("3. Viewing")
    print("4. Search")
    print("5. Count")
    print("6. Exit")

    ch=int(input("Enter the choice input: "))

    if ch == 1:
        print("Adding new Book\n ")
        book = input("Enter new book name: ")
        lib.add(book)
        print("\nBook Added!")
    
    elif ch == 2:
        print("Removing the Book\n")
        book = input("Enter the book name to delete: ")
        lib.remove(book)
        print("book deleted")
        
    elif ch == 3:
        print("Viewing all books: \n")
        print(lib)
  
    elif ch ==4:
       book=input("Enter the book to search: ")
       if book in lib:
        print(book, " is available in library")
       else:
        print(book," is not found")
        
    elif ch ==5:
       print("Total number of books: ")
       print(len(lib))

    elif ch == 6:
        print("Exiting....")
        break
    else:
        print("Invalid choice try again....")
        
