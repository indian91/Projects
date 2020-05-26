import os
def stationary():
    os.system('CLS')
    db=shelve.open('supermarket/data.db',writeback=True)
    print(f"Availabel Items in Stationary: ",end='\t')
    for i in db['stationary'].keys():
        print(i,end='\t')
    print('\n')
    s='''\n1.Pen\n2.Register\n3.Books\n4.main menu'''
    print(s)
    time.sleep(1)
    ch=int(input('Enter Choice:  '))
    if ch==1:
        print('Brands of Pens....')
        print('\n')
        s='''\n1.Link\n2.Fine'''
        print(s)
        time.sleep(1)
        ch=int(input('Enter Choice:  '))
        if ch==1:
            print(f"Available Prices in Link Pen: {db['stationary']['pen']['brand']['link']['price']}")
            time.sleep(1)
            price=int(input('Please Select Price for Pen in 5 or 10: '))
            if price==5:
                index=db['stationary']['pen']['brand']['link']['price'].index(5)
                qt=int(input('Enter the Quantity of Pen which you required:  '))
                db['stationary']['pen']['brand']['link']['stock'][index]-=qt
                print(f'You have Selected {qt} Pen of price 5')
                db.close()
                stationary()
            elif price==10:
                index=db['stationary']['pen']['brand']['link']['price'].index(10)
                qt=int(input('Enter the Quantity of Pen which you required:  '))
                db['stationary']['pen']['brand']['link']['stock'][index]-=qt
                print(f'You have Selected {qt} Pen of price 10')
                db.close()
                stationary()
            else:
                print('Price not avialable....')
                time.sleep(1)
                main()
        elif ch==2:
            print(f"Available Prices in Link Pen: {db['stationary']['pen']['brand']['fine']['price']}")
            time.sleep(1)
            price=int(input('Please Select Price for Pen in 5 or 10: '))
            if price==5:
                index=db['stationary']['pen']['brand']['fine']['price'].index(5)
                qt=int(input('Enter the Quantity of Pen which you required:  '))
                db['stationary']['pen']['brand']['fine']['stock'][index]-=qt
                print(f'You have Selected {qt} Pen of price 5')
                db.close()
                stationary()
            elif price==10:
                index=db['stationary']['pen']['brand']['fine']['price'].index(10)
                qt=int(input('Enter the Quantity of Pen which you required:  '))
                db['stationary']['pen']['brand']['fine']['stock'][index]-=qt
                print(f'You have Selected {qt} Pen of price 10')
                db.close()
                stationary()
            else:
                print('Price not avialable....')
                time.sleep(1)
                main()
        else:
            main()
    elif ch==2:
        print('Brands of Registers....')
        print('\n')
        time.sleep(1)
        s='''\n1.Classmate\n2.Icon'''
        print(s)
        time.sleep(1)
        ch=int(input('Enter Choice:  '))
        if ch==1:
            print(f"Available Prices in Classmate Register: {db['stationary']['register']['brand']['classmate']['price']}")
            time.sleep(1)
            price=int(input('Please Select Price for Register in 50 or 80: '))
            if price==50:
                index=db['stationary']['register']['brand']['classmate']['price'].index(50)
                qt=int(input('Enter the Quantity of Register which you required:  '))
                db['stationary']['register']['brand']['classmate']['stock'][index]-=qt
                print(f'You have Selected {qt} Register of price 50')
                db.close()
                stationary()
            elif price==80:
                index=db['stationary']['register']['brand']['classmate']['price'].index(80)
                qt=int(input('Enter the Quantity of Register which you required:  '))
                db['stationary']['register']['brand']['classmate']['stock'][index]-=qt
                print(f'You have Selected {qt} Register of price 80')
                db.close()
                stationary()
            else:
                print('Price not avialable....')
                time.sleep(1)
                main()
        elif ch==2:
            print(f"Available Prices in I-con Register: {db['stationary']['register']['brand']['icon']['price']}")
            time.sleep(1)
            price=int(input('Please Select Price for Register in 5 or 10: '))
            if price==5:
                index=db['stationary']['register']['brand']['icon']['price'].index(5)
                qt=int(input('Enter the Quantity of Register which you required:  '))
                db['stationary']['register']['brand']['icon']['stock'][index]-=qt
                print(f'You have Selected {qt} Register of price 50')
                db.close()
                stationary()
            elif price==10:
                index=db['stationary']['register']['brand']['fine']['price'].index(10)
                qt=int(input('Enter the Quantity of Register which you required:  '))
                db['stationary']['register']['brand']['icon']['stock'][index]-=qt
                print(f'You have Selected {qt} Register of price 60')
                db.close()
                stationary()
            else:
                print('Price not avialable....')
                time.sleep(1)
                main()
        else:
            main()
    elif ch==3:
        print('Avialble Books: ')
        print('\n')
        s='''1.Class VI\n2.Class VII\n3.Class VIII\n4.Class IX\n5.Class X'''
        print(s)
        time.sleep(1)
        ch=int(input('Select the class for Books....    '))
        if ch==1:
            qt=int(input('How many sets u required   '))
            db['stationary']['books']['class VI']['stock']-=qt
            print(f"You select {qt} set of Class VI")
            db.close()
            time.sleep(1)
            stationary()
        elif ch==2:
            qt=int(input('How many sets u required   '))
            db['stationary']['books']['class VII']['stock']-=qt
            print(f"You select {qt} set of Class VII")
            db.close()
            time.sleep(1)
            stationary()
        elif ch==3:
            qt=int(input('How many sets u required   '))
            db['stationary']['books']['class VIII']['stock']-=qt
            print(f"You select {qt} set of Class VIII")
            db.close()
            time.sleep(1)
            stationary()
        elif ch==4:
            qt=int(input('How many sets u required   '))
            db['stationary']['books']['class IX']['stock']-=qt
            print(f"You select {qt} set of Class IX")
            db.close()
            time.sleep(1)
            stationary()
        elif ch==5:
            qt=int(input('How many sets u required   '))
            db['stationary']['books']['class X']['stock']-=qt
            print(f"You select {qt} set of Class X")
            db.close()
            time.sleep(1)
            stationary()
        else:
            print('Books is not avialable for selected classes')
            stationary()
    else:
        main()
