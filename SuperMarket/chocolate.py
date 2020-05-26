def chocolate():
    global l
    print('\n')
    db=shelve.open('supermarket/data.db',writeback=True)
    print('Available Chocolates:  ')
    count=1
    for i in db['chocolate'].keys():
        print(f"{count}.{i}")
        count+=1
    print('6.main menu')
    ch=int(input('Please select Chocolate'))
    if ch==1:
        print(f"Avialable Prices Are: \t {db['chocolate']['dairymilk']['price']}")
        try:    
            price=int(input('Please Select Price for DairyMilk: '))
            index=db['chocolate']['dairymilk']['price'].index(price)
        except Exception as e:
              print('Please Select Valid Price')
              chocolate()
        else:
            qt=int(input('Please Enter Quantity of Chocolate: '))
            db['chocolate']['dairymilk']['stock'][index]-=qt
            l.append(f"Chocolate\tCadbury\tDairyMilk\t{qt}\t{price}\t{qt*price}")
            print(f"You purchased {qt} DairyMilk of {price}rs.")
            db.close()
            chocolate()
    elif ch==2:
        try:
            print(f"Avialable Prices Are: \t {db['chocolate']['munch']['price']}")
            price=int(input('Please Select Price for Munch: '))
            index=db['chocolate']['munch']['price'].index(price)
        except Exception as e:
            print('Please Select Valid Price.....')
            chocolate()
        else:
            qt=int(input('Please Enter Quantity of Chocolate: '))
            db['chocolate']['munch']['stock'][index]-=qt
            l.append(f"Chocolate\tNestle\tMunch\t{qt}\t{price}\t{qt*price}")
            print(f"You purchased {qt} Munch of {price}rs.")
            db.close()
            chocolate()
    elif ch==3:
        try:
            print(f"Avialable Prices Are: \t {db['chocolate']['kit-kat']['price']}")
            price=int(input('Please Select Price for Kit-Kat: '))
            index=db['chocolate']['kit-kat']['price'].index(price)
        except Exception as e:
            print('Please Select Valid Price.....')
            chocolate()
        else:    
            qt=int(input('Please Enter Quantity of Chocolate: '))
            db['chocolate']['kit-kat']['stock'][index]-=qt
            l.append(f"Chocolate\tNestle\tKit-Kat\t{qt}\t{price}\t{qt*price}")
            print(f"You purchased {qt} Kit-Kat of {price}rs.")
            db.close()
            chocolate()
    elif ch==4:
        try:
            print(f"Avialable Prices Are: \t {db['chocolate']['five star']['price']}")
            price=int(input('Please Select Price for Five Star: '))
            index=db['chocolate']['five star']['price'].index(price)
        except Exception as e:
            print('Please Select Valid Price.....')
            chocolate()
        else:    
            qt=int(input('Please Enter Quantity of Chocolate: '))
            db['chocolate']['five star']['stock'][index]-=qt
            l.append(f"Chocolate\tNestle\tFive star\t{qt}\t{price}\t{qt*price}")
            print(f"You purchased {qt} Five Star of {price}rs.")
            db.close()
            chocolate()
    elif ch==5:
        try:
            print(f"Avialable Prices Are: \t {db['chocolate']['perk']['price']}")
            price=int(input('Please Select Price for Perk: '))
            index=db['chocolate']['perk']['price'].index(price)
        except Exception as e:
            print('Please Select Valid Price.....')
            chocolate()
        else:    
            qt=int(input('Please Enter Quantity of Chocolate: '))
            db['chocolate']['perk']['stock'][index]-=qt
            l.append(f"Chocolate\tNestle\tPerk\t{qt}\t{price}\t{qt*price}")
            print(f"You purchased {qt} Perk of {price}rs.")
            db.close()
            chocolate()
    else:
        print('Item Not avialable.......')
        db.close()
        main()
