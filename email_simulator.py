# create class with __init__ constructor
class Email():
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        
    has_been_read = False     # create class variable = False

    def mark_as_read(self):
        self.has_been_read = True    # create methond to mark as read = True

# create empty list for inbox
inbox = []

# define function that populates inbox with 3 email instances
def populate_inbox():        
    email_1 = Email(
        email_address = "rafimadni@gmail.com",
        subject_line = "Tasks Added",
        email_content = "Please note your level 2 course content has been added"
    )    
    email_2 = Email(
        email_address = "saji7234@gmail.com",
        subject_line = "New Product",
        email_content = "Our new product has launched and in stores now "
    )
    email_3 = Email(
        email_address = "madinacc01@gmail.com",
        subject_line = "Google Services",
        email_content = "Our terms and conditions have changed, please accept"
    )
    inbox.append(email_1) 
    inbox.append(email_2) 
    inbox.append(email_3)    # append to inbox list

    return inbox 

# create function to list all emails
def list_emails():
    print("Inbox: ")
    index = 1   # let index = 1

    for email in inbox:
        print(f"{index}. {email.subject_line}")   # call subject line
        index += 1    # increment index

def read_email(index):    # index as perimeter in function
    select_email = inbox[index - 1]   # select email at given index
    print("Subject Line: ", select_email.subject_line)
    print("From: ", select_email.email_address)
    print("Content: ", select_email.email_content)

    select_email.mark_as_read()     # call function to mark as True

inbox = populate_inbox()     # populate inbox by calling function

while True:
    try:
        user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))     # promt user for input
       
        if user_choice == 1:
            print("List of emails:")
            for index, email_item in enumerate(inbox):  # use enumerate function to loop through inbox
                print(f"{index + 1}. {email_item.subject_line}")
            
            try:
                selected_index = int(input("Enter the index of the email you would like to read: "))
                if 0 <= selected_index -1 <= len(inbox):
                    print(f"Selected index: {selected_index}")
                    read_email(selected_index)
                else:
                    print("Invalid index chosen, please try again")
            except ValueError:  # error handling added
                print("Incorrect index format, please try again")
            
        elif user_choice == 2:
            index = 1                 
            for unread_email in inbox:
                if not unread_email.has_been_read:
                    print(f"Unread Email Index: {index}, Email address: {unread_email.email_address}")
                    print(f"Subject Line: {unread_email.subject_line}")
                    print(f"Email Content: {unread_email.email_content}")
                index += 1
            
        elif user_choice == 3:
            break   # exit loop
        
        else:
            print("Oops - incorrect input.")
    
    except ValueError:   # error handling added
        print("Incorrect choice made, please try again")
