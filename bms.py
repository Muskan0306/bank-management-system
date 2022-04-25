import datetime
import os
import time


def balance_sheet(when):
    if when == '':
        when = datetime.datetime.now().strftime('%d-%m-%y')
    fhand = open('data.txt')
    os.system('cls')
    print('Sno.\t       Name        \t    Date and Time    \tCredited/Debited\tNew Balance')
    print('====\t===================\t=====================\t================\t===========')
    c=1
    for i in fhand:
        x = i.split('#')
        if x[2] == when:
            print(c,'\t',x[1].strip(),'\t\t',x[2],'',x[3],'\t',x[5],'\t\t\t',x[4])
            c += 1
    fhand.close()

def createaccount():
    os.system('cls')
    name = input('Name of customer')
    fhand = open('accounts.txt')
    print('Select a username please')
    while True:
        cond = True
        username = input('')
        for i in fhand:
            x = i.split('<.>')
            if username == x[0]:
                print('Please choose a different username as this username already exist')
                cond = False
                break
        if cond == True:
            break
    amount = '0'

    while int(amount) <= 0:
        amount = input('Please deposit some amount of money to get started: ')
        try:
            int(amount)
        except:
            continue
    xim = open('no_acc.txt',"r")
    for i in xim:
        x = int(i)
        break
    acc_num = x+1
    xim.close()
    mi = open('no_acc.txt',"w")
    mi.write(str(acc_num))
    mi.close()
    password = input('What should be your password\n*NOTE* Please let the customer write the password by himself/herself and give him/her private space.\n')
    accountstore = open('accounts.txt','a')
    accountstore.write(str(acc_num)+'<.>'+password+'<.>C\n')
    accountstore.close()
    datainput = open('data.txt',"a")
    date = datetime.datetime.now().strftime('%d-%m-%y')
    tym = datetime.datetime.now().strftime('%H:%M:%S')
    principle = amount
    by = 'Bank'
    store = str(acc_num)+'#'+name+'#'+date+'#'+tym+'#'+principle+'#'+amount+'#self#'+by+'\n'
    datainput.write(store)
    datainput.close()
    print('Your account number is: ',acc_num)
    return [str(acc_num),name]
os.system('cls')
while True:
    acc_type = ''
    print('Please enter the following details to get started. If you don\'t have an account and want to create one contact any bank employee')
    print('================================================================================================================================')
    usern = input('Enter your i\'d/account number here: ')
    passw = input('Enter your password here: ')
    fhand = open('accounts.txt',"r")
    passcheck = None
    for i in fhand:
        acc = i.split('<.>')
        if usern.strip() == acc[0]:
            acc_type = acc[2].rstrip()
            passcheck = acc[1]
    if passcheck == passw.strip() and acc_type != '':
        break
    os.system('cls')
    print('Etiher username or password you have entered is wrong')
os.system('cls')
while acc_type == 'B':
    ip = input('Please enter number corresponding to your work: \n1.Specific day\'s balance sheet \n2.Today\'s balance sheet\n3.Balance sheet of a customer\n4.Create an account of customer\n')
    if ip == '1':
        os.system('cls')
        when = input('Which date entries do you need?')
        balance_sheet(when)
        log = usern+'checked the balance sheet for '+when+' on '+datetime.datetime.now().strftime('%d-%m-%y at %H:%d:%S')+'####\n'
        log_check = open('data.txt','a')
        log_check.write(log)
        log_check.close()
        break
    elif ip == '2':
        balance_sheet('')
        log = usern+' checked the balance sheet for '+datetime.datetime.now().strftime('%d-%m-%y')+' on '+datetime.datetime.now().strftime('%d-%m-%y at %H:%d:%S')+'####\n'
        log_check = open('data.txt','a')
        log_check.write(log)
        log_check.close()
        break
    elif ip == '3':
        acc_num = input('Enter account number of customer\t')
        info = open('data.txt')
        os.system('cls')
        print('Sno.\tTransaction through\t    Date and Time    \tCredited/Debited\tNew Balance')
        print('====\t===================\t=====================\t================\t===========')
        c=1
        for i in info:
            x = i.split('#')
            if x[0] == acc_num:
                name = x[1]
                print(c,'\t',x[7].strip() if x[6] == 'self' else x[6],'\t\t\t',x[2],'',x[3],'\t',x[5],'\t\t\t',x[4])
                c += 1

        print('The balance sheet of Mr./Mrs.',name)
        log = usern+' checked the balance sheet of account number '+acc_num+' on '+datetime.datetime.now().strftime('%d-%m-%y at %H:%d:%S')+'####\n'
        log_check = open('data.txt','a')
        log_check.write(log)
        log_check.close()
        break
    elif ip == '4':
        x = createaccount()
        log = usern+' created an account for Mr./Mrs. '+x[1]+' with account number '+x[0]+' on '+datetime.datetime.now().strftime('%d-%m-%y at %H:%d:%S')+'####\n'
        log_check = open('data.txt','a')
        log_check.write(log)
        log_check.close()
        break
    else:
        os.system('cls')
        print('!!!->Enter a valid input<-!!!')

while acc_type == 'C':
    ip = input('Please enter a number corresponding to your work: \n1.Withdraw or Deposit Money\n2.Check Balance\n3.Mini statement\n4.Money Transfer\n5.Password change\n')
    if ip == '1':
        os.system('cls')
        fhand = open('data.txt',"r")
        acc_num = usern.strip()
        for i in fhand:
            if i[:16] ==  acc_num:
                info = i
        data = info.split('#')
        fhand.close()
        con = input('Confirm name by pressing any key other than \'NO\'\n'+data[1]+'\n')
        if con in ['NO','no','No','nO']:
            print('Try again then')
            os.startfile('bms.py')
            exit()
        date = datetime.datetime.now().strftime('%d-%m-%y')
        tym = datetime.datetime.now().strftime('%H:%M:%S')
        amount = input('amount')
        if amount[0] == '-' and amount > data[4]:
            print('Not enough money in your account.')
            time.sleep(4)
            print('Leaving...')
            time.sleep(4)
            break
        principle = str(int(data[4])+int(amount))
        by = input('By what means:')
        store = acc_num+'#'+data[1]+'#'+date+'#'+tym+'#'+principle+'#'+amount+'#self'+'#'+by+'\n'
        os.system('cls')
        print('Please confirm the below given info: \nYou are Mr./Mrs.',data[1],'\b.Your account number is',acc_num,'you are',"withdrawing ₹" if amount[0]== '-' else "depositing ₹",amount[1:] if amount[0] in ['+','-'] else amount,'\nEnter \'YES\' to confirm\n')
        check = input('Enter YES to confirm or any other key to cancel the transaction\t')
        if check.lower() != 'yes':
            print('Transaction failed!')
            check = input('Do you want to withdraw/deposit money now?\nTo confirm enter YES or any other key to quit\t')
            if check.lower() == 'yes':
                continue
            else:
                print('quiting...')
                time.sleep(2)
                print('Thanks')
                time.sleep(2)
                quit()
        time.sleep(0.5)
        print('processing...')
        time.sleep(2)
        storing = open('data.txt',"a")
        storing.write(store)
        print('Transaction successfull!')
        storing.close()
        break
    elif ip == '2':
        os.system('cls')
        acc_num = usern
        fhand = open('data.txt')
        for i in fhand:
            if i[:16] == acc_num:
                info = i
        data = info.split('#')
        print('Welcome Mr./Mrs.',data[1],'Your last transaction was on',data[2],data[3],'you debited ₹' if data[5][0] == '-' else 'you credited ₹',data[5][1:] if data[5][0] == '-' else data[5] ,'\b. Now your total balance is ₹',data[4],'\nThanks')
        input('press Enter to exit')
        break
    elif ip == '3':
        acc_num = usern
        info = open('data.txt')
        os.system('cls')
        print('Sno.\tTransaction through\t    Date and Time    \tCredited/Debited\tNew Balance')
        print('====\t===================\t=====================\t================\t===========')
        c=1
        for i in info:
            x = i.split('#')
            if x[0] == acc_num:
                print(c,'\t',x[7].strip() if x[6] == 'self' else x[6],'\t\t\t',x[2],'',x[3],'\t',x[5],'\t\t\t',x[4])
                c += 1
        break
    elif ip == '4':
        acc_num = usern
        send_to = input('Enter the account number of the person you need to send money.\t')
        amount = input('How much money do you want to transfer?\t')
        if int(amount) <1:
            print('Not Valid!')
            break
        fhand = open('data.txt')
        to = ''
        for i in fhand:
            if i[:16] == acc_num:
                info = i
            if i[:16] == send_to:
                to = i
        if to == '':
            print('Account number you have entered is wrong.\nLeaving')
            time.sleep(5)
            quit()
        fhand.close()
        data = info.split('#')
        address = to.split('#')
        by = input('By what means are you going to pay?')
        if int(amount) > int(data[4]):
            print('You don\'t have enough money in your account to make this payment.')
            time.sleep(4)
            print('leaving...')
            break
        date = datetime.datetime.now().strftime('%d-%m-%y#%H:%M:%S')
        principle = str(int(data[4])-int(amount))
        store = acc_num+'#'+data[1]+'#'+date+'#'+principle+'#-'+amount+'#'+send_to+'#'+by+'\n'+send_to+'#'+address[1]+'#'+date+'#'+str(int(address[4])+int(amount))+'#'+amount+'#'+acc_num+'#'+by+'\n'
        os.system('cls')
        print('Confirm the following statement:\nYou are Mr./Mrs.',data[1],',your account number is',acc_num,'you are going to transfer ₹',amount,'to Mr./Mrs.',address[1],'account with account number',send_to,'\nPress Enter to continue any other key to exit')
        check = input('')
        if check != '':
            print('Exiting the transfer!')
            print('leaving...')
            break
        print('processing')
        storing = open('data.txt',"a")
        storing.write(store)
        time.sleep(1.5)
        print('Transfer succesfull')
        break
    elif ip == '5':
        os.system('cls')
        while True:
            check = True
            acc_num = usern
            pa = input('Enter your new password here:\t')
            con = input('Confirm your new password here:\t')
            fhand = open('accounts.txt')
            if pa != con:
                os.system('cls')
                print('New passwords not match! Please do it again')
                continue
            for i in fhand:
                x = i.split('<.>')
                if x[0] == usern and pa == x[1]:
                    chec = False
                    os.system('cls')
                    print('New password can\'t be one of the previous passwords')
                    break
            fhand.close()
            if check == True:
                appe = open('accounts.txt','a')
                appe.write(acc_num+'<.>'+pa+'<.>C\n')
    else:
        print('Please enter a valid input!')
