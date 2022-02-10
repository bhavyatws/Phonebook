print("\n\n#############Created By Shahid#########")

    
phonebook={}    
def phonecontact(instruction):
                match instruction:
                    case 0:
                        print(30 * '*')
                        name=input("Enter Name: ")
                        phone_number=int(input("Enter Phone Number: "))
                        print(name,'-',phone_number)
                        phonebook[name]=phone_number
                    case 1:
                        name=input("Enter Name to search contact: ")
                        print(30 * '*')
                        if phonebook.get(name):
                            print(name,'-',phonebook[name])
                            print(30 * '*')
                        else:
                            print(f'Sorry!!,We cannot contact of its{name}.. ')
                        '''print(30 * '*')
                        try:
                            print(name,'-',phonebook[name])
                            print(30 * '*')
                        except KeyError:
                            print(f'Sorry!!,We cannot contact of its{name}.. ')'''
                        
                    case 2:
                        name=input('Enter Name to update existing phone number:')
                        if phonebook.get(name):
                            phone_number=int(input('Enter phone number:'))
                            phonebook.update({name:phone_number})
                            print("Update contact: ",phonebook[name])
                        else:
                            print(f"==>Sorry,{name} name's contact doesnot exist\n So we cannot update")
                    case 3:
                        print(30 * '*')
                        name=input('Enter Name to delete from phonebook: ')
                        if phonebook.get(name):
                        # print("Deleted contact:",phonebook[name])
                            del phonebook[name]
                        else:
                            print(f"==>Sorry,{name} name's contact doesnot exist")
                       
                        
                    case 4:
                        for key,value in phonebook.items():
                            print(f'{key}-{value}')       
       

while True:
        print(50*'*')
        print('''Enter Phonebook Function:
        0-Add Contact
        1-Search
        2-Update
        3-Delete
        4-Show
        ''')
        print(50*'*')
        ins = int(input('Enter function:'))
        phonecontact(ins)
        print(50*'*')
        func=input("Enter y,Y to exit:")
        if func in 'y,Y':
           print('Thank you very much for using this software')
           break