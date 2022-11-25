import  nlpcloud

class NLPApp:
    def __init__(self):
        self.__database={}   # esa kiya taki baharse koi access na karle
        self.__first_menu()

    def __first_menu(self):
        inp = input(""" 
        HI! how would you like to proceed?
        1. Register 
        2. Login 
        3. Exit
        
        """)

        if inp=='1':
            self.__register()
        elif inp=="2":
            self.__login()
        else:
            exit()

    def __second_Menu(self):
        inp2 = input(""" 
        HI! how would you like to proceed?
        1. NER
        2. Language Detection 
        3. Sentiment Analyis
        4. Logout

        """)

        if inp2 == '1':
            self.__ner()
        elif inp2 == "2":
            self.__language_detection()
        elif inp2=="3":
            self.__sentiment_analysis()
        else:
            exit()

    def __register(self):
        name = input("Enter Name : ")
        email = input("Enter email : ")  # email ko key banaya he kyuki keys unique hote he in database
        password = input("Enter password : ")

        if email in self.__database:
            print("Account already exists")
        else:
            self.__database[email] = [name,password]
            print("Registeration successful")
            print(self.__database)
            print()
            print("Now Login")
            self.__first_menu()

    def __login(self):
        email = input("Enter email : ")
        password = input("Enter password : ")

        if email in self.__database:
            if password==self.__database[email][1]:
                print("Logged In")
                print()
                self.__second_Menu()

            else:
                print("Try again")
                self.__login()
        else:
            print("The email is not registered")
            print("Register Now")
            self.__first_menu()


    def __ner(self):
        para = input(""" Enter the paragraph : """)
        search = input("\nWhat would you like to search : ")

        client = nlpcloud.Client("finetuned-gpt-neox-20b", "", gpu=True, lang="en")
        response = client.entities(para,searched_entity=search)

    def __language_detection(self):
        pass

    def __sentiment_analysis(self):
        pass




obj=NLPApp()