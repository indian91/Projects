def electronics():
    global l
    os.system('CLS')
    db=shelve.open('supermarket/data.db',writeback=True)
    s='''1.Mobile\n2.Laptop\n3.main menu'''
    print(s)
    ch=int(input('Enter the choice......'))
    if ch==1:
        count=1
        for i in db['electronics']['mobile']['brand'].keys():
            print(f"{count}.{i}")
            count+=1
        print('4.main menu')
        ch=int(input('Please select mobile...........'))
        if ch==1:
            count=1
            for i in db['electronics']['mobile']['brand']['one plus']['model']:
                print(f"{count}. One Plus {i}")
                count+=1
            print('please select the model of one plus')
            ch=int(input('Enter Choice......'))
            if ch==1:
                index=db['electronics']['mobile']['brand']['one plus']['model'].index('7 pro')
                qt=int(input('Enter the quantity.............'))
                db['electronics']['mobile']['brand']['one plus']['stock'][index]-=qt
                price=db['electronics']['mobile']['brand']['one plus']['price'][index]
                l.append(f"electronics\tmobile\tone plus\t{qt}\t{price}\t{qt*price}")
                print(f"You purchased {qt} set of one plus 7 pro")
                db.close()
                electronics()
            elif ch==2:
                index=db['electronics']['mobile']['brand']['one plus']['model'].index('8 pro')
                qt=int(input('Enter the quantity.............'))
                db['electronics']['mobile']['brand']['one plus']['stock'][index]-=qt
                price=db['electronics']['mobile']['brand']['one plus']['price'][index]
                l.append(f"electronics\tmobile\tone plus\t{qt}\t{price}\t{qt*price}")
                print(f"You purchased {qt} set of one plus 8 pro")
                db.close()
                electronics()
            elif ch==3:
                index=db['electronics']['mobile']['brand']['one plus']['model'].index('7')
                qt=int(input('Enter the quantity.............'))
                db['electronics']['mobile']['brand']['one plus']['stock'][index]-=qt
                price=db['electronics']['mobile']['brand']['one plus']['price'][index]
                l.append(f"electronics\tmobile\tone plus\t{qt}\t{price}\t{qt*price}")
                print(f"You purchased {qt} set of one plus 7")
                db.close()
                electronics()
            else:
                print('Item not available.....')
                db.close()
                electronics()
        elif ch==2:
            count=1
            for i in db['electronics']['mobile']['brand']['iphone']['model']:
                print(f"{count}. I-phone {i}")
                count+=1
            print('please select the model of i-phone')
            ch=int(input('Enter Choice......'))
            if ch==1:
                index=db['electronics']['mobile']['brand']['iphone']['model'].index('6')
                qt=int(input('Enter the quantity.............'))
                db['electronics']['mobile']['brand']['iphone']['stock'][index]-=qt
                price=db['electronics']['mobile']['brand']['iphone']['price'][index]
                l.append(f"electronics\tmobile\tiphone\t{qt}\t{price}\t{qt*price}")
                print(f"You purchased {qt} set of iphone 6")
                db.close()
                electronics()
            elif ch==2:
                index=db['electronics']['mobile']['brand']['iphone']['model'].index('10')
                qt=int(input('Enter the quantity.............'))
                db['electronics']['mobile']['brand']['iphone']['stock'][index]-=qt
                price=db['electronics']['mobile']['brand']['iphone']['price'][index]
                l.append(f"electronics\tmobile\tiphone\t{qt}\t{price}\t{qt*price}")
                print(f"You purchased {qt} set of iphone 10")
                db.close()
                electronics()
            elif ch==3:
                index=db['electronics']['mobile']['brand']['iphone']['model'].index('11')
                qt=int(input('Enter the quantity.............'))
                db['electronics']['mobile']['brand']['iphone']['stock'][index]-=qt
                price=db['electronics']['mobile']['brand']['iphone']['price'][index]
                l.append(f"electronics\tmobile\tiphone\t{qt}\t{price}\t{qt*price}")
                print(f"You purchased {qt} set of iphone 11")
                db.close()
                electronics()
            else:
                print('Item not available.....')
                electronics()
        elif ch==3:
            count=1
            for i in db['electronics']['mobile']['brand']['MI']['model']:
                print(f"{count}.MI {i}")
                count+=1
            print('please select the model of MI')
            ch=int(input('Enter Choice......'))
            if ch==1:
                index=db['electronics']['mobile']['brand']['MI']['model'].index('10 pro')
                qt=int(input('Enter the quantity.............'))
                db['electronics']['mobile']['brand']['MI']['stock'][index]-=qt
                price=db['electronics']['mobile']['brand']['MI']['price'][index]
                l.append(f"electronics\tmobile\tMI\t{qt}\t{price}\t{qt*price}")
                print(f"You purchased {qt} set of MI 10 pro")
                db.close()
                electronics()
            elif ch==2:
                index=db['electronics']['mobile']['brand']['MI']['model'].index('8 pro')
                qt=int(input('Enter the quantity.............'))
                db['electronics']['mobile']['brand']['MI']['stock'][index]-=qt
                price=db['electronics']['mobile']['brand']['MI']['price'][index]
                l.append(f"electronics\tmobile\tMI\t{qt}\t{price}\t{qt*price}")
                print(f"You purchased {qt} set of MI 8 pro")
                db.close()
                electronics()
            elif ch==3:
                index=db['electronics']['mobile']['brand']['MI']['model'].index('8A')
                qt=int(input('Enter the quantity.............'))
                db['electronics']['mobile']['brand']['MI']['stock'][index]-=qt
                price=db['electronics']['mobile']['brand']['MI']['price'][index]
                l.append(f"electronics\tmobile\tMI\t{qt}\t{price}\t{qt*price}")
                print(f"You purchased {qt} set of MI 8A")
                db.close()
                electronics()
            elif ch==4:
                index=db['electronics']['mobile']['brand']['MI']['model'].index('7 pro')
                qt=int(input('Enter the quantity.............'))
                db['electronics']['mobile']['brand']['MI']['stock'][index]-=qt
                price=db['electronics']['mobile']['brand']['MI']['price'][index]
                l.append(f"electronics\tmobile\tMI\t{qt}\t{price}\t{qt*price}")
                print(f"You purchased {qt} set of MI 7 pro")
                db.close()
                electronics()
            elif ch==5:
                index=db['electronics']['mobile']['brand']['MI']['model'].index('6A')
                qt=int(input('Enter the quantity.............'))
                db['electronics']['mobile']['brand']['MI']['stock'][index]-=qt
                price=db['electronics']['mobile']['brand']['MI']['price'][index]
                l.append(f"electronics\tmobile\tMI\t{qt}\t{price}\t{qt*price}")
                print(f"You purchased {qt} set of MI 6A")
                db.close()
                electronics()
                
            else:
                print('Item not avialable......')
        else:
            main()
    elif ch==2:
        count=1
        for i in db['electronics']['laptop']['brand'].keys():
            print(f"{count}.{i}")
            count+=1
        print('4.main menu')
        ch=int(input('Please select laptop...........'))
        if ch==1:
            count=1
            for i in db['electronics']['laptop']['brand']['hp']['model']:
                print(f"{count}. hp {i}")
                count+=1
            print('please select the model of HP')
            ch=int(input('Enter Choice......'))
            if ch==1:
                index=db['electronics']['laptop']['brand']['hp']['model'].index('HP Pavilion Gaming 15')
                qt=int(input('Enter the quantity.............'))
                db['electronics']['laptop']['brand']['hp']['stock'][index]-=qt
                price=db['electronics']['laptop']['brand']['hp']['price'][index]
                l.append(f"electronics\tlaptop\tone plus\t{qt}\t{price}\t{qt*price}")
                print(f"You purchased {qt} set of hp HP Pavilion Gaming 15")
                db.close()
                electronics()
            elif ch==2:
                index=db['electronics']['laptop']['brand']['hp']['model'].index('HP Omen 15')
                qt=int(input('Enter the quantity.............'))
                db['electronics']['laptop']['brand']['hp']['stock'][index]-=qt
                price=db['electronics']['laptop']['brand']['hp']['price'][index]
                l.append(f"electronics\tlaptop\thp\t{qt}\t{price}\t{qt*price}")
                print(f"You purchased {qt} set of hp HP Omen 15")
                db.close()
                electronics()
            elif ch==3:
                index=db['electronics']['laptop']['brand']['hp']['model'].index('HP Spectre x360 (2019)')
                qt=int(input('Enter the quantity.............'))
                db['electronics']['laptop']['brand']['ohp']['stock'][index]-=qt
                price=db['electronics']['laptop']['brand']['hp']['price'][index]
                l.append(f"electronics\tlaptop\thp\t{qt}\t{price}\t{qt*price}")
                print(f"You purchased {qt} set of HP Spectre x360 (2019)")
                db.close()
                electronics()
            else:
                print('Item not available.....')
                db.close()
                electronics()
        elif ch==2:
            count=1
            for i in db['electronics']['laptop']['brand']['samsung']['model']:
                print(f"{count}.SAMSUNG {i}")
                count+=1
            print('please select the model of SAMSUNG')
            ch=int(input('Enter Choice......'))
            if ch==1:
                index=db['electronics']['laptop']['brand']['samsung']['model'].index('Samsung ChromeBook XE50')
                qt=int(input('Enter the quantity.............'))
                db['electronics']['laptop']['brand']['samsung']['stock'][index]-=qt
                price=db['electronics']['laptop']['brand']['samsung']['price'][index]
                l.append(f"electronics\tlaptop\tsamsung\t{qt}\t{price}\t{qt*price}")
                print(f"You purchased {qt} set of samsung Samsung ChromeBook XE50")
                db.close()
                electronics()
            elif ch==2:
                index=db['electronics']['laptop']['brand']['samsung']['model'].index('Samsung ChromeBook 3 XE501C13-K01US')
                qt=int(input('Enter the quantity.............'))
                db['electronics']['laptop']['brand']['samsung']['stock'][index]-=qt
                price=db['electronics']['laptop']['brand']['samsung']['price'][index]
                l.append(f"electronics\tlaptop\tsamsung\t{qt}\t{price}\t{qt*price}")
                print(f"You purchased {qt} set of samsung Samsung ChromeBook 3 XE501C13-K01US")
                db.close()
                electronics()
            elif ch==3:
                index=db['electronics']['laptop']['brand']['samsung']['model'].index('Samsung Spin 7 NP730QAA')
                qt=int(input('Enter the quantity.............'))
                db['electronics']['laptop']['brand']['samsung']['stock'][index]-=qt
                price=db['electronics']['laptop']['brand']['samsung']['price'][index]
                l.append(f"electronics\tlaptop\tsamsung\t{qt}\t{price}\t{qt*price}")
                print(f"You purchased {qt} set of samsung Samsung Spin 7 NP730QAA")
                db.close()
                electronics()
            else:
                print('Item not available.....')
                electronics()
        elif ch==3:
            count=1
            for i in db['electronics']['laptop']['brand']['dell']['model']:
                print(f"{count}.DELL {i}")
                count+=1
            print('please select the model of DELL')
            ch=int(input('Enter Choice......'))
            if ch==1:
                index=db['electronics']['laptop']['brand']['dell']['model'].index('Dell Inspiron Coreo')
                qt=int(input('Enter the quantity.............'))
                db['electronics']['laptop']['brand']['dell']['stock'][index]-=qt
                price=db['electronics']['laptop']['brand']['dell']['price'][index]
                l.append(f"electronics\tlaptop\tdell\t{qt}\t{price}\t{qt*price}")
                print(f"You purchased {qt} set of dell Dell Inspiron Core")
                db.close()
                electronics()
            elif ch==2:
                index=db['electronics']['laptop']['brand']['dell']['model'].index('Dell Inspiron Touchscreen 15 5548 Notebook')
                qt=int(input('Enter the quantity.............'))
                db['electronics']['laptop']['brand']['dell']['stock'][index]-=qt
                price=db['electronics']['laptop']['brand']['dell']['price'][index]
                l.append(f"electronics\tlaptop\tdell\t{qt}\t{price}\t{qt*price}")
                print(f"You purchased {qt} set of dell Dell Inspiron Touchscreen 15 5548 Notebook")
                db.close()
                electronics()
            elif ch==3:
                index=db['electronics']['laptop']['brand']['dell']['model'].index('Dell Vostro 3458')
                qt=int(input('Enter the quantity.............'))
                db['electronics']['laptop']['brand']['dell']['stock'][index]-=qt
                price=db['electronics']['laptop']['brand']['dell']['price'][index]
                l.append(f"electronics\tlaptop\tdell\t{qt}\t{price}\t{qt*price}")
                print(f"You purchased {qt} set of dell Dell Vostro 3458")
                db.close()
                electronics()
                
            else:
                print('Item not avialable......')
                electronics()
        else:
            main()
    else:
        main()
