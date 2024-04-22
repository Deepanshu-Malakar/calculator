def clear():
    # x=eval(e.get())
    e.delete(0,END)
    # e.insert(0,x)

b_clear=CTkButton(button_frame,text="AC",fg_color="black",bg_color="black",text_color="white",command=clear,width=65,height=35,corner_radius=5)
b_clear.grid(row=4,column=0,padx=5,pady=5)