from tkinter import *

def miles_to_km():
    miles= float( miles_input.get())
    km= miles*1.609
    kilometer_result_label.config(text=f"{km}") #converts float km to string
window= Tk()
window.title("Mile to km Convertor")

window.config(padx=20,pady=20)
miles_input= Entry(width=7)
miles_input.grid(column=1,row=0)
miles_label= Label(text="Miles")
miles_label.grid(column=2,row=0)
is_equal_label =Label(text="is equal to")
is_equal_label.grid(column=0,row=1)
kilometer_result_label =Label(text="0")
kilometer_result_label.grid(column=1,row=1)
kilometer_label = Label(text="km")
kilometer_label.grid(column=2,row=1)
calculate_button = Button(text="Calculate",command=miles_to_km)
calculate_button.grid(column=1,row=2)











window.mainloop()

# miles_input.grid(column=2,row=0)
#
# my_label=Label(text="It's label",font=("Arial" , 24, "bold"))
# my_label.config(text="New text")
# my_label.grid(column=0,row=0)
#
# def button_clicked():
#     print("Do something")
#
# button=Button(text="Click me", command=button_clicked)
# button.grid(column=1,row=1)
#
# new_button=Button(text="new")
# new_button.grid(column=2,row=0)
#
# #
# # text= Text(height=5, width=30)
# # text.focus()
# # text.insert(END, "Example text to be typed here in multi line")
# # print(text.get("1.0", END))
# # text.pack()
# #
# # def spinbox_used():
# #     print(spinbox.get())
# # spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# # spinbox.pack()
# #
# # def scale_used(value):
# #     print(value)
# # scale= Scale(from_=0, to=100, command=scale_used)
# # scale.pack()
# #
# # def checkbutton_used():
# #     print(checked_state.get())
# # checked_state =IntVar()
# # checkbutton =Checkbutton(text="IS On?",variable=checked_state,command=checkbutton_used)
# # checked_state.get()
# # checkbutton.pack()
# #
# # def radio_used():
# #     print(radio_state.get())
# # radio_state=IntVar()
# # radiobutton1 = Radiobutton(text="Option1",value=1,variable=radio_state,command=radio_used)
# # radiobutton2 = Radiobutton(text="Option2",value=2,variable=radio_state,command=radio_used)
# # radiobutton1.pack()
# # radiobutton2.pack()
# #
# # def listbox_used(event):
# #     print(listbox.get(listbox.curselection()))
# # listbox = Listbox(height=4)
# # places=["kasol","Kerala","Maharastra","Meghalaya","Meghamalai"]
# # for item in places:
# #     listbox.insert(places.index(item), item)
# # listbox.bind("<<listboxSelect>>",listbox_used)
# # listbox.pack()
