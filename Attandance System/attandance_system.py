def take_attandance():
    import time
    f=open('attandance.txt')
    data=f.read()
    name=data.split('\n')
    name=name[0].split('\t')[-1].split(' ')
    f.close()
    x=time.strftime("%d-%m-%y")
    f=open('attandance.txt','a')
    s=x+'\t'
    f.write(s)
    print('Please input A for Absent and P for Present')
    for i in  range(len(name)-1):
        status=input(f'{name[i]}: ')
        s=f'{status} '
        f.write(s)
    f.write('\n')
    f.close()
def count_attandance():
    f=open('attandance.txt')
    f.seek(0)
    data=f.read()
    data1=data.split('\n')
    l1=[]
    for i in data1:
        l1.append(i.split('\t')[-1].split(' '))
    for i in range(10):
        l2=[]
        for j in range(len(l1)-1):
            l2.append((l1[j][i]))
        P=l2.count('P')+l2.count('p')
        A=l2.count('A')+l2.count('a')
        print(f'{l2[0]} has total Present: {P} and total Abscent: {A}')
def main_menu():
    s="""1.Take Attandance\n2.Count Attandance"""
    print(s)
    ch=int(input('Enter the choice 1 or 2: '))
    if ch==1:
        take_attandance()
    else:
        count_attandance()
main_menu()
