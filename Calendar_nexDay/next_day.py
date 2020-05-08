x=input('Enter date in dd/mm/yyyy format ')

date=int(x.split('/')[0])
month=int(x.split('/')[1])
year=int(x.split('/')[2])
if date > 31 or date <1:
    print('Invalid Date')
elif date>30 and month in [4,6,9,11]:
    print('Ivalid Date')
elif date > 28 and month==2 and year%4!=0:
    print('Invalid Date')
elif date > 29 and month==2:
    print('Invalid Date')
elif date==29 and month==2:
    print(f'Next Date is : 1/{month+1}/{year}')
        
elif date==28 and month==2 and year%4!=0:
    print(f'Next date is : 1/{month+1}/{year}')
    
elif date==30 and month in [4,6,9,11]:
    print(f'Next Date is : 1/{month+1}/{year}')

elif date==31 and month in [1,3,5,7,8,10]:
    print(f'Next Date is : 1/{month+1}/{year}')

elif date==31 and month==12:
    print(f'Next Date is : 1/1/{year+1}')

else:
    print(f'Next Date is :{date+1}/{month}/{year}')
