import pywinstyles
from tkinter import *
from customtkinter import *
from PIL import Image

root=CTk()
root.title="My Calculator"
set_appearance_mode("light")
set_default_color_theme("green")
pywinstyles.apply_style(root,"acrylic")
root.geometry("320x320")
# root.wm_resizable(False,False)
e=CTkEntry(root,width=300,bg_color="black",justify="center",corner_radius=5,height=50,fg_color="black",text_color="white",border_color="#303336",border_width=0.1,font=("calibri",20))
e.pack(padx=10,pady=10)


button_frame=CTkFrame(root,width=300,fg_color="black",bg_color="black")
button_frame.pack(pady=0,padx=10)

class Key:
    def __init__(self,r,c,t,color="black") -> None:
        self.text=t
        self.button=CTkButton(button_frame,text=t,fg_color=color,bg_color="black",text_color="white",command=self.click,width=65,height=35,corner_radius=5)
        self.button.grid(row=r,column=c,padx=5,pady=5) 
    def click(self):
        e.insert(END,self.text)
    def opacity(self,x):
        pywinstyles.set_opacity(self.button,x)

# creating numerical keys
grey="#303336"
green="#21A666"
b7=Key(0,0,"7")        
b8=Key(0,1,"8")        
b9=Key(0,2,"9") 
minus=Key(0,3,"-",grey)       
b4=Key(1,0,"4")        
b5=Key(1,1,"5")        
b6=Key(1,2,"6")                
plus=Key(1,3,"+",grey)
b1=Key(2,0,"1")        
b2=Key(2,1,"2")        
b3=Key(2,2,"3")        
product=Key(2,3,"*",grey)
b_open=Key(3,0,"(")        
b_0=Key(3,1,"0")        
b_close=Key(3,2,")")   
quotient=Key(3,3,"/",grey)   
b_dot=Key(4,1,".")

def equal():
    x=eval(e.get())
    e.delete(0,END)
    e.insert(0,x)
b_equal=CTkButton(button_frame,text="=",fg_color=grey,bg_color="black",text_color="white",command=equal,width=65,height=35,corner_radius=5)
b_equal.grid(row=4,column=3,padx=5,pady=5)

def clear():
    # x=eval(e.get())
    e.delete(0,END)
    # e.insert(0,x)

b_clear=CTkButton(button_frame,text="AC",fg_color="black",bg_color="black",text_color="white",command=clear,width=65,height=35,corner_radius=5)
b_clear.grid(row=4,column=0,padx=5,pady=5)

def backspace():
    # x=eval(e.get())
    e.delete(len(e.get())-1)
    # e.insert(0,x)
i=CTkImage(Image.open(r"images\backspace.png"),size=(20,20))
b_back=CTkButton(button_frame,text="",image=i,fg_color="black",bg_color="black",text_color="white",command=backspace,width=65,height=35,corner_radius=5)
b_back.grid(row=4,column=2,padx=5,pady=5)
root.mainloop()
