from tkinter import *

master = Tk()
var = IntVar()
var.set(1)
namelist = []
BMIList =[]


def conclusion():# Function that allows User to store new person or print details of all old persons
    global nm
    name = nm.get()
    BMIList.append(BMI)
    namelist.append(name)
    store.destroy()
    global final
    final = Tk()
    Label(final,text='How do you wish to proceed ').grid(row=0, column=3)
    Button(final, text="Store New Person Data", command=Fullbody).grid(row=1, column=3)
    Label(final, text='OR').grid(row=2, column=3)
    Button(final, text="Print Data for all persons", command=Print).grid(row=3, column=3)


def Print():# Function that prints the people stored and their BMI values
    global BMIList
    for index in range(len(BMIList)):
        print('Name :' + namelist[index] + 'BMI' + BMIList[index])
    final.destroy()


def database(): # Function that Stores Name and Display BMI values
    global store
    store = Tk()
    store.title('Whats your name?')
    if BMI < 18.5:
        Label(store, text='YOU ARE UNDERWEIGHT ').grid(row=0, column=3)
    elif BMI>18.5 and BMI<24.9:
        Label(store, text='YOU ARE NORMAL ').grid(row=0, column=3)
    elif BMI>25 and BMI<29.9:
        Label(store, text='YOU ARE OVERWEIGHT ').grid(row=0, column=3)
    elif BMI>=30:
        Label(store, text='YOU ARE OBESE ').grid(row=0, column=3)

    Label(store, text='YOUR BMI IS ' + str(BMI)).grid(row=1, column=3)  # Heading
    Label(store, text=" Pls enter your name ").grid(row=2, column=2)
    global nm
    nm = StringVar()
    Entry(store, width=20, textvariable=nm).grid(row=2, column=3)
    Button(store, text="Store Values",command=conclusion).grid(row=3, column=3)




def quit_loop():
    global selection
    selection = var.get()
    master.destroy()

def Metricformula():# Function that calculates BMI using Metric formula
    Kilograms = int(kg.get())
    Centimetres = int(cm.get())
    Metres = int(Centimetres / 100)

    IntValidation(str(kg.get()))
    IntValidation(str(cm.get()))

    if x == False:
        Label(root, text="You Inputted one or more Invalid Values.Please Reenter it").grid(row=5, column=3)
    elif x == True:
         global BMI
         BMI = (Kilograms / (Metres * Metres))
         print("Your BMI is : " + str(BMI))
         database()
         root.destroy()


def Englishimperial():# Function that calaculates BMI according to English Imperial
    Stones = int(stn.get())
    Pounds = int(pn.get())
    Feet = int(ft.get())
    Inches = int(inc.get())

    IntValidation(str(stn.get()))
    IntValidation(str(pn.get()))
    IntValidation(str(ft.get()))
    IntValidation(str(inc.get()))

    if x==False:
     Label(root, text="You Inputted one or more Invalid Values.Please Reenter it").grid(row=5, column=3)
    elif x==True:
         Pound2 = Stones * 14
         Inch2 = Feet * 12
         Totalpounds = Pound2 + Pounds
         TotalInches = Inches + Inch2
         global BMI
         BMI = (Totalpounds / (TotalInches * TotalInches))

         print("Your BMI is : " + str(BMI))
         database()
         root.destroy()

def IntValidation(S):# Function that validates Value is an Integer
    global x
    x= S.isdigit()



def Fullbody():# Function that takes all the Weight and Height values
    global var
    Label(master, text="SELECT BMI FORMULA").grid(row=0, sticky=W)
    Radiobutton(master, text="English Imperial Formula", variable=var, value=1).grid(row=1, sticky=W)
    Radiobutton(master, text="Metric Formula ", variable=var, value=2).grid(row=2, sticky=W)
    Button(master, text="OK", command=quit_loop).grid(row=3, sticky=W)

    master.mainloop()
    global root
    root = Tk()
    root.title('BMI Program')
    global stn
    global pn
    global ft
    global kg
    global cm
    global inc
    kg = IntVar()
    cm = IntVar()
    stn = IntVar()
    pn = IntVar()
    ft = IntVar()
    inc = IntVar()

    # English Imperial Formula
    if selection == 1:
        # Weight code as in heaviness
        Label(root, text='Enter your Weight ').grid(row=0, column=3)  # Heading
        Label(root, text=" Stones ").grid(row=1, column=1)
        Entry(root, width=20, textvariable=stn).grid(row=1, column=2)

        Label(root, text=" Pounds ").grid(row=1, column=3)
        Entry(root, width=20, textvariable=pn).grid(row=1, column=4)

        # Height code as in tallness
        Label(root, text='Enter your Height ').grid(row=2, column=3)  # Heading
        Label(root, text=" Feet ").grid(row=3, column=1)
        Entry(root, width=20, textvariable=ft).grid(row=3, column=2)

        Label(root, text=" Inches ").grid(row=3, column=3)
        Entry(root, width=20, textvariable=inc).grid(row=3, column=4, sticky=E)
        Button(root, text="Calculate your BMI Now", command=Englishimperial).grid(row=4, column=3)

        # Metric Formula
    elif selection == 2:
        # Weight code as in heaviness
         Label(root, text='Enter your Weight').grid(row=0, column=3)  # Heading
         Label(root, text=" KGs ").grid(row=1, column=2)
         Entry(root, width=20, textvariable=kg).grid(row=1, column=3)

        # Height code as in tallness
         Label(root, text='Enter your Height').grid(row=2, column=3)  # Heading
         Label(root, text=" CM ").grid(row=3, column=2)
         Entry(root, width=20, textvariable=cm).grid(row=3, column=3)
         Button(root, text="Calculate your BMI Now", command=Metricformula).grid(row=4, column=3)

    root.mainloop()

Fullbody()

