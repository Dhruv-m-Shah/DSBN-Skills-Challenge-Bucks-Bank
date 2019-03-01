def checkOverDraft(account_number, draw_amount):
    if(UserBalance[account_number]-draw_amount-1<0 and UserServicePlan[account_number] == "Everyday"):
        print("TRANSACTION NOT ALLOWED CANNOT GO BEYOND ZERO DOLLAR OVERDRAFT LIMIT")
        main()
    if(UserBalance[account_number]-draw_amount<0 and UserServicePlan[account_number] == "Unlimited"):
        if(UserBalance[account_number]-draw_amount<-250):
            print("TRANSACTION NOT ALLOWED CANNOT GO BEYOND ZERO DOLLAR OVERDRAFT LIMIT")
            main()
    if(UserBalance[account_number]-draw_amount<0 and UserServicePlan[account_number] == "All-Inclusive"):
        if(UserBalance[account_number]-draw_amount<-500):
            print("TRANSACTION NOT ALLOWED CANNOT GO BEYOND ZERO DOLLAR OVERDRAFT LIMIT")
            main()

def transactionCheck(account_number):
    if(UserServicePlan[account_number] == "Everyday"):
        UserBalance[account_number]-=1
    if(UserServicePlan[account_number] == "Unlimited"):
        if(TransactionAmount[account_number]>25):
            UserBalance[account_number]-=0.5
        if(UserBalance[account_number]<0):
            UserBalance[account_number]-=2
    if(UserServicePlan[account_number] == "All-Inclusive" and UserBalance[account_number]<0):
        UserBalance[account_number]-=1

def Display_Menu():
    print("Input the number of the option you wish to choose")
    print("1. Choose Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Pay Bill")
    print("    a. Add Payee")
    print("    b. Pay Bill")
    print("    c. Automatic Bill Payment")
    print("5. Current Balance")
    print("6. Monthly Transaction List")
    print("7. Change Service Plan")
    print("8. Advance one month")
    print("9. EXIT")

def Current_Balance(account_number):
    print(UserBalance[account_number])
def Add_Payee(account_number):
    print("ENTER COMPANY NAME AND THEN ACCOUNT NUMBER. BOTH INPUTS SEPERATED BY A SPACE")
    companyname = input()
    accountnumber = int(input())
    UserPayee[account_number].append((companyname, account_number))

def Automatic_Bill_Payment():
    print(1)
    #Ran out of time

def Pay_Payee(account_number):
    print("ENTER ACCOUNT NUMBER OF PAYEE")
    PayeeAccountNumber = int(input())
    print("ENTER AMOUNT TO PAY")
    PayeeAmount = float(input())
    checkOverDraft(account_number)
    transactionCheck(account_number)
    UserBalance[account_number] -= PayeeAmount
    UserBalance[PayeeAccountNumber] +=PayeeAmount
 
def Pay_Bill(account_number):
    print("Input lower case alphabetic letter of your choice")
    print("    a. Add Payee")
    print("    b. Pay Bill")
    print("    c. Automatic Bill Payment")
    choice = input()
    if(choice == "a"):
        Add_Payee(account_number)
    if(choice == "b"):
        Pay_Payee(account_number)
    if(choice == "c"):
        Automatic_Bill_Payment(account_number)

def Monthly_Transaction_List(account_number):
    for i in range(len(TransactionList[account_number])):
        print(TransactionList[account_number][i])

def Change_Service_Plan(account_number):
    service = input()
    UserServicePlan[account_number] = service()

def MonthlyServiceFee(account):
    if(UserServicePlan[account] == "All-Inclusive"):
        UserBalance[account] -= 25
    if(UserServicePlan[account] == "Unlimited"):
        UserBalance[account] -= 12.50
    if(UserServicePlan[account] == "Everyday"):
        UserBalance[account] -= 0

def InterestFee(account):
    if(0<=UserBalance[account]<=4999.99):
        UserBalance[account] = UserBalance[account]*1.0
    if(5000<=UserBalance[account]<=9999.99):
        UserBalance[account] = UserBalance[account]*1.1
    if(10000<=UserBalance[account]<=24999.99):
        UserBalance[account] = UserBalance[account]*1.2
    if(25000<=UserBalance[account]<=59999.99):
        UserBalance[account] = UserBalance[account]*1.3
    if(60000<=UserBalance[account]<=5000000):
        UserBalance[account] = UserBalance[account]*1.4
    if(5000000.01<=UserBalance[account]):
        UserBalance[account] = UserBalance[account]*1.5


def Advance_One_Month():
    for i in UserBalance:
        MonthlyServiceFee(i)
        InterestFee(i)
        TransactionList[i].clear()


def Deposit(account_number):
    print("ENTER AMOUNT TO DEPOSIT")
    DepositAmount = float(input())
    UserBalance[account_number]+=DepositAmount
    transactionCheck(account_number)
    TransactionAmount[account_number] +=1
    TransactionList[account_number].append(("Deposit", DepositAmount))


def Withdraw(account_number):
    print("ENTER AMOUNT TO WITHDRAW")
    WithdrawAmount = float(input())
    checkOverDraft(account_number, WithdrawAmount)
    UserBalance[account_number]-=WithdrawAmount
    transactionCheck(account_number)
    TransactionAmount[account_number] +=1
    TransactionList[account_number].append(("Withdraw", WithdrawAmount))

def Change_Service_Plan(account_number):
    print("ENTER SERVICE PLAN. CASE SENSITIVE(exact same lettering as service plan provided on sheet)")
    plan = input()
    UserServicePlan[account_number] = plan


#USER DATABASE****************
UserBalance = {1 : 1000, 2 : 2000, 3: 4000, 5: 50, 6: 500, 7: 10000, 8: 100000, 9: 1000000, 10: 72, 11:650, 12: 75000000, 13: 56435, 14: 29, 15: 0}
TransactionList = {1: [], 2: [], 3: [], 5:[], 6:[], 7: [], 8: [], 9:[], 10: [], 11: [], 12: [], 13: [], 14: [], 15: []}
TransactionAmount = {1: 0, 2: 0, 3: 0, 5:0, 6:0, 7: 0, 8: 0, 9:0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0}
UserServicePlan = {1: "", 2: "", 3: "", 5:"", 6:"", 7: "", 8: "", 9:"", 10: "", 11: "", 12: "", 13: "", 14: "", 15: ""}
UserPayee = {1: [], 2: [], 3: [], 5:[], 6:[], 7: [], 8: [], 9: [], 10: [], 11: [], 12: [], 13: [], 14: [], 15: []}
#USER DATABASE****************


global account_number

def main():
    month = 0
    while(True):
        Display_Menu()
        x = int(input())
        if(x == 1):
            account_number = int(input())
        elif(x==2):
            Deposit(account_number)
        elif(x==3):
            Withdraw(account_number)
        elif(x == 4):
            Pay_Bill(account_number)
        elif(x == 5):
            Current_Balance(account_number)
        elif(x == 6):
            Monthly_Transaction_List(account_number)
        elif(x==7):
            Change_Service_Plan(account_number)
        elif(x == 8):
            month+=1
            Advance_One_Month()
        elif(x == 9):
            print("HAVE A NICE DAY!")
            break
        
        
main()
