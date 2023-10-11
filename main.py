
# This is Account Class to store account holders details
class Accounts:
    # this is a default constructor which gets triggered when called
    # This takes in the following arguments and saves them init.
    def __init__(self,name,gender,aadhar,pan,dob,phone,address,accountNo,ifscCode,accountType,password,balance):
        self.name=name
        self.gender=gender
        self.aadhar=aadhar
        self.pan=pan
        self.dob=dob
        self.phone=phone
        self.address=address
        self.accountNo=accountNo
        self.ifscCode=ifscCode
        self.accountType=accountType
        self.password=password
        self.balance=balance

    # This method is used to display the details if the account holder
    def display(self):
        print("\n")
        print("---Account Details---")
        print("Name: "+ self.name)
        print("Aadhar: "+self.aadhar)
        print("PAN: "+self.pan)
        print("DOB: "+self.dob)
        print("Phone Number: "+self.phone)
        if self.gender == 1:
            print("Gender: Male")
        elif self.gender == 2:
            print("Gender: Female")
        print("Address: "+self.address)
        print("AccountNo: "+self.accountNo)
        print("IFSC Code: "+self.ifscCode)
        if self.accountType == 1:
            print("Account Type: Savings")
        elif self.accountType == 2:
            print("Account Type: Current")
        print("Balance: "+str(self.balance))

# Here we are importing all the funtions from the validate.py and adminVerify.py files
from validate import *
from adminVerify import *

# Here we are creating a list to save all the objects we are going to create to access it easily. 
# This best when the accounts can increase dynamically
accountsData=[]

# This function is used to start the application
def start():
    # This falg is used to check if the user wants to close the application or not
    flag=True
    
    # This loop will run unitil the flag is set to False i.e the user wants to close the application
    while(flag):
        print("\n")
        print("---Amdocs Banking System---")
        print("\n")
        print("1. Employee Login")
        print("2. Customer Login")
        print("3. Close Application")
        # Here choice is used to get access to specific data is database based on choice after authentication
        choice=int(input("Enter Your Choice: "))
        print("\n")
        
        if choice==1:
            # This will get executed when the user has selected Employee Login and asks the credentials 
            print("-----Employee Login-----")
            username=input("Username: ")
            password=input("Password: ")
            # Here it checks if the credentials are true
            if verifyAdminAccount(username,password):
                # This will get executed only if the credentials are true
                print("Login Successful")
                while True:
                    print("\n")
                    print("Operations?")
                    print("1. Open A Account")
                    print("2. Display All The Accounts")
                    print("3. Close An Account")
                    print("4. Update Account Details")
                    print("5. Get Details of a specific Account")
                    print("6. Add Money in an Account")
                    print("7. Exit")
                    choice=int(input("Enter Your Choice: "))
                    # Now based on the choice the respective Operation is executed
                    print("\n")
                    if choice == 1:
                        # This is open an account
                        # This loop will run until a valid entery is done
                        while True:
                            # here it is asking for the type of account it should be 1 or 2
                            accountType=int(input("Select Account Type: 1.Savings ; 2.Current : "))
                            # Here we are verifying if it is valid or not
                            if not verifyAccountType(accountType):
                                print("Invalid Account Type! Please Enter It Again.")
                            # if it is valid then the loop will be breaked
                            else:
                                break
                        # similar to above
                        while True:
                            name=input("Enter Name: ")
                            if not verifyName(name):
                                print("Invalid Name! Please Enter It Again.")
                            else:
                                break
                        while True:
                            gender=int(input("Select gender: 1.Male ; 2.Female : "))
                            if not verifyGender(gender):
                                print("Invalid! Please Enter It Again.")
                            else:
                                break
                        while True:
                            DOB=input("Enter DOB: ")
                            if not verifyDOB(DOB):
                                print("Invalid DOB! Please Enter It Again.")
                            else:
                                break
                        while True:
                            PAN=input("Enter PAN: ")
                            if not verifyPAN(PAN):
                                print("Invalid PAN! Please Enter It Again.")
                            else:
                                break
                        while True:
                            aadhar=input("Enter Aadhar: ")
                            if not verifyAadhar(aadhar):
                                print("Invalid Aadhar! Please Enter It Again.")
                            else:
                                break
                        while True:
                            phone=input("Enter Phone Number: ")
                            if not verifyPhone(phone):
                                print("Invalid Phone Number! Please Enter It Again.")
                            else:
                                break
                        # Here the user enters the address
                        print("Enter the address:")
                        houseNo=input("House: ")
                        city=input("City: ")
                        state=input("State: ")
                        # Here the address is getting appending
                        address=houseNo + " , " + city + " , " + state
                        # Here an abject named account is created using Accounts class
                        # All the required arguments are added
                        # Along with the generate account no funtion which generates account number using city, state and account Type
                        # Also generate IFSC  funtion generates IFSC Code using city and state
                        account=Accounts(name,gender,aadhar,PAN,DOB,phone,address,generateAccountNo(city,state,accountType),generateIFSC(city,state),accountType,generatePassword(PAN,phone),balance=0)
                        # Now that object is added in the list
                        accountsData.append(account)
                        print("\n")
                        print("Successful!")
                        # this method is called with prints the details of the account created
                        account.display()
                        
                    elif choice==2:
                        # This will display all the accounts using for loop which iterates through all the accounts database list we have created
                        print("Accounts:")
                        for i in accountsData:
                            i.display()
                    
                    elif choice==3:
                        # Here account number is taken as an input
                        accountNo=input("Enter The Account No. To Close: ")
                        # Now we will be iterating though all the accounts and 
                        #when it matches with the input account humber then that object in that index is remove from the list
                        for i in accountsData:
                            if i.accountNo==accountNo:
                                accountsData.remove(i)
                        print("Account Closed")
                    
                    elif choice==4:
                        # Here account number is taken as an input
                        accountNo=input("Enter The Account No. of the account you want to update: ")
                        print("Choose what do you want to update.")
                        print("1. Name")
                        print("2. DOB")
                        choice=int(input("Enter your choice: "))
                        # Here based on the choice we will iterate through the accounts database and when it is matched
                        # The following data is modified
                        for i in accountsData:
                            if i.accountNo==accountNo:
                                if choice==1:
                                    # This loop will run untill valid entery is made
                                    while True:
                                        name=input("Enter Name: ")
                                        if not verifyName(name):
                                            print("Invalid Name! Please Enter It Again.")
                                        else:
                                            i.name=name
                                            print("Account Details Updated")
                                            break
                                # similar as above
                                elif choice==2:
                                    while True:
                                        DOB=input("Enter DOB: ")
                                        if not verifyDOB(DOB):
                                            print("Invalid DOB! Please Enter It Again.")
                                        else:
                                            i.dob=DOB
                                            print("Account Details Updated")
                                            break
                        
                    elif choice==5:
                        # This is used to search an account
                        print("Search Account Based on:")
                        print("1. Name")
                        print("2. AccountNo")
                        while True:
                            choice=int(input("Enter your choice: "))
                            # Here based on the choice we will iterate through the accounts database and when it is matched
                            # The following data is fetched
                            if choice==1:
                                name=input("Enter The Name of The Account Holder: ")
                                for i in accountsData:
                                    if i.name==name:
                                        i.display()
                                        break
                            elif choice==2:
                                accountNo=input("Enter The AccountNo of The Account Holder: ")
                                for i in accountsData:
                                    if i.accountNo==accountNo:
                                        i.display()
                                        break
                            else:
                                print("Invalid choice!")
                            break
                                
                        
                    elif choice==6:
                        # Here the user enters the account number and amount to be deposited
                        accountNo=input("Enter The Account No.: ")
                        amount=int(input("Enter The amount to be deposited: "))
                        # so we will be iterating through the database and when the account number is matched we will
                        # add the specified ammount to that account
                        for i in accountsData:
                            if i.accountNo==accountNo:
                                i.balance=i.balance+amount
                                print("Balance Updated Successfully!")
                                break
                    
                    elif choice==7:
                        # This is exit from the recurring loop
                        print("Thank You!")
                        break
                        
                    else:
                        # It will be printed if invalid input is given by the user
                        print("Invalid Choice")
            
            else:
                # this will get executed if the employee has enterted invalid credentials
                print("Invalid Username/Password")
        
        elif choice==2:
            # This will get executed when the user has selected Customer Login and asks the credentials 
            print("-----Customer Login-----")
            print(" ** Password Hint: First 4 letters of PAN followed by last 4 number of the mobile number **")
            username=input("Account No.: ")
            password=input("Password : ")
            # This check variable is used to check if the username and Password combinations is valid
            check=False
            for i in accountsData:
                if i.accountNo==username and i.password==password:
                    print("Login Successful")
                    # if the credentials are valid it will be executed
                    check=True
                    while True:
                        print("\n")
                        print("What do you want to do?")
                        print("1. Update Account Details")
                        print("2. Withdaw")
                        print("3. Transfer")
                        print("4. Balance Enquiry")
                        print("5. Exit")
                        choice=int(input("Enter Your Choice: "))
                        print("\n")
                        
                        if choice==1:
                            
                            print("Choose what do you want to update.")
                            print("1. Name")
                            print("2. DOB")
                            choice=int(input("Enter your choice: "))
                            if choice==1:
                                while True:
                                    name=input("Enter Name: ")
                                    if not verifyName(name):
                                        print("Invalid Name! Please Enter It Again.")
                                    else:
                                        i.name=name
                                        print("Account Details Updated Successfully!")
                            elif choice==2:
                                while True:
                                    DOB=input("Enter DOB: ")
                                    if not verifyDOB(DOB):
                                        print("Invalid DOB! Please Enter It Again.")
                                    else:
                                        i.dob=DOB
                                        print("Account Details Updated Successfully!")
                                    
                        elif choice==2:
                            # Here we will first check if he can withdraw if not it will throw an error
                            amount=int(input("Enter the amount you want to withdraw: "))
                            if i.balance>=amount:
                                i.balance=i.balance-amount
                                print("Windraw Successful")
                                print("Updated balance is "+str(i.balance))
                            else:
                                print("insufficient balance")
                        
                        elif choice==3:
                            
                            accountNoT=input("Enter The Account No. you want to transfer: ")
                            amount=int(input("Enter the amount you want to Transfer: "))
                            if i.balance>=amount:
                                i.balance=i.balance-amount
                                for j in accountsData:
                                    if j.accountNo==accountNoT:
                                        j.balance=j.balance+amount
                                        print("Transfer Successful")
                                        print("Updated balance is "+str(i.balance))
                                        break
                            else:
                                print("insufficient balance")
                            
                        
                        elif choice==4:
                            print("Account Balance: "+str(i.balance))
                            
                        elif choice==5:
                            print("Thank You!")
                            break
                        else:
                            print("Invalid Choice")
                    break
            if(check==False):
                print("Invalid Username/Password")
            
            
        elif choice==3:
            flag=False
            print("Thank You!")
        else:
            print("Invalid Choice")

# Here i am stating the application   
start()