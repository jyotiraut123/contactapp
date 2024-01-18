#contacts App in python
contacts={}
def add_contact():
    contact_no= int(input("Enter Contact Number:"))
    if not contact_no in contacts:
        name= input("Enter Name:")
        contacts[contact_no]=name
    else:
        print("Contact Number already exist")
    return

def search_contact():
    contact_no=int(input("Enter Contact Number to search:"))
    if contact_no in contacts:
        print(f'Contact Details\n Name: {contacts.get(contact_no)} and Contact_no:{contact_no}')
    else:
        print("No Matching Record Found")
    return
def all_contacts():
    for k,v in contacts.items():
        print("name is ", v,"contact no is", k)
    
def update_contact():
    contact_no=int(input("Enter Contact Number to Update:"))
    if contact_no in contacts:
        print("Enter Name to Update")
        name=input("Enter name: ")
        contacts.update({contact_no:name})
    else:
        print("Number not Found")
    return
def del_contact():
    contact_no=int(input("Enter Contact Number:"))
    if contact_no in contacts:
        contacts.pop(contact_no)
    else:
        print("number not found")
    return

def exit_contact():
    print("contact number Exiting")
    
    
while True:
    ch= int(input("Enter Choice:\n1.Add Contact\n2.Search Contact\n3.Display all contacts\n4.Upadate Contact\n"\
                  "5.Delete Contact\n6.Exit"))
    match ch:
        case 1:
            add_contact()
        case 2:
            search_contact()
        case 3:
            all_contacts()
        case 4:
            update_contact()
        case 5:
            del_contact()
        case 6:
            exit_contact()
            break

