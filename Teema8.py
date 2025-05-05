from tkinter import *
k=0
def vajutatud():
    global k
    k+=1
    pealkiri.config(text=f"Sa vajutasid nuppu! {k} korda!", bg="white", fg="black" )
    nupp.config(text="Valjuta veel kord!", bg="orange",fg="blue")

def vajutatudPK(event):
    global k
    k-=1
    pealkiri.config(text=f"Sa vajutasid nuppu! {k} korda!", bg="lightblue", fg="pink" )
    nupp.config(text="Valjuta veel kord!", bg="blue",fg="orange")

def tuhista(event):
    sisestus.delete(0,END)
    # sisestus.unhind("<FocusIn>")
    # sisestus.bind("<FocusOut>",tagasi))

aken=Tk()
aken.title("Teema 8")
aken.geometry("400x400")
aken.configure(bg="lightpink")
aken.resizable(width=False, height=True)
aken.iconbitmap("k.ico")
pealkiri=Label(aken, text="Tere tulemast teema 8!", bg="lightpink", font=("Arial", 16), fg="black")
nupp=Button(aken, text="Valjuta mind!", bg="white", font=("Arial", 12), fg="darkred", relief=RAISED, command=vajutatud)#RAISED, GROOVE, RIDGE,SUNKEN
nupp.bind("<Button-3>", vajutatudPK)
sisestus=Entry(aken, bg="white", font=("Arial",12), fg="black")
sisestus.insert(0, "Sisesta midagi alla")
sisestus.bind("<FocusIn>", tuhista)
pealkiri.pack(pady=20)
sisestus.pack(pady=40)
nupp.pack(pady=20)
aken.mainloop()
