from bs4 import BeautifulSoup
import requests
# import urllib.request
import time
import emoji

print("\n\t\t\t\t WELCOME TO MINI GOOGLE")
print("\t\t--------------------------\u2764--------------------------")
print("\n\t\t\t-----------MENU CARD--------------")
print("\n\t\t\U0001F449 Search your favourite places near you")
print("\n\t\t\U0001F449 You can search by pincode ")
print("\n\t\t\U0001F449 You can search by area \n")


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

dict = {}
check = 0
def information_by_pincode(place, pincode):
    res = requests.get(
        f'https://www.google.com/search?rlz=1C1ONGR_enIN977IN977&tbs=lf:1,lf_ui:2&tbm=lcl&sxsrf=AOaemvI6gwntMDHHsgtYiIGkifdrQx-5Lg:1638536618897&q={place}+near+{pincode}+phone+number&rflfq=1&num=10&sa=X&ved=2ahUKEwiImfvI2Mf0AhUjSGwGHWDrAEoQjGp6BAgLEF0&cshid=1638536672002223&biw=1366&bih=657&dpr=1#rlfi=hd:;si:;mv:[[19.4381055,72.8371334],[19.4023987,72.8151962]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:2', headers=headers)
    print("searching in Mini Google.....")
    print("\t\t\tPlease , Wait for few seconds")
    soup = BeautifulSoup(res.text, 'html.parser')
    for i in range(5):
        # printing emoji
        print("\U0001F9D0", end=" ")
        time.sleep(1)

        # checking for correct pin code

        if(len(str(pincode)) < 6 or len(str(pincode)) > 6):
            n = len(str(pincode))
            print("\n\nSORRY! NOTHING FOUND ")
            print("enter correct pincode")
            print(f"you have entered {n} digit of pincode.")
            exit()  # it will exit the program.

    print("\nfound your results ", "\n")
    time.sleep(1)

    # printing list of found results

    print("___________________")
    print('''      |NO OF     |                  |          ''')
    print('''RATING|REVIEWS   |NAME OF {P}     |EXTRA INFO'''.format(
        P=place.upper()))
    print("___________________")
    for i in range(6):
        location = soup.select('.rllt__details')[i].getText()
        print("|", location, "\n")
        print("|_______________________________")
        

        #area and place
def information_by_area(place, area):
    res = requests.get(
        f'https://www.google.com/search?rlz=1C1ONGR_enIN977IN977&tbs=lf:1,lf_ui:2&tbm=lcl&sxsrf=AOaemvI6gwntMDHHsgtYiIGkifdrQx-5Lg:1638536618897&q={place}+near+{area}+phone+number&rflfq=1&num=10&sa=X&ved=2ahUKEwiImfvI2Mf0AhUjSGwGHWDrAEoQjGp6BAgLEF0&cshid=1638536672002223&biw=1366&bih=657&dpr=1#rlfi=hd:;si:;mv:[[19.4381055,72.8371334],[19.4023987,72.8151962]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:2', headers=headers)
    print("searching in Mini-Google.....")
    print("\t\t\tPlease , Wait for few seconds")
    soup = BeautifulSoup(res.text, 'html.parser')
    for i in range(5):
        # printing emoji
        print("\U0001F9D0", end=" ")
        time.sleep(1)
    print("\nfound your results ", "\n")
    time.sleep(1)
    # printing list of found results
    print("___________________")
    print('''      |NO OF     |                  |          ''')
    print('''RATING|REVIEWS   |NAME OF {P}     |EXTRA INFO'''.format(
        P=place.upper()))
    print("___________________")
    for i in range(6):
        location = soup.select('.rllt__details')[i].getText()
        print("|", location, "\n")
        print("|_______________________________")

while(1):
    check = check+1    #check is used for history checking.
    place = input("what place are you looking for...")
    print(f"\n\tHow do you want to find {place}??")
    print("\n\tChoose 1 for area wise sorting  \n\tchoose 0 for pincode wise sorting   ")
    choice = int(input("enter your choice here: "))
    if (choice == 0):
        pincode = int(input("enter pincode: "))
        dict.update({place: pincode})
        information_by_pincode(place, pincode)
    elif(choice == 1):
        area = input("enter your area: ")
        dict.update({place: area})
        information_by_area(place, area)

    if(check>=2):    
        print("DO YOU WANT TO SEE YOUR HISTORY: ")
        response = input("enter yes or no: ")
        if (response == "yes" or "Yes" or "YES" ):
            print("\n\t You have used Mini-Google",check," times")
            print(dict)
            print("\n\tWanna search again or exit??     ")
            response2 = int(input("\tchoose 1 for next search and 0 for exit   "))
            if(response2==0):
                print("\t\tTHANK YOU FOR USING MINI GOOGLE")
                exit()
            elif(response2==1):
                continue
            else:
                print("You have entered wrong input ")
                time.sleep(1)
                print("Program is being shut")
                print("\t\tTHANK YOU FOR USING MINI GOOGLE")
                exit()
        elif(response=="no" or "No" or "NO" or "nO"):
            again = input("Wanna search again?? Enter y/n: ")
            if(again=="y" or again=="Y"):
                continue
            elif(again =="n" or "N"):
                print("\t\tTHANK YOU FOR USING MINI GOOGLE ")
                exit()

        else:
            print("You have entered wrong input ")
            print("\t\tTHANK YOU FOR USING MINI GOOGLE")
            exit()
    search = input("Do you want to search again?\n y or n  ")
    if (search=="y" or search == "Y"):
        continue
    else:
        print("\t\t----THANK YOU FOR USING MINI GOOGLE---- ")
        exit()