from tkinter import *
import time
from os import getcwd
import random
from math import *

class cannon_game:
    def __init__(self,parent):
        self.parent=parent
        bottomframe=Frame(parent, height=100,width=1350)
        bottomframe.grid(row=1)
        topframe=Frame(parent, height=600,width=1350)
        topframe.grid(row=0)
        self.canvas=Canvas(topframe,width=1350, height=600)
        self.canvas.pack()
        angleLabel=Label(bottomframe,text='Enter cannon angle: ')
        angleLabel.grid(row=0, column=0)
        self.angle=StringVar()
        self.angle_entry=Entry(bottomframe,textvariable=self.angle)
        #angle_entry.config(validatecommand=validate_entry(entry.get()))
        self.angle_entry.grid(row=0,column=1)
        self.velocity=StringVar()
        velocityLabel=Label(bottomframe,text='     Enter cannon power: ')
        velocityLabel.grid(row=0,column=2)
        velocity_entry=Entry(bottomframe, textvariable=self.velocity)
        velocity_entry.grid(row=0,column=3)
        self.fire_button=Button(bottomframe,text='Fire Cannon', font='optima',command=self.fireCannon)
        self.fire_button.grid(column=4,row=0,padx=50)
        self.canvas.create_line(0,600,1350,600)
        self.canvas.create_line(40,40,240,40)
        self.canvas.create_text(140,50, text='200 metres')
        self.angle.set(30)
        self.velocity.set(200)
        self.setcannon()
        self.target_man()
        
        
        
    def setcannon(self):
        #self.canvas.create_oval(20,580,40,600,width=2)
        #ypos=590-(10*cos(radians(int(self.angle.get()))))
        #xpos=30-(10*sin(radians(int(self.angle.get()))))
        #print('sin of angle =',sin(radians(int(self.angle.get()))))
        #print('xpos',xpos+30*cos(radians(int(self.angle.get()))),'ypos',ypos-30*sin(radians(int(self.angle.get()))))
        #arc at back of cannon
        #coords are upper left box and lower right box?
        #self.canvas.create_arc(xpos+15*cos(radians(int(self.angle.get()))),ypos-15*sin(radians(int(self.angle.get()))),xpos-(15*cos(radians(int(self.angle.get())))),ypos+(15*sin(radians(int(self.angle.get())))),start=90+int(self.angle.get()),extent=180,fill='orange')
        #line touching wheel
        #self.canvas.create_line(xpos,ypos,30,590,fill='red')
        #self.canvas.create_line(xpos,ypos,xpos+(50*cos(radians(int(self.angle.get())))),ypos-(50*sin(radians(int(self.angle.get())))),fill='red')
        #line parallel to ^
        #self.canvas.create_line(xpos-(15*cos(radians(int(self.angle.get())))),ypos-(15*sin(radians(int(self.angle.get())))),xpos-(15*cos(radians(int(self.angle.get()))))-50*cos(radians(int(self.angle.get()))),ypos-(15*sin(radians(int(self.angle.get()))))+(50*sin(radians(int(self.angle.get())))),fill='green')
        #last line
        #self.canvas.create_line(xpos-(50*cos(radians(int(self.angle.get())))),ypos+(50*sin(radians(int(self.angle.get())))),xpos-(15*cos(radians(int(self.angle.get()))))-50*cos(radians(int(self.angle.get()))),ypos+(15*sin(radians(int(self.angle.get()))))+(50*sin(radians(int(self.angle.get())))),fill='blue')   
        self.cannon=PhotoImage(file='cannon.gif')
        self.canvas.create_image(30,585,image=self.cannon)
    def target_man(self):
        self.xcoord=random.randrange(700,1350-16)
        self.ycoord=random.randrange(0+17,600-23)
        print(self.xcoord, self.ycoord)
        self.target=PhotoImage(file='stickman.gif')
        self.canvas.create_image(self.xcoord,self.ycoord,image=self.target)
    

    def user_input(self):
        if int(self.angle.get())>90:
            self.angle.set(90)
        elif int(self.angle.get())<0:
            self.angle.set(0)
        else:
            self.angle.set(self.angle.get())
        if int(self.velocity.get())>200:
            self.velocity.set(200)
        elif int(self.velocity.get())<50:
            self.velocity.set(50)
        else:
            self.velocity.set(self.velocity.get())
    def cannonball(self):
        sy=0.1
        sx=0.1
        t=0
        self.user_input()
        self.traj=[]
        while sy>-10 and sx<1300:
            if self.detect_hit(sx,sy)==True:
                sy=-20
                self.target_hit()
            else:
                time.sleep(0.001)
                t+=0.01
                sy=(t*int(self.velocity.get())*sin(radians(float(self.angle.get()))))-((9.81/2)*(t**2))
                sx=(float(self.velocity.get())*cos(radians(float(self.angle.get())))*t)
                #print('sx', sx+45, 'xcoord:', self.xcoord-7,'sy:', 580-sy,'ycoord: ',self.ycoord-23)
                self.trajectory=self.canvas.create_line(45+sx, 580-sy, 46+sx,581-sy)
                self.traj+=[self.trajectory]
                root.update()
        else:
            for i in self.traj:
                self.canvas.delete(i)
            self.fire_button.configure(state=NORMAL)
            
    def fireCannon(self):
        self.fire_button.configure(state=DISABLED)
        self.cannonball()

    def detect_hit(self,sx,sy):
        if self.xcoord-7<(sx+45)<self.xcoord+7:
                if self.ycoord-23<(580-sy)<self.ycoord+23:
                    return True
                    

    def target_hit(self):
        text=self.canvas.create_text(700,300, text= 'KILL SHOT', fill='red', font=("helvetica", 50))
        self.parent.update()
        time.sleep(4)
        self.canvas.itemconfig(text,state=HIDDEN)
        self.target_man()
        for i in self.traj:
                self.canvas.delete(i)
        self.fire_button.configure(state=NORMAL)

#def fireCannon():
 #   cg.cannonball()
root=Tk()
cg=cannon_game(root)
root.mainloop()
