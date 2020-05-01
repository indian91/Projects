import matplotlib.pyplot as plt
import pandas as pd
import requests
import bs4
import os
import random
page=requests.get('https://api.covid19india.org/csv/latest/state_wise.csv')
f=open('update.csv','wb')
f.write(page.content)
f.close()
df=pd.read_csv('update.csv')
def Confirmed(df):
    df = df.sort_values('Confirmed',axis=0 ,ascending=False)
    choices = [ '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a','b', 'c', 'd', 'e']
    def make_color():
        ch = [ random.choice(choices) for i in range(6)]
        return "#"+"".join(ch)
    colors = []
    while len(colors) != 20:
        color = make_color()
        if color in colors:
            continue
        colors.append(color)
    fig= plt.figure()
    ax = fig.add_axes([0.2,0.2,0.6,0.6])
    ax.bar(df['State_code'][1:21], df['Confirmed'][1:21],color=colors)
    ax.set_xticklabels(df['State_code'][1:21],rotation=90,size=10)
    #ax.set_ylim([0, 25000])
    #ax.set_yticklabels(range(0,10000, 500))
    ax.set_yticks(range(0, 10000, 1000))
    ax.set_title("Corona Cases Till Now", fontsize=25, color='red', pad=20)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.set_xlabel('States')
    ax.set_ylabel("Total Cases")
    
    c = 1
    for patch,color,lb in zip(ax.patches, colors, ax.get_xticklabels()):
        x  = patch.get_x() + 0.2
        h = patch.get_height()
        y=h+1000
        if c == 1:
            text = df.iloc[1,1]
        else:
            text = h
        c += 1
        ax.text(x, y, text, fontsize=10, color=color, rotation=90)
        lb.set_color(color)
    plt.show()
def Recovered(df):
    df = df.sort_values('Recovered',axis=0 ,ascending=False)
    choices = [ '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a','b', 'c', 'd', 'e']
    def make_color():
        ch = [ random.choice(choices) for i in range(6)]
        return "#"+"".join(ch)
    colors = []
    while len(colors) != 20:
        color = make_color()
        if color in colors:
            continue
        colors.append(color)
    fig= plt.figure()
    ax = fig.add_axes([0.2,0.2,0.6,0.6])
    ax.bar(df['State_code'][1:21], df['Recovered'][1:21],color=colors)
    ax.set_xticklabels(df['State_code'][1:21],rotation=90,size=10)
    #ax.set_ylim([0, 25000])
    #ax.set_yticklabels(range(0,10000, 500))
    ax.set_yticks(range(0, 5000, 500))
    ax.set_title("Corona Recovered Till Now", fontsize=25, color='red', pad=20)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.set_xlabel('States')
    ax.set_ylabel("Total Recovered")
    
    c = 1
    for patch,color,lb in zip(ax.patches, colors, ax.get_xticklabels()):
        x  = patch.get_x() + 0.2
        h = patch.get_height()
        y=h+500
        if c == 1:
            text = df.iloc[1,2]
        else:
            text = h
        c += 1
        ax.text(x, y, text, fontsize=10, color=color, rotation=90)
        lb.set_color(color)
    plt.show()
def Deaths(df):
    df = df.sort_values('Deaths',axis=0 ,ascending=False)
    choices = [ '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a','b', 'c', 'd', 'e']
    def make_color():
        ch = [ random.choice(choices) for i in range(6)]
        return "#"+"".join(ch)
    colors = []
    while len(colors) != 20:
        color = make_color()
        if color in colors:
            continue
        colors.append(color)
    fig= plt.figure()
    ax = fig.add_axes([0.2,0.2,0.6,0.6])
    ax.bar(df['State_code'][1:21], df['Deaths'][1:21],color=colors)
    ax.set_xticklabels(df['State_code'][1:21],rotation=90,size=10)
    #ax.set_ylim([0, 25000])
    #ax.set_yticklabels(range(0,10000, 500))
    ax.set_yticks(range(0, 500, 50))
    ax.set_title("Corona Deaths Till Now", fontsize=25, color='red', pad=20)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.set_xlabel('States')
    ax.set_ylabel("Total Deaths")
    
    c = 1
    for patch,color,lb in zip(ax.patches, colors, ax.get_xticklabels()):
        x  = patch.get_x() + 0.2
        h = patch.get_height()
        y=h+50
        if c == 1:
            text = df.iloc[1,3]
        else:
            text = h
        c += 1
        ax.text(x, y, text, fontsize=10, color=color, rotation=90)
        lb.set_color(color)
    plt.show()
def Active(df):
    df = df.sort_values('Active',axis=0 ,ascending=False)
    choices = [ '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a','b', 'c', 'd', 'e']
    def make_color():
        ch = [ random.choice(choices) for i in range(6)]
        return "#"+"".join(ch)
    colors = []
    while len(colors) != 20:
        color = make_color()
        if color in colors:
            continue
        colors.append(color)
    fig= plt.figure()
    ax = fig.add_axes([0.2,0.2,0.6,0.6])
    ax.bar(df['State_code'][1:21], df['Active'][1:21],color=colors)
    ax.set_xticklabels(df['State_code'][1:21],rotation=90,size=10)
    #ax.set_ylim([0, 25000])
    #ax.set_yticklabels(range(0,10000, 500))
    ax.set_yticks(range(0, 10000, 1000))
    ax.set_title("Active Cases Till Now", fontsize=25, color='red', pad=20)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.set_xlabel('States')
    ax.set_ylabel("Active Cases")
    
    c = 1
    for patch,color,lb in zip(ax.patches, colors, ax.get_xticklabels()):
        x  = patch.get_x() + 0.2
        h = patch.get_height()
        y=h+750
        if c == 1:
            text = df.iloc[1,4]
        else:
            text = h
        c += 1
        ax.text(x, y, text, fontsize=10, color=color, rotation=90)
        lb.set_color(color)
    plt.show()
    
def  HighlyRecoveredStates(df):
    df=df.sort_values('Confirmed',axis=0,ascending=False)
    l2=[]
    for i in range(1,21):
        l2.append(round(((df['Recovered'][i]/df['Confirmed'][i])*100),2))
    df1=pd.DataFrame(l2,columns=list('A'))
    choices = [ '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a','b', 'c', 'd', 'e']
    def make_color():
        ch = [ random.choice(choices) for i in range(6)]
        return "#"+"".join(ch)
    colors = []
    while len(colors) != 20:
        color = make_color()
        if color in colors:
            continue
        colors.append(color)
    fig= plt.figure()
    ax = fig.add_axes([0.2,0.2,0.6,0.6])
    ax.bar(df['State_code'][1:21], df1['A'],color=colors)
    ax.set_xticklabels(df['State_code'][1:21],rotation=90,size=10)
    #ax.set_ylim([0, 25000])
    #ax.set_yticklabels(range(0,10000, 500))
    ax.set_yticks(range(0, 100, 10))
    ax.set_title("Recovered Percentage", fontsize=25, color='red', pad=20)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.set_xlabel('States')
    ax.set_ylabel("Highly Recovered States")
    
    c = 1
    for patch,color,lb in zip(ax.patches, colors, ax.get_xticklabels()):
        x  = patch.get_x() + 0.2
        h = patch.get_height()
        y=h+10
        text = h
        c += 1
        ax.text(x, y, text, fontsize=10, color=color, rotation=90)
        lb.set_color(color)
    plt.show()
    
def  DeathPercentage(df):
    df=df.sort_values('Confirmed',axis=0,ascending=False)
    l2=[]
    for i in range(1,21):
        l2.append(round(((df['Deaths'][i]/df['Confirmed'][i])*100),2))
    df1=pd.DataFrame(l2,columns=list('A'))
    choices = [ '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a','b', 'c', 'd', 'e']
    def make_color():
        ch = [ random.choice(choices) for i in range(6)]
        return "#"+"".join(ch)
    colors = []
    while len(colors) != 20:
        color = make_color()
        if color in colors:
            continue
        colors.append(color)
    fig= plt.figure()
    ax = fig.add_axes([0.2,0.2,0.6,0.6])
    ax.bar(df['State_code'][1:21], df1['A'],color=colors)
    ax.set_xticklabels(df['State_code'][1:21],rotation=90,size=10)
    #ax.set_ylim([0, 25000])
    #ax.set_yticklabels(range(0,10000, 500))
    ax.set_yticks(range(0, 25, 5))
    ax.set_title("Death Percentage of States", fontsize=25, color='red', pad=20)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.set_xlabel('States')
    ax.set_ylabel("Death %")
    
    c = 1
    for patch,color,lb in zip(ax.patches, colors, ax.get_xticklabels()):
        x  = patch.get_x() + 0.2
        h = patch.get_height()
        y=h+2.5
        text = h
        c += 1
        ax.text(x, y, text, fontsize=10, color=color, rotation=90)
        lb.set_color(color)
    plt.show()
def main_menu():
    while True:
        os.system('cls')
        print("\n\n\n")
        s="""1.Total Confirmed Cases\n2.Total Recovred Cases\n3.Total Deaths\n4.Active Patients\n5.HighlyRecoveredStates\n6.DeathPercentage"""
        print(s)
        ch=int(input('Choose Option from above'))
        if ch==1:
            Confirmed(df)
        elif ch==2:
            Recovered(df)
        elif ch==3:
            Deaths(df)
        elif ch==4:
            Active(df)
        elif ch==5:
            HighlyRecoveredStates(df)
        elif ch==6:
            DeathPercentage(df)
        else:
            print('Please Input Correct Option')
plt.rcParams['figure.figsize']  = 12, 6
plt.rcParams['xtick.major.pad'] = 5
plt.rcParams['xtick.major.pad'] = 5
plt.rcParams['ytick.major.pad'] = 5
plt.rcParams['ytick.major.pad'] = 5
plt.rcParams['axes.labelcolor'] = 'red'
plt.rcParams['axes.labelsize']  = 20
plt.rcParams['xtick.labelsize'] = 15
plt.rcParams['ytick.labelsize'] = 15
plt.rcParams['legend.fontsize'] = 20       
main_menu()
