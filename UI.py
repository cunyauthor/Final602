from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.base import runTouchApp
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.listview import ListView
import numpy as np
layout = FloatLayout()

##################################################################
# Change your info here
MyPath="/Users/fionaho/Desktop/Final Project 602/plotly/"
API_ID=""
API_PW=""
##################################################################

DiceCount=0
Wage=[]
State=[]
Occupation=[]
Sampling=[]

DiceCountList=[]
SelectedOccupations=[]
SelectedOccupations2=[]

import sys
sys.path.append(MyPath)

import plotly 
plotly.tools.set_credentials_file(username=API_ID, api_key=API_PW)
plotly.tools.set_config_file(world_readable=True,sharing='public')

    
def AddOccupations(instance):
    if mainbutton2.text not in SelectedOccupations and mainbutton2.text<>"Occupation":
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
             listview2.item_strings.append('No Occupation is selected!')
     
     box.add_widget(listview2)
     popup = Popup(content=box, auto_dismiss=False,title='Selected Occupations')

    # bind the on_press event of the button to the dismiss function
     content.bind(on_press=popup.dismiss)

    # open the popup
     popup.open()
     return x

def MyExit(instance):
    sys.exit()
       
def MyConfig(instance):
    return x
    
# Function to call Dice.com web service to ger the 1st 50 jobs 
def PlotChart1():
    
    global Sampling
    global DiceCount
    
    URL="http://service.dice.com/api/rest/jobsearch/v1/simple.json?text=%s&state=%s" %(mainbutton2.text.replace(' ','+'),mainbutton1.text)
    
    import urllib, json
    response = urllib.urlopen(URL)
    data = json.loads(response.read())
    
    Sampling=[]
    DiceCount=0
    DiceCount=int(data['count']) 
    
    if(DiceCount>0):
        for i in data['resultItemList']:
            Sampling.append(i['jobTitle'] + '|' + i['company']+ "|" + i['location'])
    
    return ''

# Function to call Dice.com web service to get the job count 
def PlotChart2():
    
    import urllib, json
    
    global SelectedOccupations
    global DiceCountList
    global API_ID
    global API_PW
    
    DiceCountList=[]
   
    for i in range(0,len(SelectedOccupations)):
        URL="http://service.dice.com/api/rest/jobsearch/v1/simple.json?text=%s&state=%s" %(SelectedOccupations[i].replace(' ','+'),mainbutton1.text)
        response = urllib.urlopen(URL)
        data = json.loads(response.read())
        DiceCountList.append(int(data['count'])) 
    
    for i in range(0,len(SelectedOccupations)):
        print DiceCountList[i]
        print SelectedOccupations[i]
        
    
    import plotly.plotly as py
    import plotly.graph_objs as go

    trace0 = go.Bar(
    x=SelectedOccupations,
    y=DiceCountList,
    #text=['27% market share', '24% market share', '19% market share'],
    marker=dict(
        color='rgb(158,202,225)',
        line=dict(
            color='rgb(8,48,107)',
            width=1.5,
        )
    ),
    opacity=0.6
    )

    data = [trace0]
    layout = go.Layout(
        title='Job Count of ' + SelectedOccupations[0] + ' in '+ mainbutton1.text
    )

    fig = go.Figure(data=data, layout=layout)
    py.plot(fig, filename='Report-2')
    
    
def PlotChart3():
    
    global API_ID
    global API_PW
    
    global SelectedOccupations
    global Wage
    
    Wage=[]
   
    for i in range(0,len(SelectedOccupations)):
        SearchWage(SelectedOccupations[i],0)
       
    for i in range(0,len(SelectedOccupations)):
        print Wage[i]
        print SelectedOccupations[i]
               
    import plotly.plotly as py
    import plotly.graph_objs as go

    trace0 = go.Bar(
    x=SelectedOccupations,
    y=Wage,
    #text=['27% market share', '24% market share', '19% market share'],
    marker=dict(
        color='rgb(158,202,225)',
        line=dict(
            color='rgb(8,48,107)',
            width=1.5,
        )
    ),
    opacity=0.6
    )

    data = [trace0]
    layout = go.Layout(
        title='Comparing Wages of ' + SelectedOccupations[0] + ' in ' + mainbutton1.text
        )

    fig = go.Figure(data=data, layout=layout)
    py.plot(fig, filename='Report-3')
    
def PlotChart4():
    
    
    global SelectedOccupations
    global State
    global Wage
    global SelectedOCC
    global API_ID
    global API_PW
    
    Wage=[]
    State=[]
    SelectedOCC=[]
 
    
    for i in range(0,len(SelectedOccupations)):
        SearchWage(SelectedOccupations[i],1)
        
    for i in range(0,len(SelectedOccupations)):
        for j in range(0, len(SelectedOCC)):
            if(SelectedOccupations[i]==SelectedOCC[j]):
                print State[j]
                print Wage[j]
                print SelectedOCC[j]
                    
    import plotly.plotly as py
    import plotly.graph_objs as go

    trace0 = go.Bar(
    x=State,
    y=Wage,
    #text=['27% market share', '24% market share', '19% market share'],
    marker=dict(
        color='rgb(158,202,225)',
        line=dict(
            color='rgb(8,48,107)',
            width=1.5,
        )
    ),
    opacity=0.6
    )

    data = [trace0]
    layout = go.Layout(
        title='Comparing Wages of ' + SelectedOccupations[0] +' in each state',
        )

    fig = go.Figure(data=data, layout=layout)
    py.plot(fig, filename='Report-4')
                    
    
def PlotChart5():
    
    
    global SelectedOccupations
    global SelectedOccupations2
    global Wage
    global API_ID
    global API_PW
    
    Wage=[]
    
   
    SearchWage(SelectedOccupations[0],2)
       
    
    import plotly.plotly as py
    import plotly.graph_objs as go


    trace0 = go.Bar(
    x=SelectedOccupations2,
    y=Wage,
    #text=['27% market share', '24% market share', '19% market share'],
    marker=dict(
        color='rgb(158,202,225)',
        line=dict(
            color='rgb(8,48,107)',
            width=1.5,
        )
    ),
    opacity=0.6
    )


    data = [trace0]
    layout = go.Layout(
        title='Comparing Wages of ' + SelectedOccupations[0] + ' Between Year ' + mainbutton3.text + ' and ' + mainbutton4.text
        )


    fig = go.Figure(data=data, layout=layout)
    py.plot(fig, filename='Report-5')

    
    
def PlotChart6():
    
    
    global SelectedOccupations
    global SelectedOccupations2
    global Wage
    global API_ID
    global API_PW
    
    Wage=[]
    Diff=[]
   
    SearchWage(SelectedOccupations[0],3)
       
    for i in range(0,len(SelectedOccupations2)-1):
         Diff.append((float(Wage[i+1])-float(Wage[i]))/float(Wage[i+1]))
   
    from numpy import array
    
    NewDiff = array( Diff )
    
    mu = NewDiff.mean()    
     
    sigma = NewDiff.std()
    
    s = np.random.normal(mu, sigma, 1)
    
    NewWage= Wage[len(Wage)-1]+(Wage[len(Wage)-1]*s[0])
     
    Wage.append(NewWage)   
    SelectedOccupations2.append("2016")
    
    import plotly.plotly as py
    import plotly.graph_objs as go


    trace0 = go.Bar(
    x=SelectedOccupations2,
    y=Wage,
    #text=['27% market share', '24% market share', '19% market share'],
    marker=dict(
        color='rgb(158,202,225)',
        line=dict(
            color='rgb(8,48,107)',
            width=1.5,
        )
    ),
    opacity=0.6
    )


    data = [trace0]
    layout = go.Layout(
        title='Comparing Wages of ' + SelectedOccupations[0] + ' Between Year 2005 and 2016 (Forecast)'
        )


    fig = go.Figure(data=data, layout=layout)
    py.plot(fig, filename='Report-6')

    
     
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
           sql = "SELECT DISTINCT OCC_TITLE FROM WageByState where OCC_GROUP=%s and MyYear=%s order by OCC_TITLE"
           cursor.execute(sql,("detailed","2015"))
           
           Temp=cursor.fetchall()
           
           for row in Temp:
               Occupation.append(row["OCC_TITLE"])
               
       connection.commit()   
           
   finally:
        connection.close()
        
def SearchWage(Occupations,Report):
    
   global State
   global Wage
   import pymysql.cursors
   global SelectedOccupations
   global SelectedOccupations2
   global SelectedOCC

    # Connect to the database
   connection = pymysql.connect(host='localhost',user='user1',password='Password1234',db='sys',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
    
   try:
       
       with connection.cursor() as cursor:
           if(Report==0):
               sql = "SELECT a_mean FROM WageByState where OCC_TITLE=%s and STATE=%s and MyYear=%s"
               cursor.execute(sql,(Occupations,mainbutton1.text.strip(),mainbutton3.text.strip()))
               Temp=cursor.fetchall()
               for row in Temp:
                   Wage.append(int(row["a_mean"].replace(",","")))
           if(Report==1):
               sql = "SELECT a_mean,STATE FROM WageByState where OCC_TITLE=%s and MyYear=%s order by a_mean"
               cursor.execute(sql,(Occupations,mainbutton3.text.strip()))
               Temp=cursor.fetchall()
               for row in Temp:
                   Wage.append(int(row["a_mean"].replace(",","")))
                   print row["STATE"]
                   State.append(row["STATE"])
                   SelectedOCC.append(Occupations)
                   
           if(Report==2):
               sql = "SELECT a_mean,MyYear FROM WageByState where OCC_TITLE=%s and MyYear >=%s AND MyYear <=%s and State=%s order by MyYear"
               print sql
               cursor.execute(sql,(Occupations,mainbutton3.text.strip(),mainbutton4.text.strip(),mainbutton1.text.strip()))
               Temp=cursor.fetchall()
               SelectedOccupations2=[]
               for row in Temp:
                   Wage.append(int(row["a_mean"].replace(",","")))
                   SelectedOccupations2.append(row["MyYear"])
                   
           if(Report==3):
               sql = "SELECT a_mean,MyYear FROM WageByState where OCC_TITLE=%s and State=%s order by MyYear"
               print sql
               cursor.execute(sql,(Occupations,mainbutton1.text.strip()))
               Temp=cursor.fetchall()
               SelectedOccupations2=[]
               for row in Temp:
                   Wage.append(int(row["a_mean"].replace(",","")))
                   SelectedOccupations2.append(row["MyYear"])
           
                  
       connection.commit()   
           
   finally:
        connection.close()
    

def MyMsg(msg):
    
    content = Button(text='Close',size_hint=(0.1, None), pos=(0, 0))
    box = BoxLayout()
    box.add_widget(content)
    popup = Popup(content=box, auto_dismiss=False,title=msg)
    content.bind(on_press=popup.dismiss)
    popup.open()
    
def MyMsgWList(msg,L):
    
    content = Button(text='Close',size_hint=(0.1, None), pos=(0, 0))
    box = BoxLayout()
    box.add_widget(content)
    box.add_widget(L)
    popup = Popup(content=box, auto_dismiss=False,title=msg)
    content.bind(on_press=popup.dismiss)
    popup.open()
     
    
def MyShow(instance):
    
     global Sampling
     global DiceCount
     MyTitle= ''.join([mainbutton1.text, '---', mainbutton2.text, '---', mainbutton3.text, '---',mainbutton4.text, '---',mainbutton5.text])
       
     if(mainbutton5.text<>"Report Type"):
   
          
         listview1=ListView(pos=(0, 30),halign='left')
    
         
         if(mainbutton5.text=="Listing 1st 50 Job Records from Dice.com based on Selected Occupation and State"):
             
             if(btnF4.text<>"0" and mainbutton1.text<>"State"):
                 
                 MyTitle= ''.join([mainbutton1.text, '---', mainbutton2.text, '---',mainbutton5.text])
       
                 PlotChart1() 
                 
                 for i in range(0,len(Sampling)):
                     listview1.item_strings.append(Sampling[i])
                 if(DiceCount==0):
                     listview1.item_strings.append('Record not found!')
                 MyMsgWList(MyTitle,listview1)
                  
             else:    
                 MyMsg("Please select the State and Press the + button after selected the Occupation")
    
         if(mainbutton5.text=="Plotting the Job Count based on selected Occupation(s) and State"):
             
             if(btnF4.text<>"0" and mainbutton1.text<>"State"):
                 PlotChart2() 
                 
             else:
                 MyMsg("Please select the State and Press the + button after selected the Occupation")
             
         if(mainbutton5.text=="Comparing Wages by selected occupation(s) and state"):
             
             if(btnF4.text<>"0" and mainbutton1.text<>"State" and mainbutton3.text<>"Year From"):
                 PlotChart3() 
             
             else:
                 MyMsg("Please select the State, From Year and Press the + button after selected the Occupation")
         
         if(mainbutton5.text=="Comparing Wages of an occupation by state"):
             if(btnF4.text<>"0" and mainbutton3.text<>"Year From"):
                 PlotChart4() 
             else:
                 MyMsg("Please select the Year From and Press the + button after selected the Occupation")
                 
         if(mainbutton5.text=="Comparing Wages with selected occupation and year"):
             if(btnF4.text<>"0" and mainbutton3.text<>"Year From" and mainbutton4.text<>"Year To" and mainbutton1.text<>"State"):
                 PlotChart5()
             else:
                 MyMsg("Please select the State, Year From , Year To and Press the + button after selected the Occupation")
         
         if(mainbutton5.text=="Comparing Wages with selected occupation and forcast next year"):
             if(btnF4.text<>"0" and mainbutton1.text<>"State"):
                 PlotChart6()
             else:
                 MyMsg("Please select the State and Press the + button after selected the Occupation")
                  
                 
                 
     else:
            MyMsg("Please Select the Report Type")
             
# State
dropdown1 = DropDown()
dropdown2 = DropDown()
dropdown3 = DropDown()
dropdown4 = DropDown()
dropdown5 = DropDown()

###################################################################

btnF1 = Button(text='Show Wage Data Analysis', size_hint=(0.8, None), pos=(0, 0))
btnF1.bind(on_press=MyShow)

###################################################################

btnF2 = Button(text='+', size_hint=(0.05, 0.05), pos=(650, 370))
btnF2.bind(on_press=AddOccupations)

###################################################################

btnF3 = Button(text='-', size_hint=(0.05, 0.05), pos=(650, 300))
btnF3.bind(on_press=RemoveOccupations)

btnF4 = Button(text='0', size_hint=(0.05, 0.05), pos=(650, 335))
btnF4.bind(on_press=ListOccupations)

btnF5 = Button(text='Exit', size_hint=(0.05, 0.05), pos=(760, 570))
btnF5.bind(on_press=MyExit)

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
stack5.append(Button(text='Listing 1st 50 Job Records from Dice.com based on Selected Occupation and State', size_hint_y=None, height=20)) 
stack5.append(Button(text='Plotting the Job Count based on selected Occupation(s) and State', size_hint_y=None, height=20)) 
stack5.append(Button(text='Comparing Wages by selected occupation(s) and state', size_hint_y=None, height=20)) 
stack5.append(Button(text='Comparing Wages of an occupation by state', size_hint_y=None, height=20)) 
stack5.append(Button(text='Comparing Wages with selected occupation and year', size_hint_y=None, height=20)) 
stack5.append(Button(text='Comparing Wages with selected occupation and forcast next year', size_hint_y=None, height=20)) 

for x in range(0, 6): 
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

for x in range(0, 6): 
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
layout.add_widget(btnF5)


runTouchApp(layout)

