import tkinter as tk
from tkinter import *
import COVID19Py
import webbrowser
kt=COVID19Py.COVID19()
url="https://www.willmaster.com/blog/misc/country-name-abbreviations.php"
new=1
def show_entry_fields():
    cd=x.get()
    code=kt.getLocationByCountryCode(cd)
    ld=code[0]
    vd=dict(ld['latest'])
    box.insert(INSERT,"Country Name = "+ld['country']+","+ld['country_code']+"\n")
    box.insert(INSERT,"Country Population = "+str(ld['country_population'])+"\n")
    box.insert(INSERT,"Confirmed = "+str(vd['confirmed'])+"\n")
    box.insert(INSERT,"Deaths = "+str(vd['deaths'])+"\n")
    box.insert(INSERT,"Recovered = "+str(vd['recovered'])+"\n")
    lu=ld['last_updated']
    box.insert(INSERT,"Last Updated = "+lu[0:10]+"\n")

def site():
    webbrowser.open(url,new=new)

def clr():
	box.delete("1.0","end")

master = tk.Tk()
master.title("Corona Details")
master.geometry('600x400')
tk.Label(master,text="First Find Country code by clicking this button: ").grid(row=0,column=0)
Btn=Button(master,text="Click for codes",command=site).grid(row=0,column=1)
tk.Label(master,text="Enter Country Name: \n Eg:- India = In \n united States = Us \n United Kingdom = Gb ").grid(row=2,column=0)
x = tk.Entry(master)
x.grid(row=2, column=1)
box = tk.Text(master, height=10, width=50)
box.grid(row=4,columnspan=2)
tk.Button(master,text='Quit',command=master.quit).grid(row=3,column=1, 
                                    sticky=tk.W, 
                                    pady=4,padx=100)
tk.Button(master,text='Show',command=show_entry_fields).grid(row=3, 
                                                       column=0,padx=50,
                                                       sticky=tk.W, 
                                                       pady=4)
tk.Button(master,text='Clear',command=clr).grid(row=3,column=0,padx=150,sticky=tk.W,pady=4)

tk.mainloop()