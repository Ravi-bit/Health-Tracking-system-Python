from tkinter import *
import tkinter.font as font

from tkinter import ttk
from tkinter import messagebox

import time
import sqlite3


#Database connection and tables creation part
if __name__ == "__main__":
    global conn
    conn = sqlite3.connect("../assets/Users.db")
    cursor = conn.cursor()
  
    try:

        command = (
            """CREATE TABLE IF NOT EXISTS Users_Details
        (NAME TEXT NOT NULL, 
        AGE INTEGER NOT NULL,
        GENDER TEXT NOT NULL,
        HEIGHT REAR NOT NULL,
        WEIGHT REAR NOT NULL,
        BP REAR NOT NULL,
        BMI REAR NOT NULL,
        HEART_BEAT REAR NOT NULL
        )"""
        )
        conn.execute(command)
        conn.execute(
            """CREATE TABLE IF NOT EXISTS Users_tbl
            (USERNAME TEXT NOT NULL, 
            PASSWORD TEXT NOT NULL
            )"""
        )
       
    except:
        pass

conn = sqlite3.connect("../assets/Users.db")





#Main Screen part
def check_additional_details(name):
    user_exist = False
    command = 'SELECT NAME from Users_Details WHERE NAME = "' + name + '"'
    cursor = conn.execute(command)
    rows = cursor.fetchone()
    
    if rows == None:
        user_exist = False
    else:
        user_exist = True
    if user_exist:
        return True    
    else:
        return False



def calculate_bmi(h,w):
    user_weight = w
    user_height =h
    return user_weight/(user_height/100)**2


def insert_details(username, age, gender, height, weight, bp, bmi, hb):
    cursor = conn.cursor()
    command = """INSERT INTO Users_Details (NAME, AGE, GENDER, HEIGHT, WEIGHT, BP ,BMI, HEART_BEAT) VALUES (?, ?, ?, ?, ?, ?, ?, ?);"""
    data_tuple = (username, age, gender, height, weight, bp, bmi, hb)
    cursor.execute(command, data_tuple)
    conn.commit()
    return True
def confirm_update(username, age, gender, height, weight, bp, bmi, hb):
    command = """Update Users_Details set AGE = ?, GENDER =?, HEIGHT =?, WEIGHT =?, BP =?, BMI = ?, HEART_BEAT =?  where NAME = ?"""
    cursor = conn.cursor()
    upt_data_tuple = (age, gender, height, weight, bp, bmi, hb, username)
    cursor.execute(command, upt_data_tuple)
    conn.commit()
    return True
def adding_details():
    global add_gender, add_age, add_height, add_weight, add_BP, add_HB
    add_detail_uname= present_user.capitalize()
    age=add_age.get()
    gender = add_gender.get().capitalize()
    height = add_height.get()
    weight = add_weight.get()
    bp = add_BP.get()
    hb = add_HB.get()
    #print(hb,  bp, weight, height, gender, age, add_detail_uname)
    if(add_detail_uname == '' or age == '' or gender == '' or height == '' or weight == '' or bp == '' or hb == ''):
        messagebox.showerror('Error in Adding details!',"Please Fill all the details...")
    else:
        if(int(age)>=1 and int(age)<=100):
         bmi = float(calculate_bmi(float(height), float(weight)))
         if insert_details(add_detail_uname,int(age),gender,float(height),float(weight),float(bp),bmi, float(hb)):
            res = messagebox.showinfo("Add Account!","Account added successfully")
            if res == 'ok':
              add_additional_details_screen.destroy()
              main_screen.destroy()
              time.sleep(1.5)
              show_main_screen(add_detail_uname)

         else:
            messagebox.showerror('Error while adding!', "Error while adding the details for Username {}".format(add_detail_uname))
        else:
         messagebox.showerror('Error in Adding details!',"Age must be in between 1 and 100...")

def process_updating_details():
    global upt_gender, upt_age, upt_height, upt_weight, upt_BP, upt_HB
    upt_detail_uname= present_user.capitalize()
    age=upt_age.get()
    gender = upt_gender.get()
    height = upt_height.get()
    weight = upt_weight.get()
    bp = upt_BP.get()
    hb = upt_HB.get()
    #print(hb,  bp, weight, height, gender, age, add_detail_uname)
    if(upt_detail_uname == '' or age == '' or gender == '' or height == '' or weight == '' or bp == '' or hb == ''):
        messagebox.showerror('Error in updating details!',"Please Fill all the details...")
    else:
        if(int(age)>=1 and int(age)<=100):
         bmi = float(calculate_bmi(float(height), float(weight)))
         if confirm_update(upt_detail_uname,int(age),gender,float(height),float(weight),float(bp),bmi , float(hb)):
            res = messagebox.showinfo("Updation!","Account details updated successfully")
            if res == 'ok':
              upt_additional_details_screen.destroy()
              #main_screen.destroy()
              #time.sleep(1.5)
              #main_screen(upt_detail_uname)

         else:
            messagebox.showerror('Error while updating!', "Error while updating the details for Username {}".format(upt_detail_uname))
        else:
         messagebox.showerror('Error in updating details!',"Age must be in between 1 and 100...")


def fetch_age(uname):
    command = 'SELECT AGE from Users_Details WHERE NAME = "' + uname + '"'
    cursor = conn.execute(command)
    rows = cursor.fetchone()
    if rows == None:
      return None
    else:
        age = int(rows[0])
        return age


def fetch_bmi(uname):
    command = 'SELECT BMI from Users_Details WHERE NAME = "' + uname + '"'
    cursor = conn.execute(command)
    rows = cursor.fetchone()
    if rows == None:
      return None
    else:
        bmi = float(rows[0])
        return bmi
       
def fetch_height(uname):
    command = 'SELECT HEIGHT from Users_Details WHERE NAME = "' + uname + '"'
    cursor = conn.execute(command)
    rows = cursor.fetchone()
    if rows == None:
      return None
    else:
        height = float(rows[0])
        return height

def fetch_weight(uname):
    command = 'SELECT WEIGHT from Users_Details WHERE NAME = "' + uname + '"'
    cursor = conn.execute(command)
    rows = cursor.fetchone()
    if rows == None:
      return None
    else:
        weight = float(rows[0])
        return weight
def fetch_BP(uname):
    command = 'SELECT BP from Users_Details WHERE NAME = "' + uname + '"'
    cursor = conn.execute(command)
    rows = cursor.fetchone()
    if rows == None:
      return None
    else:
        bp = float(rows[0])
        return bp
def fetch_HB(uname):
    command = 'SELECT HEART_BEAT from Users_Details WHERE NAME = "' + uname + '"'
    cursor = conn.execute(command)
    rows = cursor.fetchone()
    if rows == None:
      return None
    else:
        hb = float(rows[0])
        return hb
def fetch_gender(uname):
    command = 'SELECT GENDER from Users_Details WHERE NAME = "' + uname + '"'
    cursor = conn.execute(command)
    rows = cursor.fetchone()
    if rows == None:
      return None
    else:
        gender = str(rows[0])
        return gender

def display_bmi(BMI, h ,w, name):
    bmi_screen = Tk()
    bmi_screen.title("BMI Recommender for User - {}.".format(name))
    bmi_screen.geometry("700x500")
    Label(bmi_screen,width="300", text="User - {}".format(name), bg="orange",fg="white").pack()
    Label(bmi_screen, text="Height - {}".format(h)).pack()
    Label(bmi_screen, text="Weight - {}".format(w)).pack()
    Label(bmi_screen, text="BMI - {}".format(BMI)).pack()
    frame = Frame(bmi_screen, bd = 2,relief = 'sunken')
    frame.pack(fill = 'both', padx = 10, pady= 10)
    Label(frame, text="You BMI Recommendations :",font=("Algerian", 13, 'bold')).pack()
    if(BMI<18.5):
         
            Label(frame, text="Your BMI is very LOW that means you are in UNDERWEIGHT situation").pack()
            Label(frame, text="Make PROPER DIET with :").pack()
            Label(frame, text="->Eating at least 5 portions of a variety of fruit and vegetables every day.").pack()
            Label(frame, text="->Basing meals on potatoes, bread, rice, pasta or other starchy carbohydrates. Choose wholegrain where possible.").pack()
            Label(frame, text="->Choosing unsaturated oils and spreads, such as sunflower or rapeseed, and eating them in small amounts").pack()
            Label(frame, text="->Drinking plenty of fluids. The government recommends 6 to 8 glasses a day.").pack()
            Label(frame, text="->But try not to have drinks just before meals to avoid feeling too full to eat.").pack()
            Label(frame, text="Do EXCERCISES daily...").pack()
    elif(BMI>=18.5 and BMI<=24.9):
            Label(frame, text="->Your BMI is VERYGOOD that means you are in HEALTHY situation").pack()
            Label(frame, text="->Do EXCERCISES daily to keep your BMI healthy...").pack()
    elif(BMI>=25.0 and BMI<=29.9):
            Label(frame, text="Your BMI is HIGH that means you are in OVERWEIGHT situation").pack()
            Label(frame, text="The best way to achieve this is to swap unhealthy and high-energy food choices – such as fast food, processed food and sugary drinks (including alcohol)").pack()
            Label(frame, text="Make PROPER DIET with :").pack()
            Label(frame, text="->plenty of fruit and vegetable").pack()
            Label(frame, text="->plenty of potatoes, bread, rice, pasta and other starchy foods (ideally you should choose wholegrain varieties)").pack()
            Label(frame, text="->some meat, fish, eggs, beans and other non-dairy sources of protein").pack()
            Label(frame, text="Do EXCERCISES daily which is very important..").pack()
            Label(frame, text="->just small amounts of food and drinks that are high in fat and sugar").pack()
         
    else:
            Label(frame, text="Your BMI is HIGH that means you are in OBESE situation").pack()
            Label(frame, text="CONSULT A DOCTOR FOR QUICK REACTION..").pack()
            Label(frame, text="The best way to achieve this is to swap unhealthy and high-energy food choices – such as fast food, processed food and sugary drinks (including alcohol)").pack()
            Label(frame, text="Make PROPER DIET with :").pack()
            Label(frame, text="->plenty of fruit and vegetables").pack()
            Label(frame, text="->plenty of potatoes, bread, rice, pasta and other starchy foods (ideally you should choose wholegrain varieties)").pack()
            Label(frame, text="->some meat, fish, eggs, beans and other non-dairy sources of protein").pack()
            Label(frame, text="->just small amounts of food and drinks that are high in fat and sugar").pack()
            Label(frame, text="Do EXCERCISES daily which is very important...").pack()

def display_bp(BP_level, uname):
    bp_screen = Tk()
    bp_screen.title("BP Recommender for User - {}.".format(uname))
    bp_screen.geometry("600x500")
    Label(bp_screen,width="300", text="User - {}".format(uname), bg="orange",fg="white").pack()
    Label(bp_screen, text="BP Level - {}".format(BP_level)).pack()
    Label(bp_screen, text="You BP Recommendations :",font=("Algerian", 13, 'bold')).pack()
    frame = Frame(bp_screen, bd = 2,relief = 'sunken')
    frame.pack(fill = 'both', padx = 10, pady= 10)
    if(BP_level<=90):
            Label(frame, text="Your BP level is NOT good that is LOW BLOOD PRESSURE").pack()
            Label(frame, text="->Low blood pressure is less common.").pack()
            Label(frame, text="->Some medicines can cause low blood pressure as a side effect. ").pack()
            Label(frame, text="->It can also be caused by a number of underlying conditions, including heart failure and dehydration.").pack()
    elif(BP_level>=90 and BP_level<=120):
            Label(frame, text="Your BP level is GOOD and HEALTHY").pack()
            
    else:   
            Label(frame, text="Your BP level is NOT good that is HIGH BLOOD PRESSURE").pack()
            Label(frame, text="->High blood pressure is often related to unhealthy lifestyle habits, such as smoking, drinking too much alcohol, being overweight and not exercising enough.").pack()
            Label(frame, text="->Left untreated, high blood pressure can increase your risk of developing a number of serious long-term health conditions, such as coronary heart disease and kidney disease.").pack()

def display_hb(Hb, uname, a):
    hb_screen = Tk()
    hb_screen.title("BP Recommender for User - {}.".format(uname))
    hb_screen.geometry("500x400")
    Label(hb_screen,width="300", text="User - {}".format(uname), bg="orange",fg="white").pack()
    Label(hb_screen, text="Age - {}".format(a)).pack()
    Label(hb_screen, text="Heart Beat Level - {}".format(Hb)).pack()
    Label(hb_screen, text="You Heart Beat Recommendations :",font=("Algerian", 13, 'bold')).pack()
    frame = Frame(hb_screen, bd = 2,relief = 'sunken')
    frame.pack(fill = 'both', padx = 10, pady= 10)
    if a > 0 and a < 3:
         if Hb < 80 or Hb > 130:
            l = Label(frame, bg = "RED", text="Your HB  level is NOT good..80 to 130 BPM is recommended for your age but you have {} BPM".format(Hb)).pack()
          
         else:
            l = Label(frame, bg = "GREEN", text="Your HB  level is GOOD").pack()
           
    elif a >= 3 and a < 5:
          if Hb < 80 or Hb > 120:
            l = Label(frame, bg = "RED", text="Your HB level is NOT good..80 to 120 BPM is recommended for your age but you have {} BPM".format(Hb)).pack()
            
          else:
            l = Label(frame, bg = "GREEN", text="Your HB  level is GOOD").pack()
         
    elif a >= 5 and a < 10:
          if Hb < 70 or Hb > 110:
            l = Label(frame, bg = "RED", text="Your HB  level is NOT good..70 to 110 BPM is recommended for your age but you have {} BPM".format(Hb)).pack()
       
          else:
            l = Label(frame, bg = "GREEN", text="Your HB  level is GOOD").pack()
        
    elif a >= 10 and a < 16:
          if Hb < 60 or Hb > 105:
            l = Label(frame, bg = "RED", text="Your HB  level is NOT good..60 to 105 BPM is recommended for your age but you have {} BPM".format(Hb)).pack()
        
          else:
            l = Label(frame, bg = "GREEN", text="Your HB  level is GOOD").pack()
          
    elif a >= 16:
          if Hb < 60 or Hb > 100:
            l = Label(frame, bg = "RED", text="Your HB  level is NOT good..60 to 100 BPM is recommended for your age but you have {} BPM".format(Hb)).pack()
          else:
            l = Label(frame, bg = "GREEN", text="Your HB  level is GOOD").pack()
           
    else:
        pass                
   

def show_bmi():
    if check_additional_details(present_user):
       show_bmi = fetch_bmi(present_user)
       show_height = fetch_height(present_user)
       show_weight = fetch_weight(present_user)
       display_bmi(show_bmi,show_height,show_weight, present_user)
    else:
      res = messagebox.showinfo('OOPs..!','No health values entered!. First add the required details to check the BMI! click "ok" now to add details!')
      if res == 'ok':
          add_additional_details()
      else:
          pass 

def show_bp():
    if check_additional_details(present_user):
       show_bp = fetch_BP(present_user)
       display_bp(show_bp, present_user)
    else:
      res = messagebox.showinfo('OOPs..!','No health values entered!. First add the required details to check the BMI! click "ok" now to add details!')
      if res == 'ok':
          add_additional_details()
      else:
          pass 
def show_heart_beat():
    if check_additional_details(present_user):
       show_hb = fetch_HB(present_user)
       show_age = fetch_age(present_user)
       display_hb(show_hb, present_user, show_age)
    else:
      res = messagebox.showinfo('OOPs..!','No health values entered!. First add the required details to check the BMI! click "ok" now to add details!')
      if res == 'ok':
          add_additional_details()
      else:
          pass

def process_medicines(uname, name, quantity, time):
    cursor = conn.cursor()
    command = """INSERT INTO {}_Medicines (Medicine_name,QUANTITY,TIME) VALUES (?, ?, ?);""".format(uname)
    med_data_tuple = (name, quantity, time)
    cursor.execute(command, med_data_tuple)
    conn.commit()
    return True

def adding_medicines():
    global add_mname, add_quantity, add_timings
    med_uname= present_user.capitalize()  
    mname=add_mname.get()
    quantity = add_quantity.get()
    time = add_timings.get()
    #print(hb,  bp, weight, height, gender, age, add_detail_uname)
    if(med_uname == '' or mname == '' or  quantity == '' or time == ''):
        messagebox.showerror('Error in Adding details!',"Please Fill all the details...")
    else:
         if process_medicines(med_uname,mname, quantity, time):
            res = messagebox.showinfo("Add Medicines!","Medicines added successfully")
            if res == 'ok':
              add_medication_screen.destroy()

         else:
            messagebox.showerror('Error while adding!', "Error while adding the details for Username {}".format(med_uname))
        

def update_details():
    global upt_additional_details_screen
    global upt_age, upt_height, upt_weight, upt_BP, upt_HB,upt_gender

    
    upt_additional_details_screen = Tk()
    upt_additional_details_screen.title("Add Details")
    upt_additional_details_screen.geometry("500x400")
    upt_detail_uname= present_user.capitalize()

    old_age = fetch_age(upt_detail_uname)
    old_height = fetch_height(upt_detail_uname)
    old_weight = fetch_weight(upt_detail_uname)
    old_BP = fetch_BP(upt_detail_uname)
    old_HB = fetch_HB(upt_detail_uname)
    old_gender = fetch_gender(upt_detail_uname)
    Label(upt_additional_details_screen,width="300", text="Please enter details below", bg="orange",fg="white").pack()

    Label(upt_additional_details_screen, text="Enter age(b/w 1-100 yrs only*").place(x=50,y=60)
    upt_age = Entry(upt_additional_details_screen, width= 22)
    upt_age.focus_set()
    upt_age.place(x=230,y=60)
   
    Label(upt_additional_details_screen, text="Gender * ").place(x=50,y=100)

    upt_gender = Entry(upt_additional_details_screen, width= 22)
    upt_gender.focus_set()
    upt_gender.place(x=230,y=100)
   

    Label(upt_additional_details_screen, text="Enter height in (cm)*").place(x=50,y=150)
    upt_height = Entry(upt_additional_details_screen, width= 22)
    upt_height.focus_set()
    upt_height.place(x=230,y=150)
 

    Label(upt_additional_details_screen, text="Enter weight in (kg)*").place(x=50,y=190)
    upt_weight = Entry(upt_additional_details_screen, width= 22)
    upt_weight.focus_set()
    upt_weight.place(x=230,y=190)
  

    Label(upt_additional_details_screen, text="Enter your BP levels*").place(x=50,y=230)
    upt_BP = Entry(upt_additional_details_screen, width= 22)
    upt_BP.focus_set()
    upt_BP.place(x=230,y=230)

    Label(upt_additional_details_screen, text="Enter your heartbeat levels*").place(x=50,y=270)
    upt_HB = Entry(upt_additional_details_screen, width= 22)
    upt_HB.focus_set()
    upt_HB.place(x=230,y=270)
 
    Button(upt_additional_details_screen, text="update details", width=10, height=1, bg="orange",command=process_updating_details).place(x=230,y=310)  


def add_additional_details():
    global add_additional_details_screen
    global add_age, add_height, add_weight, add_BP, add_HB,add_gender
  
    add_additional_details_screen = Tk()
    
    add_additional_details_screen.title("Add Details")
    
    add_additional_details_screen.geometry("500x400")
    
    Label(add_additional_details_screen,width="300", text="Please enter details below", bg="orange",fg="white").pack()

    Label(add_additional_details_screen, text="Enter age(b/w 1-100 yrs only*").place(x=50,y=60)
    add_age = Entry(add_additional_details_screen, width= 22)
    add_age.focus_set()
    add_age.place(x=230,y=60)
    
    Label(add_additional_details_screen, text="Gender * ").place(x=50,y=100)

    add_gender = Entry(add_additional_details_screen, width= 22)
    add_gender.focus_set()
    add_gender.place(x=230,y=100)
    
    Label(add_additional_details_screen, text="Enter height in (cm)*").place(x=50,y=150)
    add_height = Entry(add_additional_details_screen, width= 22)
    add_height.focus_set()
    add_height.place(x=230,y=150)

    Label(add_additional_details_screen, text="Enter weight in (kg)*").place(x=50,y=190)
    add_weight = Entry(add_additional_details_screen, width= 22)
    add_weight.focus_set()
    add_weight.place(x=230,y=190)

    Label(add_additional_details_screen, text="Enter your BP levels*").place(x=50,y=230)
    add_BP = Entry(add_additional_details_screen, width= 22)
    add_BP.focus_set()
    add_BP.place(x=230,y=230)

    Label(add_additional_details_screen, text="Enter your heartbeat levels*").place(x=50,y=270)
    add_HB = Entry(add_additional_details_screen, width= 22)
    add_HB.focus_set()
    add_HB.place(x=230,y=270)

    Button(add_additional_details_screen, text="Add details", width=10, height=1, bg="orange",command=adding_details).place(x=230,y=310)


def add_medication():
        global add_medication_screen
        global add_mname, add_quantity, add_timings
      
        add_medication_screen = Tk()
        add_medication_screen.title("Add Medications")
    
        add_medication_screen.geometry("500x400")
    
        Label(add_medication_screen,width="300", text="Please enter details below", bg="orange",fg="white").pack()

        Label(add_medication_screen, text="Enter medicine name*").place(x=50,y=60)
        add_mname = Entry(add_medication_screen, width= 22)
        add_mname.focus_set()
        add_mname.place(x=230,y=60)
        
        Label(add_medication_screen, text="Quantity per consumption* ").place(x=50,y=100)

        add_quantity = Entry(add_medication_screen, width= 22)
        add_quantity.focus_set()
        add_quantity.place(x=230,y=100)
        
        Label(add_medication_screen, text="Time *").place(x=50,y=140)
        add_timings = Entry(add_medication_screen, width= 22)
        add_timings.focus_set()
        add_timings.place(x=230,y=140)

        Button(add_medication_screen, text="Add entry", width=10, height=1, bg="orange",command=adding_medicines).place(x=200,y=190)

def check_medicine_details(uname):
    command = 'SELECT * from {}_Medicines'.format(uname)
    cursor = conn.execute(command)
    data = cursor.fetchall()
    if len(data) == 0:
        return False
    else:
        return True

def fetch_medicines(uname):
    command = 'SELECT * from {}_Medicines'.format(uname)
    cursor = conn.execute(command)
    data = list(cursor.fetchall())
    for i in data:
        print(i)
    medicines = []
    if len(data) == 0:
        return medicines
    else:
        for i in data:
            medicines.append(list(i))
        return medicines    

def display_medicines(med, uname):
    show_med_screen = Tk()
    show_med_screen.title("Medicines for User - {}.".format(uname))
    show_med_screen.geometry("600x600")
    Label(show_med_screen,width="300", text="User - {}".format(uname), bg="orange",fg="white").pack()

    Label(show_med_screen, text="You Medicines :",font=("Algerian", 13, 'bold')).pack()
    frame = Frame(show_med_screen, bd = 2,relief = 'sunken')
    frame.pack(fill = 'both', padx = 10, pady= 10)
    if(len(med) == 0):
        Label(frame, text="No data found").pack()
    else:
        for i in range(0, len(med)):
          Label(frame, text="medicine name : "+med[i][0]+ ", quantity : "+ str(med[i][1])+ ", time : "+med[i][2]).pack()

def show_medication():
    if check_medicine_details(present_user):
       med_arr = fetch_medicines(present_user)
       print(med_arr)
       display_medicines(med_arr, present_user)
    else:
      res = messagebox.showinfo('OOPs..!','No Medicines stored!. First add the required details to check the BMI! click "ok" now to add details!')
      if res == 'ok':
          add_medication()
      else:
          pass 

   



def logout():
    global present_user
    main_screen.destroy()
    present_user = None
    home_page()

def show_main_screen(logged_user):
    global main_screen
    global present_user
    present_user = logged_user
    main_screen=Tk()
    main_screen.title("Health tracker for user -{}.".format(present_user))
    main_screen.geometry("650x580")
    main_screen.config(bg = "#ceebd5")

    Tops = Frame(main_screen, width=100, height=30, bd=8, relief="raise")
    Tops.grid(row = 0,  padx= 40, pady=25)
    lbl_T1 = Label(Tops, text="HEALTH TRACKING SYSTEM", padx=10, pady=10, bd=8, fg='#000000',font=("Algerian", 23, 'bold'), bg="navajo white", relief='raise', width=28, height=1)
    lbl_T1.pack()

    myFont = font.Font(family='Helvetica', size=12, weight='bold')
    if not check_additional_details(present_user):
        btn1 = Button(main_screen, text = 'Add Details',  width = 18 , bg='#0052cc', fg='#ffffff', command = add_additional_details)
        btn1['font'] = myFont
        btn1.grid(row = 1, column = 0, pady = 7)
    else:
        btn2 = Button(main_screen, text = 'Update Details',  width = 18 , bg='#0052cc', fg='#ffffff', command = update_details)
        btn2['font'] = myFont
        btn2.grid(row = 1, column = 0, pady = 7)   
    
    bmi = Button(main_screen, text = 'BMI Recommender',width = 18, bg='#34ebc3', fg='#ffffff', command = show_bmi)
    bmi['font'] = myFont
    bmi.grid(row = 2, column = 0, pady = 7)
    btn3 = Button(main_screen, text = 'BP Recommender',width = 18, bg='#ebe834', fg='#ffffff', command = show_bp)
    btn3['font'] = myFont
    btn3.grid(row = 3, column = 0, pady = 7)
    btn4 = Button(main_screen, text = 'Heart beat recommender',width = 18, bg='#eb8034', fg='#ffffff', command = show_heart_beat)
    btn4['font'] = myFont
    btn4.grid(row = 4, column = 0, pady = 7)
    btn5 = Button(main_screen, text = 'Add your medications',width = 18, bg='#349beb', fg='#ffffff', command = add_medication)
    btn5['font'] = myFont
    btn5.grid(row = 5, column = 0, pady = 7)
    btn6 = Button(main_screen, text = 'Check Your medications',width = 18, bg='#9651f0', fg='#ffffff', command = show_medication)
    btn6['font'] = myFont
    btn6.grid(row = 6, column = 0, pady = 7)
   
    btn8 = Button(main_screen, text = 'Log out!',width = 18, bg='#eb3459', fg='#ffffff', command = logout)
    btn8['font'] = myFont
    btn8.grid(row = 7, column = 0, pady = 7)
    main_screen.mainloop()
   








#Home screen part
def get_password(username):
    command = 'SELECT PASSWORD from Users_tbl WHERE USERNAME = "' + username + '"'
    cursor = conn.execute(command)
    for row in cursor:
        password = row[0]
    return password


def check_details(username):
    cursor = conn.execute("SELECT USERNAME from Users_tbl where USERNAME = ?", (username,))
    data = cursor.fetchall()
    if len(data) == 0:
        return False
    else:
        return True


def login():
    global username, password
    uname=username.get().capitalize()
    pwd=password.get()
    #applying empty validation
    if uname=='' or pwd=='':
      messagebox.showerror('Log In error!', 'Please! Fill the empty fields!')
    else:
      flag = check_details(uname)
      if flag:
            if get_password(uname) == pwd:
               res = messagebox.showinfo("Log In!","Logged in successfully")
               if res == 'ok':
                   login_screen.destroy()
                   home_screen.destroy()
                   show_main_screen(uname)
            else:
               messagebox.showerror('Log In error!',"Your password does not seem to match...")
      else:
        messagebox.showerror('Log In error!', "Incorrect username")

def process_account(username, password):
    command1 = (
            """CREATE TABLE IF NOT EXISTS {}_Medicines 
        (Medicine_name TEXT NOT NULL, 
        QUANTITY TEXT NOT NULL,
        TIME TEXT NOT NULL)"""
        ).format(username)
    command = (
        'INSERT INTO Users_tbl (USERNAME,PASSWORD) VALUES("'
        + username
        + '","'
        + password
        + '");'
    )
    conn.execute(command)
    conn.execute(command1)
    conn.commit()
    return True

def adding_ac():
    global ac_username, ac_password
    ac_uname= ac_username.get().capitalize()
    ac_pwd=ac_password.get()
    if ac_uname=='' or ac_pwd=='':
      messagebox.showerror('Error while adding ac!', 'Please! Fill the empty fields!')
    else:
      flag = check_details(ac_uname)
      if flag:
        messagebox.showerror('Error while adding ac!', "Username {} already exists.".format(ac_uname))  
      else:
        res = messagebox.askquestion('Adding account updation', 'Do you like to add account?') 
        if res == 'yes':
            if process_account(ac_uname, ac_pwd):
             res = messagebox.showinfo("Add Account!","Account added successfully")
             add_ac_screen.destroy()
            else:   
             messagebox.showerror('Error while adding account!', "Error while adding account for Username {}\n".format(ac_uname))     
        else:
            add_ac_screen.destroy()  

def confirm_update_pwd(user, pswd):
    command = (
        'UPDATE Users_tbl set PASSWORD = "'
        + pswd
        + '" where USERNAME = "'
        + user
        + '"'
    )
    conn.execute(command)
    conn.commit()
    return True

def updating_pswd():
    global up_username, old_password, new_password
    up_uname= up_username.get().capitalize()
    old_pwd=old_password.get()
    new_pwd = new_password.get()
    if up_uname=='' or old_pwd=='' or new_pwd == '':
        messagebox.showerror('Error while updating password!', 'Please! Fill the empty fields!')
    else:    
        flag = check_details(up_uname)
        if flag:
                if get_password(up_uname) == old_pwd:
                    res = messagebox.askquestion('Password updation', 'Do you want to update password?')
                    if res == 'yes':
                        if confirm_update_pwd(up_uname, new_pwd):
                         messagebox.showinfo("Update password!","Password Updated successfully") 
                         update_pswd_screen.destroy()  
                        else:
                         messagebox.showerror('Update password!', "Error while updating password for Username {}".format(up_uname)) 
                    else:
                        update_pswd_screen.destroy()         
                else:
                    messagebox.showerror('Error in Updating password!', "Old password is not correct for Username '{}'. Please check!".format(up_uname))     
        else:
            messagebox.showerror('Update password!', "There are no details for Username '{}'. Please check the username".format(up_uname))     

def log_in_page():
    global login_screen
    login_screen = Tk()
    #Setting title of screen
    login_screen.title("Login Screen")
    #setting height and width of screen
    login_screen.geometry("500x300")
    #declaring variable
    global username
    global password
  
    #Creating layout of login form
    Label(login_screen,width="300", text="Please enter details below", bg="orange",fg="white").pack()
    #Username Label
    Label(login_screen, text="Username * ").place(x=130,y=60)
    #Username textbox
    username= Entry(login_screen, width= 20)
    username.focus_set()
    username.place(x=220,y=60)
    #Password Label
    Label(login_screen, text="Password * ").place(x=130,y=100)
    #Password textbox
    password= Entry(login_screen, width= 20, show="*")
    password.focus_set()
    password.place(x=220,y=100)
    #Login button
    Button(login_screen, text="Login", width=10, height=1, bg="orange",command=login).place(x=230,y=150)

def add_ac():
    global add_ac_screen
    global ac_username, ac_password
    add_ac_screen = Tk()
    #Setting title of screen
    add_ac_screen.title("Add Account")
    #setting height and width of screen
    add_ac_screen.geometry("500x300")
    #declaring variable
   
    #Creating layout of login form
    Label(add_ac_screen,width="300", text="Please enter details below", bg="orange",fg="white").pack()
    #Username Label
    Label(add_ac_screen, text="Username * ").place(x=130,y=60)
    ac_username = Entry(add_ac_screen, width= 20)
    ac_username.focus_set()
    ac_username.place(x=220,y=60)
    #Password Label
    Label(add_ac_screen, text="Password * ").place(x=130,y=100)
    #Password textbox
    ac_password= Entry(add_ac_screen, width= 20, show="*")
    ac_password.focus_set()
    ac_password.place(x=220,y=100)
    #add ac button
    Button(add_ac_screen, text="Add account", width=10, height=1, bg="orange",command=adding_ac).place(x=230,y=150)

def update_pswd():
    global update_pswd_screen
    global up_username, old_password, new_password
    update_pswd_screen = Tk()
    #Setting title of screen
    update_pswd_screen.title("Update Password")
    #setting height and width of screen
    update_pswd_screen.geometry("500x300")
    #declaring variable
   
    #Creating layout of login form
    Label(update_pswd_screen,width="300", text="Please enter details below", bg="orange",fg="white").pack()
    #Username Label
    Label(update_pswd_screen, text="Username * ").place(x=130,y=60)
    up_username = Entry(update_pswd_screen, width= 20)
    up_username.focus_set()
    up_username.place(x=220,y=60)
    #Password Label
    Label(update_pswd_screen, text="Old Password * ").place(x=130,y=100)
    #Password textbox
    old_password= Entry(update_pswd_screen, width= 20, show="*")
    old_password.focus_set()
    old_password.place(x=220,y=100)
    Label(update_pswd_screen, text="New Password * ").place(x=130,y=140)
    #New Password textbox
    new_password= Entry(update_pswd_screen, width= 20, show="*")
    new_password.focus_set()
    new_password.place(x=220,y=140)
    Button(update_pswd_screen, text="update", width=10, height=1, bg="orange",command=updating_pswd).place(x=230,y=200)

def confirm_delete(user):
    command = 'DELETE from Users_tbl where USERNAME = "' + user + '"'
    command1 = 'DELETE from Users_Details where NAME = "' + user + '"'
    command2 = 'DROP TABLE '+user+'_Medicines'
    conn.execute(command)
    conn.execute(command1)
    conn.execute(command2)
    conn.commit() 
    return True   

def deleting_ac():
    global del_username, del_password
    del_uname= del_username.get().capitalize()
    del_pwd=del_password.get()
    if del_uname=='' or del_pwd=='':
        messagebox.showerror('Error while deleting the account!', 'Please! Fill the empty fields!')
    else:
        flag = check_details(del_uname)
        if flag:
            if get_password(del_uname) == del_pwd:
                res = messagebox.askquestion('Delete Account', 'Do you want to delete account?') 
                if res == 'yes':
                  if confirm_delete(del_uname):
                    res = messagebox.showinfo("Delete Account!","Account deleted successfully")
                    delete_ac_screen.destroy()
                  else:
                    messagebox.showerror('Error while deleting account!', "Error while deleting account for Username '{}'\n".format(del_uname)) 
                else:
                  delete_ac_screen.destroy()
            else:
                messagebox.showerror('Error in deleting account!', "Password is not correct for Username '{}'. Please check!".format(del_uname))        
        else:
            messagebox.showerror('Error while deleting the account!', "Username '{}' not exists.".format(del_uname))
       

def delete_ac():
    global delete_ac_screen
    global del_username, del_password
    delete_ac_screen = Tk()
    #Setting title of screen
    delete_ac_screen.title("Delete Account")
    #setting height and width of screen
    delete_ac_screen.geometry("500x250")
    #declaring variable
   
    #Creating layout of login form
    Label(delete_ac_screen,width="300", text="Please enter details below", bg="orange",fg="white").pack()
    #Username Label
    Label(delete_ac_screen, text="Username * ").place(x=130,y=60)
    del_username = Entry(delete_ac_screen, width= 20)
    del_username.focus_set()
    del_username.place(x=220,y=60)
    #Password Label
    Label(delete_ac_screen, text="Password * ").place(x=130,y=100)
    #Password textbox
    del_password= Entry(delete_ac_screen, width= 20, show="*")
    del_password.focus_set()
    del_password.place(x=220,y=100)
    Button(delete_ac_screen, text="Delete account", width=10, height=1, bg="orange",command=deleting_ac).place(x=230,y=150)

def home_page():
    global home_screen
    home_screen=Tk()
    home_screen.title("Home Page")
    home_screen.geometry("550x500")
    home_screen.config(bg = "#ceebd5")

    #frame= Frame(home_screen, relief= 'sunken', bg= "#ceebd5")
    #frame.grid(row = 0,  padx= 10, pady=25)

    Tops = Frame(home_screen, width=80, height=30, bd=8, relief="raise")
    Tops.grid(row = 0,  padx= 40, pady=25)
    lbl_T1 = Label(Tops, text="HEALTH TRACKING SYSTEM", padx=10, pady=10, bd=8, fg='#000000',font=("Algerian", 20, 'bold'), bg="navajo white", relief='raise', width=25, height=1)
    lbl_T1.pack()

    myFont = font.Font(family='Helvetica', size=12, weight='bold')
    btn1 = Button(home_screen, text = 'Log in',  width = 15 , bg='#0052cc', fg='#ffffff', command = log_in_page)
    btn1['font'] = myFont
    btn1.grid(row = 1, column = 0, pady = 7, padx = 80)
    btn2 = Button(home_screen, text = 'Add an acccount',width = 15, bg='#34ebc3', fg='#ffffff', command = add_ac)
    btn2['font'] = myFont
    btn2.grid(row = 2, column = 0, pady = 7, padx = 80)
    btn3 = Button(home_screen, text = 'Update Password',width = 15, bg='#ebe834', fg='#ffffff', command = update_pswd)
    btn3['font'] = myFont
    btn3.grid(row = 3, column = 0, pady = 7, padx = 80)
    btn4 = Button(home_screen, text = 'Delete account',width = 15, bg='#eb8034', fg='#ffffff', command = delete_ac)
    btn4['font'] = myFont
    btn4.grid(row = 4, column = 0, pady = 7, padx = 80)
    btn5 = Button(home_screen, text = 'Exit !',width = 15, bg='#eb3459', fg='#ffffff', command = home_screen.destroy)
    btn5['font'] = myFont
    btn5.grid(row = 5, column = 0, pady = 7, padx = 80)
    home_screen.mainloop()
home_page()