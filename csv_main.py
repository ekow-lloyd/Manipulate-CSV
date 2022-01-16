import csv
from csv import writer
import pyinputplus as pyip
import getpass
import pandas as pd

try:         
    def add_stud():
        try:
            while True:
                """This function is to add/append user"""

                print("\nLet's add some info to the database\n")
                item_nmbr =int(input("How many records are you going to add?\nEnter '0' to exit : "))
                if item_nmbr == 0:
                    print('\nReturning to main Menu \n')
                    break
        
                for i in range(item_nmbr):
                    stud_iD = input('\nkindly enter the student id number : \n').lower().title()
                    f_Name = input("Kindly fill in the student's first name : \n").lower().title()
                    l_name = input("Kindly fill in the student's last name : \n").lower().title()
                    cntact = input("Kindly fill in the student's contact info : \n").lower().title()
                    score = input("Kindly fill in the student's score : \n").lower().title()
                    remark = input("Kindly fill in any remark : \n").lower().title()

                    new_pupil = ([stud_iD,f_Name,l_name,cntact,score,remark])

                    with open('Records.csv', 'a') as append_file:
                        writer_object = writer(append_file)
                        writer_object.writerow(new_pupil)
                        append_file.close() 

                print( "\nAction successfully executed\n")
                break

        except ValueError as VE:
            print('\nInvalid Selection, returning to Main menu.\n')


    def delete():
        while True:
            try:
                
                def row_to_delete():
                    while True:
                        data = pd.read_csv('Records.csv',error_bad_lines=False)
                        row = int(input('Enter the row number : '))
                        data = data.drop(row,axis=0)          # the first argument determines whether row(number) or column(name),axis O for rows and 1 for col
                        data.to_csv('Records.csv',index=False,encoding='utf-8')
                    
                def column_to_delete():
                    while True:
                        data = pd.read_csv('Records.csv')
                        column = input('Enter column name to delete : ')
                        data = data.drop(column,axis=1)          # the first argument determines whether row(number) or column(name),axis O for rows and 1 for col
                        data.to_csv('Records.csv',index=False,encoding='utf-8')


                print('\nSelect something to delete or "Quit" to return to main menu\n')
                delete_menu = pyip.inputMenu(["Delete Row", "Delete Column", "Quit"],numbered=True, lettered=False)

                if delete_menu == "Delete Row":
                    row_to_delete()

                elif delete_menu == " ":
                    pass

                if delete_menu == "Delete Column":
                    column_to_delete()

                elif delete_menu == " ":
                    pass

                if delete_menu == "Quit":
                    print('Nothing else to do here, returning to main menu')
                    choices()

            except ValueError as VE:
                print('\nInvalid entry given, or interrupted by user, returning to main menu\n')
            

            except KeyError as KE:
                print('\nNo such key found')
                

            except KeyboardInterrupt as KI:
                print('\nInterrupted by user\n')
                

    def update():
        print("\nLets update some records.")
        while True:
            try:
                
                """This function updates a column, requires row and column"""

                row_update = int(input("\nWhat row number needs to be updated(press enter to return to main menu)? : "))
                column_update = input('\nWhat column name needs to be updated?: ').lower().title()
                new_value = input('\nWhat should be the new value for "{}" of row {}?: \n'.format(column_update,row_update)).lower().title()

                update = pd.read_csv("Records.csv")
                update.loc[row_update, column_update] = new_value
                update.to_csv("Records.csv", index=False)

                print("Changes succesfully carried out!")
            
            except ValueError as VE:
                print('\nBlank or Invalid entry\nReturning to main menu\n')
                choices()

        
    def search_Csv():
        while True:
            
            with open("Records.csv") as search_file:
                reader = csv.reader(search_file)

                find_pupil = input("\nenter name of a student to find: \n").lower().title()
                if find_pupil == '':
                        print('\nNothing entered, returning to main Menu : \n')
                        choices()
                       
                for row in reader:
                    if (row[1]) == find_pupil:                      
                        print('\nRecords of "{}" found'.format(find_pupil))
                        print(row)                        
                      
                    elif (row[2]) == find_pupil:
                        print('\nRecords of "{}" found'.format(find_pupil))
                        print(row)
                
                                                                                                                                                  
    def choices():
        while True:
            query = pyip.inputMenu(["Search", "Add", "Update", "Delete", "Quit"],numbered=1,lettered=False)

            if query == "Add":
                add_stud()

            elif query == "Search":
                search_Csv()
            
            elif query == "Update":
                update()
            
            elif query == "Delete":
                delete()
            
            else:
                if query == "Quit":
                    print('\nYou chose to quit...terminating program.\n')
                    quit()

    def authenticate():
        while True:
            ma = ["Matilda","Naa","dede","Attoh","Brehun"]
            ma1 = ma[2]
            print("\nWelcome , kindly enter your password to gain access to the records")
            password = getpass.getpass()
            if password != ma1:
                    print("Wrong Password")
                    continue
            elif password == ma1:
                print("\nYou have access\n")
                choices()
    authenticate()

except KeyboardInterrupt as KI:
    print('\nStopped by user...Terminating program\n')