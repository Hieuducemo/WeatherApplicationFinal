from tkinter import *
import tkinter as tk
from urllib import request 
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder 
from datetime import datetime 
import pytz 
from tkintermapview import TkinterMapView
from WeatherAPI import WeatherAPI
from tkinter import ttk, messagebox
class GUI:
    """The text describes a class called "GUI", which is used to create a graphical user interface for a weather application.
       The class has a constructor that initializes the window, sets its dimensions, title, and background image"""
    def __init__(self, root):
        #Initialize window
        self.root = root
        self.root.title("Weather App")
        self.root.geometry("1200x600+300+200")
        #background
        self.background_image = PhotoImage(file='background.png')
        self.background_image = self.background_image.subsample(1)
        self.background_label = Label(root, image=self.background_image, bg='white')
        self.background_label.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.root.resizable(True, True)
        self.creat_widgets()

    def creat_widgets(self):
        Search_image = PhotoImage(file="search_box.png")
        myimage=Label(image=Search_image)
        myimage.place(x=20,y=20)

        self.textfield = tk.Entry(self.root,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border =0,fg="red")
        self.textfield.place(x=50,y=40)
        self.textfield.focus()

        Search_icon= PhotoImage(file="icon_search3.png")
        #button, when click the button, method check_weather will run
        myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=self.search_Weather)
        myimage_icon.place(x=420,y=23)

        Logo = PhotoImage(file="Logo.png")
        logo=Label(image=Logo)
        logo.place(x=50,y=180)

        Frame = PhotoImage(file="Bottom2.png")
        frame_myimage = Label(image= Frame)
        frame_myimage.pack(padx=5,pady=5,side=BOTTOM)

        #time
        self.name=Label(self.root,font=("arial",15,"bold"))
        self.name.place(x=30,y=100)
        self.clock=Label(self.root,font=("Helvetica",20))
        self.clock.place(x=30,y=130)
        #Add label
        label1 = Label(self.root,text="WIND",font=("Helvetice",15,'bold'),fg="white",bg="#1ab5ef")
        label1.place(x=120,y=520)

        label2 = Label(self.root,text="HUMIDITY",font=("Helvetice",15,'bold'),fg="white",bg="#1ab5ef")
        label2.place(x=320,y=520)

        label3 = Label(self.root,text="DESCRIPTION",font=("Helvetice",15,'bold'),fg="white",bg="#1ab5ef")
        label3.place(x=520,y=520)

        label4 = Label(self.root,text="PRESSURE",font=("Helvetice",15,'bold'),fg="white",bg="#1ab5ef")
        label4.place(x=820,y=520)

        self.t=Label(font=("arial",70,'bold'),fg="#ee666d")
        self.t.place(x=400,y=150)
        self.c=Label(font=("arial",15,'bold'))
        self.c.place(x=350,y=250)

        self.w=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
        self.w.place(x=120,y=550)
        self.w1=Label(text="m/s",font=("arial",20,"bold"),bg="#1ab5ef")
        self.w1.place(x=180,y=550)

        self.h=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
        self.h.place(x=320,y=550)
        self.h1 = Label(text="%",font=("arial",20,"bold"),bg="#1ab5ef")
        self.h1.place(x=380,y=550)

        self.d=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
        self.d.place(x=520,y=550)


        self.p=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
        self.p.place(x=820,y=550)
        self.p1=Label(text="nPa",font=("arial",20,"bold"),bg="#1ab5ef")
        self.p1.place(x=890,y=550)
        self.root.mainloop()

    def search_Weather(self):
        #take the value from textbox
        city = self.textfield.get()
        weather = WeatherAPI.get_weather(city)
        # to get the latitude and longitude coordinates of a specified city using the Nominatim geocoder.
        geolocator=Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        # to determine the timezone at the specified latitude and longitude coordinates, and then use the pytz library to get the current time in that timezone.
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time = local_time.strftime("%I:%M%p")
        self.clock.config(text=current_time)
        self.name.config(text="CURRENT TIME")

        try:
         self.t.config(text=(weather[2],"\u00B0"))
         self.c.config(text=(weather[0],"|","FEELS","LIKE",weather[0],"\u00B0"))

         self.w.config(text=weather[5])
         self.h.config(text=weather[4])
         self.d.config(text=weather[1])
         self.p.config(text=weather[3])

         widgetmap_widget = TkinterMapView(self.root,width=550,height =350)
         widgetmap_widget.pack(expand =False)
         widgetmap_widget.set_address(city, marker=True)
         widgetmap_widget.place(x=630,y=80)
        except Exception as e:
         messagebox.showerror("Weather App","Invalid Entry!!")