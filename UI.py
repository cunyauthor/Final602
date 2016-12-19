from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.base import runTouchApp
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.listview import ListView

layout = FloatLayout()
State=[]
Occupation=[]
MyPath="/Users/fionaho/Desktop/Final Project 602/"
Sampling=[]
DiceCount=0
SelectedOccupations=[]

def AddOccupations(instance):
    if mainbutton2.text not in SelectedOccupations:
        SelectedOccupations.append(mainbutton2.text)
        btnF4.text=str(len(SelectedOccupations))
    return x
    
def RemoveOccupations(instance):
    if mainbutton2.text in SelectedOccupations:
        SelectedOccupations.remove(mainbutton2.text)
        btnF4.text=str(len(SelectedOccupations))
    return x

def ListOccupations(instance):
    # create content and add to the popup
     global SelectedOccupations
     content = Button(text='Close',size_hint=(0.1, None), pos=(0, 0))
     
     box = BoxLayout()
     box.add_widget(content)
     
     listview2=ListView(pos=(0, 30),halign='left')

     
     
     for i in range(0,len(SelectedOccupations)):
             listview2.item_strings.append(SelectedOccupations[i])
     if(len(SelectedOccupations)==0):
             listview2.item_strings.append('No Occupation is selected not!')
     
     box.add_widget(listview2)
     popup = Popup(content=box, auto_dismiss=False,title='Selected Occupations')

    # bind the on_press event of the button to the dismiss function
     content.bind(on_press=popup.dismiss)

    # open the popup
     popup.open()
     return x
    
    
def PlotChart1():
    
    global Sampling
    global DiceCount
    URL="http://service.dice.com/api/rest/jobsearch/v1/simple.json?text=%s&state=%s" %(mainbutton2.text.replace(' ','+'),mainbutton1.text)
    
    print URL
    
    import urllib, json
    response = urllib.urlopen(URL)
    data = json.loads(response.read())
    #print data
    
    Sampling=[]
    DiceCount=0
    DiceCount=int(data['count']) 
    
    if(DiceCount>0):
        for i in data['resultItemList']:
            Sampling.append(i['jobTitle'] + '|' + i['company']+ "|" + i['location'])
    
    
   
    
    return ''
   
def PlotChart2():
    
    
    import urllib, json
    global SelectedOccupations
    DiceCountList=[]
   
    for i in range(0,len(SelectedOccupations)):
        URL="http://service.dice.com/api/rest/jobsearch/v1/simple.json?text=%s&state=%s" %(SelectedOccupations[i].replace(' ','+'),mainbutton1.text)
        response = urllib.urlopen(URL)
        data = json.loads(response.read())
        DiceCountList.append(int(data['count'])) 
    
    for i in range(0,len(SelectedOccupations)):
        print DiceCountList[i]
        print SelectedOccupations[i]
        
    import glob
    import os
    for f in glob.glob("*.png"): # find all csv files
        if not f.endswith("0.png"):
            os.remove(f)  # if file name ends in 0.csv, delete it
    
    
    import numpy as np
    import matplotlib.pyplot as plt
    plt.rcParams['interactive'] =False
    
    fig = plt.figure(figsize=(10,10))
    index = np.arange(len(DiceCountList))
    bar_width = 1.0
    plt.bar(index, DiceCountList, bar_width,  color="green")
    plt.xticks(index + bar_width / 2, SelectedOccupations,rotation=90) # labels get centered
    
    
    
    
    import time
    ts = time.time()
    import datetime
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    
    st1 = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S')
    fig.savefig(MyPath+st1+'.png')
    
    plt.close(1) 
    
    return MyPath+st1+'.png'
    
def PlotChart3():
    
    
    import glob
    import os
    for f in glob.glob("*.png"): # find all csv files
        if not f.endswith("0.png"):
            os.remove(f)  # if file name ends in 0.csv, delete it
    
    from pylab import figure, axes, pie, title, show,close
    import matplotlib.pyplot as plt
    
    plt.rcParams['interactive'] =False
    
    # Make a square figure and axes
    f=figure(1, figsize=(6, 6))
    ax = axes([0.1, 0.1, 0.8, 0.8])
    
    labels = 'I', 'J', 'K', 'L'
    fracs = [15, 30, 45, 10]
    
    explode = (0, 0.05, 0, 0)
    pie(fracs, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True)
    
    import time
    ts = time.time()
    import datetime
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    
    st1 = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S')
    title(st, bbox={'facecolor': '0.8', 'pad': 5})
    f.savefig(MyPath+st1+'.png')
    
    plt.close(1) 
    
    return MyPath+st1+'.png'
    
def PlotChart4():
    
    
    import glob
    import os
    for f in glob.glob("*.png"): # find all csv files
        if not f.endswith("0.png"):
            os.remove(f)  # if file name ends in 0.csv, delete it
    
    from pylab import figure, axes, pie, title, show,close
    import matplotlib.pyplot as plt
    
    plt.rcParams['interactive'] =False
    
    # Make a square figure and axes
    f=figure(1, figsize=(6, 6))
    ax = axes([0.1, 0.1, 0.8, 0.8])
    
    labels = 'M', 'N', 'O', 'P'
    fracs = [15, 30, 45, 10]
    
    explode = (0, 0.05, 0, 0)
    pie(fracs, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True)
    
    import time
    ts = time.time()
    import datetime
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    
    st1 = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S')
    title(st, bbox={'facecolor': '0.8', 'pad': 5})
    f.savefig(MyPath+st1+'.png')
    
    plt.close(1) 
    
    return MyPath+st1+'.png'
    
def PrepareDB():
    
   global State
   import pymysql.cursors

    # Connect to the database
   connection = pymysql.connect(host='localhost',user='user1',password='Password1234',db='sys',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
    
   try:
       
       with connection.cursor() as cursor:
           sql = "SELECT * from State"
           cursor.execute(sql)
           Temp=cursor.fetchall()
           
           for row in Temp:
               State.append(row["State"])
               
       connection.commit()   
       
       with connection.cursor() as cursor:
           sql = "SELECT DISTINCT OCC_TITLE FROM WageByState order by OCC_TITLE"
           cursor.execute(sql)
           Temp=cursor.fetchall()
           
           for row in Temp:
               Occupation.append(row["OCC_TITLE"])
               
       connection.commit()   
           
   finally:
        connection.close()
    


def HelloWorld(instance):
     global Sampling
     global DiceCount
     #print('The button <%s> is being pressed' % instance.text)
     print('%s' % mainbutton1.text)
     print('%s' % mainbutton2.text)
     print('%s' % mainbutton3.text)
     print('%s' % mainbutton4.text)
     print('%s' % mainbutton5.text)
     
     MyTitle= ''.join([mainbutton1.text, '---', mainbutton2.text, '---', mainbutton3.text, '---',mainbutton4.text, '---',mainbutton5.text])
     
     
     ###################################################################
     image1=Image()     
     image1.size_hint=(0.9,0.9)
     image1.pos=(500, 0)
     
     listview1=ListView(pos=(0, 30),halign='left')

     
     if(mainbutton5.text=="Sampling 1st 50 Job Records from Dice.com based on Selected Occupation"):
         image1.source=PlotChart1() 
         for i in range(0,len(Sampling)):
             listview1.item_strings.append(Sampling[i])
         if(DiceCount==0):
             listview1.item_strings.append('Record not found!')
     if(mainbutton5.text=="Plotting the Job Count based on selected Occupations"):
         image1.source=PlotChart2() 
         
         
         
     if(mainbutton5.text=="Report 3"):
         image1.source=PlotChart3() 
     if(mainbutton5.text=="Report 4"):
         image1.source=PlotChart4() 
         
         
     
     
     
    # create content and add to the popup
     content = Button(text='Close',size_hint=(0.1, None), pos=(0, 0))
     
     box = BoxLayout()
     box.add_widget(content)
     
     if(mainbutton5.text=="Sampling 1st 50 Job Records from Dice.com based on Selected Occupation"):
         box.add_widget(listview1)
     if(mainbutton5.text=="Plotting the Job Count based on selected Occupations"):
         box.add_widget(image1)
     
     popup = Popup(content=box, auto_dismiss=False,title=MyTitle)

    # bind the on_press event of the button to the dismiss function
     content.bind(on_press=popup.dismiss)

    # open the popup
     popup.open()
        
        
    
     

    

# State
dropdown1 = DropDown()
dropdown2 = DropDown()
dropdown3 = DropDown()
dropdown4 = DropDown()
dropdown5 = DropDown()


###################################################################
label1=Label()
label1.text="Wage Data Analysis"
label1.font_size='30sp'
label1.size_hint=(None, None)
label1.pos=(100, 500)

###################################################################

btnF1 = Button(text='Show', size_hint=(0.8, None), pos=(0, 0))
btnF1.bind(on_press=HelloWorld)

###################################################################

btnF2 = Button(text='+', size_hint=(0.05, 0.05), pos=(650, 370))
btnF2.bind(on_press=AddOccupations)

###################################################################

btnF3 = Button(text='-', size_hint=(0.05, 0.05), pos=(650, 300))
btnF3.bind(on_press=RemoveOccupations)

btnF4 = Button(text='...', size_hint=(0.05, 0.05), pos=(650, 335))
btnF4.bind(on_press=ListOccupations)


###################################################################
# State 

PrepareDB()

stack1 = []

global State

for x in range(0, 50):
    stack1.append(Button(text=State[x], size_hint_y=None, height=20))

for x in range(0, 50):
    stack1[x].bind(on_release=lambda btn: dropdown1.select(btn.text))

###################################################################
# Job 
stack2 = []

global Occupation
for x in range(0, len(Occupation)):
    stack2.append(Button(text=Occupation[x], size_hint_y=None, height=20)) 

for x in range(0, len(Occupation)): 
    stack2[x].bind(on_release=lambda btn: dropdown2.select(btn.text))


###################################################################
# From Year 
stack3 = []

for x in range(2005, 2016): 
    stack3.append(Button(text=str(x), size_hint_y=None, height=20)) 
    
for x in range(0, 11): 
    stack3[x].bind(on_release=lambda btn: dropdown3.select(btn.text))
    
###################################################################
# To Year 
stack4 = []

for x in range(2005, 2016): 
    stack4.append(Button(text=str(x), size_hint_y=None, height=20)) 
    
for x in range(0, 11): 
    stack4[x].bind(on_release=lambda btn: dropdown4.select(btn.text))
    
###################################################################
# Report Type 
stack5 = []


stack5.append(Button(text='Sampling 1st 50 Job Records from Dice.com based on Selected Occupation', size_hint_y=None, height=20)) 
stack5.append(Button(text='Plotting the Job Count based on selected Occupations', size_hint_y=None, height=20)) 
stack5.append(Button(text='Report 3', size_hint_y=None, height=20)) 
stack5.append(Button(text='Report 4', size_hint_y=None, height=20)) 
    
for x in range(0, 4): 
    stack5[x].bind(on_release=lambda btn: dropdown5.select(btn.text))
    
###################################################################


for x in range(0, 50): 
    dropdown1.add_widget(stack1[x])
    
for x in range(0, len(Occupation)): 
    dropdown2.add_widget(stack2[x])
    
for x in range(0, 11): 
    dropdown3.add_widget(stack3[x])
    
for x in range(0, 11): 
    dropdown4.add_widget(stack4[x])

for x in range(0, 4): 
    dropdown5.add_widget(stack5[x])


# create a big main button
mainbutton1 = Button(text='State', size_hint=(0.8, None),pos=(0, 400))
mainbutton2 = Button(text='Occupation', size_hint=(0.8, None),pos=(0, 300))
mainbutton3 = Button(text='Year From', size_hint=(0.8, None),pos=(0, 200))
mainbutton4 = Button(text='Year To', size_hint=(0.8, None),pos=(0, 100))
mainbutton5 = Button(text='Report Type', size_hint=(0.8, None),pos=(0, 500))


# show the dropdown menu when the main button is released
# note: all the bind() calls pass the instance of the caller (here, the
# mainbutton instance) as the first argument of the callback (here,
# dropdown.open.).
mainbutton1.bind(on_release=dropdown1.open)
mainbutton2.bind(on_release=dropdown2.open)
mainbutton3.bind(on_release=dropdown3.open)
mainbutton4.bind(on_release=dropdown4.open)
mainbutton5.bind(on_release=dropdown5.open)
# one last thing, listen for the selection in the dropdown list and
# assign the data to the button text.
dropdown1.bind(on_select=lambda instance, x: setattr(mainbutton1, 'text', x))
dropdown2.bind(on_select=lambda instance, x: setattr(mainbutton2, 'text', x))
dropdown3.bind(on_select=lambda instance, x: setattr(mainbutton3, 'text', x))
dropdown4.bind(on_select=lambda instance, x: setattr(mainbutton4, 'text', x))
dropdown5.bind(on_select=lambda instance, x: setattr(mainbutton5, 'text', x))

layout.add_widget(mainbutton1)
layout.add_widget(mainbutton2)
layout.add_widget(mainbutton3)
layout.add_widget(mainbutton4)
layout.add_widget(mainbutton5)
layout.add_widget(btnF1)
layout.add_widget(btnF2)
layout.add_widget(btnF3)
layout.add_widget(btnF4)
#layout.add_widget(label1)


runTouchApp(layout)

