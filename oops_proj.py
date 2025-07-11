class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()
 #self.loggedin → an attribute of the object,False → initial value, meaning the user is not logged in yet       
#Why do we use self.menu() inside attributes/__init__() of a class?
#Because we often want certain methods to run immediately when the object is created — like showing a welcome screen or setting things up.        
#You are calling the menu() method from inside the constructor (__init__()), during object creation
    def menu(self):
        user_input = input("""welcome to chatbook, how wouldu like to procedd? 
                            1. press 1 to signup
                            2.press 2 to signin 
                            3.press 3 to  write a post 
                            4.press 4 to message a friend
                            5.press any other key to exit""")
        if user_input == "1":
            pass
        if user_input == "2":
            pass
        if user_input == "3":
            pass
        if user_input == "4":
            pass
        else:
            exit()

obj = chatbook()
#basic structure is ready