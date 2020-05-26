def cosmatic():
    global l
    print('Avialable Items in Cosmatic.....')
    db=shelve.open('supermarket/data.db',writeback=True)
    count=1
    for i in db['cosmatic'].keys():
        print(f"{count}.{i}")
        count+=1
    print(f"{count}.main menu")
    ch=int(input('Please enter any choice....'))
    if ch==1:
        print('Select the brand of bodylotion....')
        s='''1.Joy\n2.Vaseline'''
        print(s)
        ch=int(input('Enter Choice: '))
        if ch==1:
            print('Avialable prices in Joy: ')
            print(db['cosmatic']['bodylotion']['brand']['joy']['price'])
            try:
                price=int(input('Please enter price for joy'))
                index=db['cosmatic']['bodylotion']['brand']['joy']['price'].index(price)
                qt=int(input('Enter the quantity......'))
                db['cosmatic']['bodylotion']['brand']['joy']['stock'][index]-=qt
            except Exception as e:
                print('Please enter valid price')
                cosmatic()
            else:
                l.append(f"Cosmatic\tBodylotion\tJoy\t{qt}\t{price}\t{qt*price}")
                print(f'You select {qt} of Joy')
                db.close()
                cosmatic()
        elif ch==2:
            print('Avialable prices in Vaseline: ')
            print(db['cosmatic']['bodylotion']['brand']['vaseline']['price'])
            try:
                price=int(input('Please enter price for vasseline'))
                index=db['cosmatic']['bodylotion']['brand']['vaseline']['price'].index(price)
                qt=int(input('Enter the quantity......'))
                db['cosmatic']['bodylotion']['brand']['vaseline']['stock'][index]-=qt
            except Exception as e:
                print('Please enter valid price')
                cosmatic()
            else:
                
                l.append(f"Cosmatic\tBodylotion\tVaseline\t{qt}\t{price}\t{qt*price}")
                print('You select {qt} of Joy')
                db.close()
                cosmatic()
        else:
            print('Not Avialable...')
            cosmatic()
    elif ch==2:
        print('Avialable Soaps:  ')
        s='''1.LifeBoy\n2.Dettol\n3.Godrej No.1'''
        print(s)
        ch=int(input('Enter Choice: '))
        if ch==1:
            print('Avialable prices in Lifeboy: ')
            print(db['cosmatic']['soap']['brand']['lifeboy']['price'])
            try:
                price=int(input('Please enter price for lifeboy'))
                index=db['cosmatic']['soap']['brand']['lifeboy']['price'].index(price)
                qt=int(input('Enter the quantity......'))
                db['cosmatic']['soap']['brand']['lifeboy']['stock'][index]-=qt
            except Exception as e:
                print('Please enter valid price')
                cosmatic()
            else:
                
                l.append(f"Cosmatic\tSoap\tLifeBoy\t{qt}\t{price}\t{qt*price}")
                print(f'You select {qt} of Lifeboy')
                db.close()
                cosmatic()
        elif ch==2:
            print('Avialable prices in Dettol: ')
            print(db['cosmatic']['soap']['brand']['dettol']['price'])
            try:
                price=int(input('Please enter price for Dettol'))
                index=db['cosmatic']['soap']['brand']['dettol']['price'].index(price)
                qt=int(input('Enter the quantity......'))
                db['cosmatic']['soap']['brand']['dettol']['stock'][index]-=qt
            except Exception as e:
                print('Please enter valid price')
                cosmatic()
            else:
                
                l.append(f"Cosmatic\tSoap\tDettol\t{qt}\t{price}\t{qt*price}")
                print(f'You select {qt} of Dettol')
                db.close()
                cosmatic()
                
        elif ch==3:
            print('Avialable prices in godrej no.1: ')
            print(db['cosmatic']['soap']['brand']['godrej no.1']['price'])
            try:
                price=int(input('Please enter price for Godrej No. 1'))
                index=db['cosmatic']['soap']['brand']['godrej no.1']['price'].index(price)
                qt=int(input('Enter the quantity......'))
                db['cosmatic']['soap']['brand']['godrej no.1']['stock'][index]-=qt
            except Exception as e:
                print('Please enter valid price')
                cosmatic()
            else:
               
                l.append(f"Cosmatic\tSoap\tGodrej No.1\t{qt}\t{price}\t{qt*price}")
                print(f'You select {qt} of Godrej No.1')
                db.close()
                cosmatic()
        else:
            print('Item not avialable')
            cosmatic()
    elif ch==3:
        print('Avialable Creams:  ')
        s='''1.Boroplus\n2.Fair Handsome\n3.Meglow'''
        print(s)
        ch=int(input('Please eneter choice: '))
        if ch==1:
            print('Avialable prices in Boroplus: ')
            print(db['cosmatic']['cream']['brand']['boroplus']['price'])
            try:
                price=int(input('Please enter price for Boroplus'))
                index=db['cosmatic']['cream']['brand']['boroplus']['price'].index(price)
                qt=int(input('Enter the quantity......'))
                db['cosmatic']['cream']['brand']['boroplus']['stock'][index]-=qt
            except Exception as e:
                print('Please enter valid price')
                cosmatic()
            else:
               
                l.append(f"Cosmatic\tCream\tBoroplus\t{qt}\t{price}\t{qt*price}")
                print(f'You select {qt} of Boroplus')
                db.close()
                cosmatic()
        elif ch==2:
            print('Avialable prices in fair Handsome: ')
            print(db['cosmatic']['cream']['brand']['fair Handsome']['price'])
            try:
                price=int(input('Please enter price for Fair Handsome'))
                index=db['cosmatic']['cream']['brand']['fair Handsome']['price'].index(price)
                qt=int(input('Enter the quantity......'))
                db['cosmatic']['cream']['brand']['fair Handsome']['stock'][index]-=qt
            except Exception as e:
                print('Please enter valid price')
                cosmatic()
            else:
                
                l.append(f"Cosmatic\tCream\tFair Handsome\t{qt}\t{price}\t{qt*price}")
                print(f'You select {qt} of Fair Handsome')
                db.close()
                cosmatic()
                
        elif ch==3:
            print('Avialable prices in Meglow: ')
            print(db['cosmatic']['cream']['brand']['meglow']['price'])
            try:
                price=int(input('Please enter price for Meglow'))
                index=db['cosmatic']['cream']['brand']['meglow']['price'].index(price)
                qt=int(input('Enter the quantity......'))
                db['cosmatic']['cream']['brand']['meglow']['stock'][index]-=qt
            except Exception as e:
                print('Please enter valid price')
                cosmatic()
            else:
                
                l.append(f"Cosmatic\tCream\tMeglow\t{qt}\t{price}\t{qt*price}")
                print(f'You select {qt} of Meglow')
                db.close()
                cosmatic()
        else:
            print('Item Not Avialable...')
            cosmatic()
    elif ch==4:
        print('Avialable Perfumes:  ')
        s='''1.Denver\n2.Park Avenue\n3.Fogg'''
        print(s)
        ch=int(input('Please eneter choice: '))
        if ch==1:
            print('Avialable prices in Denver: ')
            print(db['cosmatic']['perfume']['brand']['denver']['price'])
            try:
                price=int(input('Please enter price for Denver'))
                index=db['cosmatic']['perfume']['brand']['denver']['price'].index(price)
                qt=int(input('Enter the quantity......'))
                db['cosmatic']['perfume']['brand']['denver']['stock'][index]-=qt
            except Exception as e:
                print('Please enter valid price')
                cosmatic()
            else:
                
                l.append(f"Cosmatic\tPerfume\tDenver\t{qt}\t{price}\t{qt*price}")
                print(f'You select {qt} of Denver')
                db.close()
                cosmatic()
        elif ch==2:
            print('Avialable prices in Park Avenue: ')
            print(db['cosmatic']['perfume']['brand']['park avenue']['price'])
            try:
                price=int(input('Please enter price for Park Avenue'))
                index=db['cosmatic']['perfume']['brand']['park avenue']['price'].index(price)
                qt=int(input('Enter the quantity......'))
                db['cosmatic']['perfume']['brand']['park avenue']['stock'][index]-=qt
            except Exception as e:
                print('Please enter valid price')
                cosmatic()
            else:
               
                l.append(f"Cosmatic\tPerfume\tPark Avenue\t{qt}\t{price}\t{qt*price}")
                print(f'You select {qt} of Park Avenue')
                db.close()
                cosmatic()
                
        elif ch==3:
            print('Avialable prices in Fogg: ')
            print(db['cosmatic']['perfume']['brand']['fogg']['price'])
            try:
                price=int(input('Please enter price for Fogg'))
                index=db['cosmatic']['perfume']['brand']['fogg']['price'].index(price)
                qt=int(input('Enter the quantity......'))
                db['cosmatic']['perfume']['brand']['fogg']['stock'][index]-=qt
            except Exception as e:
                print('Please enter valid price')
                cosmatic()
            else:
                
                l.append(f"Cosmatic\tPerfume\tFogg\t{qt}\t{price}\t{qt*price}")
                print(f'You select {qt} of Fogg')
                db.close()
                cosmatic()
        else:
            print('Item Not Avialable...')
            cosmatic()
    else:
        main()
        
