psw = ["0000-0000", "1111-1111", "2222-2222", "3333-3333", "4444-4444", "5555-5555", "6666-6666", "7777-7777"] #Change passwords
a = 7 #Total passwords
while True:
    user = input("Premi 1\n")
    if user == "1" and a >= 0: #When you press one
        print(psw[0])
        a -= 1
        psw.pop(0)
    elif user == "1" and a <= 0:
        print("Password esaurite") #If you run out of passwords to print
    else:
        print("Errore") #If you write wrong
