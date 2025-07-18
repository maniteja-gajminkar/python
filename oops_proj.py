class chatbook:
    __user_id = 1

    def __init__(self):
        self.id = chatbook.__user_id #here values to use declared outside we need to use with class,whihc are static values/methods
        chatbook.__user_id +=1
        self.__name = "Default User"
        self.username = ''
        self.password = ''
        self.loggedin = False
        #self.menu()
 #self.loggedin → an attribute of the object,False → initial value, meaning the user is not logged in yet       
#Why do we use self.menu() inside attributes/__init__() of a class?
#Because we often want certain methods to run immediately when the object is created — like showing a welcome screen or setting things up.        
#You are calling the menu() method from inside the constructor (__init__()), during object creation
    @staticmethod #static method wil use dirctly from class
    def get_id():
        return chatbook.__user_id
    #Note static method doesnt required object means it doesn't required self
    @staticmethod
    def set_id(val):
        chatbook.__user_id = val

    def get_name(self): #getter
        return self.__name
    
    def set_name(self, value): #setter
        self.__name = value
    
        

    def menu(self):
        user_input = input("""welcome to chatbook, how wouldu like to procedd? 
                            1. press 1 to signup
                            2.press 2 to signin 
                            3.press 3 to  write a post 
                            4.press 4 to message a friend
                            5.press any other key to exit""")
        if user_input == "1":
            self.sign_up()
            #here self.signup() it means object has already created for class chatbook (obj = chatbook())
            # fom that obnject its calling method ,Object calling methods not even after obj creation also works
            # self.sign_up() → calling method using the current object (obj)
# in simple words The object is already created: obj = chatbook()
# So self = obj
        if user_input == "2":
            self.sign_in()
        if user_input == "3":
            self.my_Post()
        if user_input == "4":
            self.sendingmsg()
        else:
            exit()

    def sign_up(self):
        email = input("enter your email here:")
        password = input("enter your password here:")
        self.username = email
        self.password = password
        print("you have signedup with credentials succefully")
        print("\n")       
        self.menu()
        
    def sign_in(self):
        if self.username == '' and self.password == '':
# self.username is initialized as an empty string ''
# self.password is also initialized as an empty string ''
# The following line checks whether a user has signed up or not:
#if self.username == '' and self.password == '':
    # If both username and password are still empty,
    # it means no account has been registered yet.
    #print("Press signup first by pressing the mainmenu")
    # This prevents the user from trying to sign in before signing up.
    # Without this check, the program would allow login attempts
    # even though there's no saved user to compare credentials with.            
            print("press signup first by pressing the mainmenu")
        else:
            uname = input("enter your email here:")
            password = input("enter your password here:")
            if self.username == uname and self.password == password:
                print("youhave signed in successfully")
                self.loggedin = True
            else:
                print("pls enter correct credentials")
            print("\n")
            self.menu()

    def my_Post(self):
        if self.loggedin == True:
            txt = input("enter the text message to write a pos")
            print(f"follwoing content has been posted --> {txt}")
        else:
            print("please you need to sign in first to write a message")
            print("\n")
            self.menu()

    def sendingmsg(self):
        if self.loggedin == True:
            txt = input("enter your message here")
            frnd = input("whom to send the message")
            print(f"your message has been sent to {frnd}")
        else:
            print("please you need to sign in first to write a message")
            print("\n")
            self.menu()





        
if __name__ == "__main__":
    user1 = chatbook()  # Only runs when this file is executed directly
# if __name__ == "__main__": 
# So it only runs when oops_proj.py is executed directly.
#basic structure is ready
# __name__ is a special variable in Python.
# When a file is run directly, __name__ becomes "__main__".
# When the same file is imported in another script, __name__ becomes the module name.
# This allows us to control what runs directly vs. what runs on import.

