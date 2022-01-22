class library:
    def __init__(self,list,name):
        self.booklist = list
        self.name = name
        self.lendict = {}
    def displayBooks(self):
        print(f'We have following books in our library: {self.name}')
        for book in self.booklist:
            print(book)
    def lendbook(self,user,book):
        if book not in self.lendict.keys():
            self.lendict.update({book:user})
            print('lender book database has been updated. You can now take the book')
        else:
            print(f'book been already been used by {self.lendict[book]}')
    def addBook(self,book):
        self.booklist.append(book)
        print('Book has been added to the list')
    def returnbook(self,book):
        self.lendict.pop(book)

if __name__ == "__main__":
    harry = library(["python",'Machiine learning','data science',"statistics","Probablity","Algorithm by CLRS"],"Black & White World Lovers")

    while True:
        print(f"Welcome to the {harry.name} library. Enter your choice to continue")

        print("1 to Display Books")
        print("2 to lend a book")
        print("3 to Add a book")
        print("4 to Return a book")

        user_choice = input()
        if user_choice not in ['1','2','3','4']:
            print("Please enter a valid option")
            continue
        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            harry.displayBooks()

        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend: ")
            user = input('Enter your name: ')
            harry.lendbook(user,book)

        elif user_choice == 3:
            book = input("Enter the book you want to add: ")
            harry.addBook(book)

        elif user_choice == 4:
            book = input("Enter the name of the book you want to return: ")
            harry.returnbook(book)

        else:
            print("Not a valid option")


        print("Press q to quit and and c to return back")

        user_choice2 = ""
        while(user_choice2!="c" and user_choice2!="q"):
            user_choice2 = input()
            if user_choice2=="q":
                exit()
            elif user_choice2 == "c":
                continue



