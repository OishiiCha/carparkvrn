from tkinter import *
import DVLAextract as DVLA
import saveData as sd
import time

def entGrab():
    global current_vrn
    current_vrn = vrnent.get()

def vrnSend():
    DVLA.clear_list()
    dvlaBx.config(state='normal')
    dvlaBx.delete('1.0', END)
    entGrab()
    DVLA.requestvrn(current_vrn)
    DVLA.getDVLAdata()
    DVLA.append_data_list()
    DVLA.transpose_data()
    dvlaBx.insert(END,DVLA.textdetails)
    dvlaBx.config(state='disabled')
    time.sleep(1)

def clr():
    if len(wStatus.get()) > 0:
        wStatus.config(state='normal')
        wStatus.delete(0,END)
        wStatus.config(state='disabled')
    dvlaBx.config(state='normal')
    dvlaBx.delete('1.0', END)
    vrnent.delete(0,END)
    dvlaBx.config(state='disabled')

def status():
    wStatus.config(state='normal')
    wStatus.insert(END,"'%s' submitted" % (DVLA.reg))
    wStatus.config(state='disabled')

def writeToFile():
    if len(dvlaBx.get("1.0",'end-1c')) > 0:
        nowtime = sd.WhatTime()
        addline = [DVLA.reg,DVLA.make,DVLA.colour,nowtime]
        sd.WriteToCSV(addline)
        clr()
        status()

def KeyboardInput(kbl):
    if len(wStatus.get()) > 0:
        wStatus.config(state='normal')
        wStatus.delete(0,END)
        wStatus.config(state='disabled')
    vrnent.insert(END,kbl)

def Backspace():
    txt = vrnent.get()[:-1]
    vrnent.delete(0,END)
    vrnent.insert(END,txt)

tFont1 = ("Helvetica",36,"bold")
entFont = ("Helvetica",24)
dvlaFont = ("Helvetica",24)
kbFont = ("Helvetica",24)
vrnentdv = 'e.g. AA19DSL'
btnW = 2
btnH = 2

root = Tk()
root.title('CarPark')
#root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.attributes("-fullscreen", True)

frame1 = Frame(root)
frame2 = Frame(root)
frame3 = Frame(root)
frame4 = Frame(root)
frame5 = Frame(root)
frame6 = Frame(root)

frame1.pack(padx=1,pady=1)
frame2.pack(padx=1,pady=1)
frame3.pack(padx=1,pady=1)
frame4.pack(padx=1,pady=1)
frame5.pack(padx=1,pady=1)
frame6.pack(padx=1,pady=1)

r0frame1 = Frame(frame1)
r0frame1.pack(padx=1,pady=1)
r1frame1 = Frame(frame1)
r1frame1.pack(padx=1,pady=1)


r0frame5 = Frame(frame5)
r0frame5.pack(padx=1,pady=1)
rsframe5 = Frame(frame5)
rsframe5.pack(padx=1,pady=1)
r1frame5 = Frame(frame5)
r1frame5.pack(padx=1,pady=1)
r2frame5 = Frame(frame5)
r2frame5.pack(padx=1,pady=1)
r3frame5 = Frame(frame5)
r3frame5.pack(padx=1,pady=1)
r4frame5 = Frame(frame5)
r4frame5.pack(padx=1,pady=1)


#Frame1
wtitle = Label(r0frame1, text='Car Parking', justify=CENTER, font=tFont1)
wtitle.pack(side=LEFT)
wStatus = Entry(r0frame1, justify=CENTER, font=entFont, borderwidth=0, width=20, state='disabled')
wStatus.pack(side=RIGHT)
wpadder = Label(r0frame1,text='   ',font=tFont1)
wpadder.pack()
submitBtn2 = Button(r1frame1, text='Submit', font=entFont, command=writeToFile)
submitBtn2.pack()

#Frame2
dvlaBx = Text(frame2, font=dvlaFont, state='disabled', height=7, width=40)
dvlaBx.pack(expand=True)

#Frame5
vrnent = Entry(r0frame5, justify=CENTER, font=tFont1, fg='black',bg='yellow', width=10)
vrnent.pack()
submitBtn1 = Button(r0frame5, text='Enter', font=entFont, command=vrnSend)
submitBtn1.pack(side='left')
clrBtn = Button(r0frame5, text='Clear', font=entFont, command=clr)
clrBtn.pack(side='right')
spacer3 = Label(rsframe5,text='',font=tFont1)
spacer3.pack()

n1Btn = Button(r1frame5,text='1', width=btnW, height=btnH, command= lambda: KeyboardInput(1), font=kbFont)
n1Btn.grid(column=1,row=1)
n2Btn = Button(r1frame5,text='2', width=btnW, height=btnH,command= lambda: KeyboardInput(2), font=kbFont)
n2Btn.grid(column=2,row=1)
n3Btn = Button(r1frame5,text='3', width=btnW, height=btnH,command= lambda: KeyboardInput(3), font=kbFont)
n3Btn.grid(column=3,row=1)
n4Btn = Button(r1frame5,text='4', width=btnW, height=btnH,command= lambda: KeyboardInput(4), font=kbFont)
n4Btn.grid(column=4,row=1)
n5Btn = Button(r1frame5,text='5', width=btnW, height=btnH,command= lambda: KeyboardInput(5), font=kbFont)
n5Btn.grid(column=5,row=1)
n6Btn = Button(r1frame5,text='6', width=btnW, height=btnH,command= lambda: KeyboardInput(6), font=kbFont)
n6Btn.grid(column=6,row=1)
n7Btn = Button(r1frame5,text='7', width=btnW, height=btnH,command= lambda: KeyboardInput(7), font=kbFont)
n7Btn.grid(column=7,row=1)
n8Btn = Button(r1frame5,text='8', width=btnW, height=btnH,command= lambda: KeyboardInput(8), font=kbFont)
n8Btn.grid(column=8,row=1)
n9Btn = Button(r1frame5,text='9', width=btnW, height=btnH,command= lambda: KeyboardInput(9), font=kbFont)
n9Btn.grid(column=9,row=1)
n0Btn = Button(r1frame5,text='0', width=btnW, height=btnH,command= lambda: KeyboardInput(0), font=kbFont)
n0Btn.grid(column=10,row=1)

qBtn = Button(r2frame5,text='Q', width=btnW, height=btnH,command= lambda: KeyboardInput('Q'), font=kbFont)
qBtn.grid(column=1,row=1)
wBtn = Button(r2frame5,text='W', width=btnW, height=btnH,command= lambda: KeyboardInput('W'), font=kbFont)
wBtn.grid(column=2,row=1)
eBtn = Button(r2frame5,text='E', width=btnW, height=btnH,command= lambda: KeyboardInput('E'), font=kbFont)
eBtn.grid(column=3,row=1)
rBtn = Button(r2frame5,text='R', width=btnW, height=btnH,command= lambda: KeyboardInput('R'), font=kbFont)
rBtn.grid(column=4,row=1)
tBtn = Button(r2frame5,text='T', width=btnW, height=btnH,command= lambda: KeyboardInput('T'), font=kbFont)
tBtn.grid(column=5,row=1)
yBtn = Button(r2frame5,text='Y', width=btnW, height=btnH,command= lambda: KeyboardInput('Y'), font=kbFont)
yBtn.grid(column=6,row=1)
uBtn = Button(r2frame5,text='U', width=btnW, height=btnH,command= lambda: KeyboardInput('U'), font=kbFont)
uBtn.grid(column=7,row=1)
iBtn = Button(r2frame5,text='I', width=btnW, height=btnH,command= lambda: KeyboardInput('I'), font=kbFont)
iBtn.grid(column=8,row=1)
oBtn = Button(r2frame5,text='O', width=btnW, height=btnH,command= lambda: KeyboardInput('O'), font=kbFont)
oBtn.grid(column=9,row=1)
pBtn = Button(r2frame5,text='P', width=btnW, height=btnH,command= lambda: KeyboardInput('P'), font=kbFont)
pBtn.grid(column=10,row=1)

aBtn = Button(r3frame5,text='A', width=btnW, height=btnH,command= lambda: KeyboardInput('A'), font=kbFont)
aBtn.grid(column=1,row=1)
sBtn = Button(r3frame5,text='S', width=btnW, height=btnH,command= lambda: KeyboardInput('S'), font=kbFont)
sBtn.grid(column=2,row=1)
dBtn = Button(r3frame5,text='D', width=btnW, height=btnH,command= lambda: KeyboardInput('D'), font=kbFont)
dBtn.grid(column=3,row=1)
fBtn = Button(r3frame5,text='F', width=btnW, height=btnH,command= lambda: KeyboardInput('F'), font=kbFont)
fBtn.grid(column=4,row=1)
gBtn = Button(r3frame5,text='G', width=btnW, height=btnH,command= lambda: KeyboardInput('G'), font=kbFont)
gBtn.grid(column=5,row=1)
hBtn = Button(r3frame5,text='H', width=btnW, height=btnH,command= lambda: KeyboardInput('H'), font=kbFont)
hBtn.grid(column=6,row=1)
jBtn = Button(r3frame5,text='J', width=btnW, height=btnH,command= lambda: KeyboardInput('J'), font=kbFont)
jBtn.grid(column=7,row=1)
kBtn = Button(r3frame5,text='K', width=btnW, height=btnH,command= lambda: KeyboardInput('K'), font=kbFont)
kBtn.grid(column=8,row=1)
lBtn = Button(r3frame5,text='L', width=btnW, height=btnH,command= lambda: KeyboardInput('L'), font=kbFont)
lBtn.grid(column=9,row=1)

zBtn = Button(r4frame5,text='Z', width=btnW, height=btnH,command= lambda: KeyboardInput('Z'), font=kbFont)
zBtn.grid(column=1,row=1)
xBtn = Button(r4frame5,text='X', width=btnW, height=btnH,command= lambda: KeyboardInput('X'), font=kbFont)
xBtn.grid(column=2,row=1)
cBtn = Button(r4frame5,text='C', width=btnW, height=btnH,command= lambda: KeyboardInput('C'), font=kbFont)
cBtn.grid(column=3,row=1)
vBtn = Button(r4frame5,text='V', width=btnW, height=btnH,command= lambda: KeyboardInput('V'), font=kbFont)
vBtn.grid(column=4,row=1)
bBtn = Button(r4frame5,text='B', width=btnW, height=btnH,command= lambda: KeyboardInput('B'), font=kbFont)
bBtn.grid(column=5,row=1)
nBtn = Button(r4frame5,text='N', width=btnW, height=btnH,command= lambda: KeyboardInput('N'), font=kbFont)
nBtn.grid(column=6,row=1)
mBtn = Button(r4frame5,text='M', width=btnW, height=btnH,command= lambda: KeyboardInput('M'), font=kbFont)
mBtn.grid(column=7,row=1)
bksBtn = Button(r4frame5,text='BACKSPACE', width=10, height=btnH,command=Backspace, font=kbFont)
bksBtn.grid(column=8,row=1)

#Frame6 --Spacer
spacer2 = Label(frame6,text='',font=tFont1)
spacer2.pack()


if __name__ == '__main__':
    root.mainloop()