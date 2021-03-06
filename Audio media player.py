from tkinter import *
from pygame import *
import time;
import csv

root=Tk()
root.geometry("1000x500+0+0")
root.title("Song Categorisation System")

Tops=Frame(root,width=1600,bg='powder blue',relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(root,width=1600,height=700,relief=SUNKEN)
f1.pack(side=LEFT)



#f2=Frame(root,width=300,height=700,bg='powder blue',relief=SUNKEN)
#f2.pack(side=RIGHT)
#=====================TIME===============================================
localtime = time.asctime(time.localtime(time.time()))


#=======================file handling===================================
name1=[];lang1=[];genre1=[];album1=[];comp1=[];bb=[]; 
i=0;j=0
with open("D:\dsa project final\Book1.csv",'r') as file:
    reader = csv.reader(file)
    for line in reader:
        album1.append(line[3])
        lang1.append(line[1])
        name1.append(line[0])
        bb.append(line[0])
        genre1.append(line[2])
        comp1.append(line[4])
        i+=1



#==============================================================================

scroll=Scrollbar(root)
scroll.pack(side=RIGHT, fill=Y)

mylist=Listbox(root,yscrollcommand=scroll.set)

for x in bb:
    mylist.insert(END,x)
mylist.pack(side=RIGHT,fill=BOTH)
scroll.config(command=mylist.yview)



#=======================function for new gui window=========================

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

s=Stack();


def fun1():
    root2=Tk()
    root2.geometry("600x75")
    root2.title("Song details")

    Tops2=Frame(root2,width=1600,bg='powder blue',relief=SUNKEN)
    Tops2.pack(side=TOP)
    info2=Label(Tops2,font=('cambria',20,'bold'),text="For Song Details See Command Window",fg="black",bd=10,anchor='w')
    info2.grid(row=1,column=1)

    t=0
    while name1[t] != song_name.get():
        if(t==69):
            print('Data not available')
            print('***************************************')
            return
        else:
            t=t+1

    print('             Song : ' + name1[t])
    print('         Language : ' + lang1[t])
    print('            Genre : ' + genre1[t])
    print('            Album : ' + album1[t])
    print('Composers/Singers : ' + comp1[t])
    print('******************************************')

    root2.mainloop()

def fun2():
    root2=Tk()
    root2.geometry("600x75")
    root2.title("Play")

    Tops2=Frame(root2,width=1600,bg='powder blue',relief=SUNKEN)
    Tops2.pack(side=TOP)
    info2=Label(Tops2,font=('cambria',20,'bold'),text="The song is being played in the command window",fg="black",bd=10,anchor='w')
    info2.grid(row=1,column=1)

    t=0
    while name1[t] != song_name.get():
        if(t==70):
            print('Data not available')
            print('***************************************')
            return
        else:
            t=t+1
    print("Playing......")
    print('             Song : ' + name1[t])
    print('            Album : ' + album1[t])
    print('Composers/Singers : ' + comp1[t])
    l="D:\dsa project final"
    l=l+'/'+song_name.get()+'.ogg'
    mixer.init()
    mixer.music.load(l)
    mixer.music.play()
    #while mixer.music.get_busy():
        #time(10)
    s.push(name1[t])
    root2.mainloop()

def fun3():
    root2=Tk()
    root2.geometry("600x75")
    root2.title("Recently played")

    Tops2=Frame(root2,width=1600,bg='powder blue',relief=SUNKEN)
    Tops2.pack(side=TOP)
    info2=Label(Tops2,font=('cambria',20,'bold'),text="View the recently played songs in the command window",fg="black",bd=10,anchor='w')
    info2.grid(row=1,column=1)
    while s.size()!=0:
        print(s.pop())

def fun31():
    print('Stopped.........')
    print('********************************************')
    mixer.music.stop()

    

#======================Sorting Fun=================================

def  sorting():
    root3=Tk()
    root3.geometry("710x80")
    root3.title("Songs details")

    Tops3=Frame(root3,width=1600,bg='powder blue',relief=SUNKEN)
    Tops3.pack(side=TOP)
    info3=Label(Tops3,font=('cambria',20,'bold'),text="check the best songs for your mood in Command Window ",fg="steel blue",bd=10,anchor='w')
    info3.grid(row=1,column=1)

    name2=[];lang2=[];genre2=[];album2=[];comp2=[];
    name3=[];lang3=[];genre3=[];album3=[];comp3=[];
    name4=[];lang4=[];genre4=[];album4=[];comp4=[];
    e=0;q=0;g=0

    
    if(Lang.get()=='' and Genre.get()=='' and Album.get()==''):
        print("Data not available")
        print("******************************************")
        print('\n')

        
    elif(Lang.get()!='' and Genre.get()=='' and Album.get()==''):
        for i in range(0,70):
            if(lang1[i]==Lang.get()):
                genre2.append(genre1[i])
                lang2.append(lang1[i])
                name2.append(name1[i])
                album2.append(album1[i])
                comp2.append(comp1[i])
                e+=1
        for i in range(0,e):
            print('\n')
            print('             Song : ' + name2[i])
            print('         Language : ' + lang2[i])
            print('            Genre : ' + genre2[i])
            print('            Album : ' + album2[i])
            print('Composers/Singers : ' + comp2[i])
        print('******************************************')
        if(e==0):
            print("Data not available")
            print("******************************************")


    elif(Lang.get()=='' and Genre.get()!='' and Album.get()==''):
        for i in range(0,70):
            if(genre1[i]==Genre.get()):
                genre2.append(genre1[i])
                lang2.append(lang1[i])
                name2.append(name1[i])
                album2.append(album1[i])
                comp2.append(comp1[i])
                e+=1
        for i in range(0,e):
            print('\n')
            print('             Song : ' + name2[i])
            print('         Language : ' + lang2[i])
            print('            Genre : ' + genre2[i])
            print('            Album : ' + album2[i])
            print('Composers/Singers : ' + comp2[i])
        print('******************************************')
        if(e==0):
            print("Data not available")
            print("******************************************")



    elif(Lang.get()=='' and Genre.get()=='' and Album.get()!=''):
        for i in range(0,70):
            if(album1[i]==Album.get()):
                genre2.append(genre1[i])
                lang2.append(lang1[i])
                name2.append(name1[i])
                album2.append(album1[i])
                comp2.append(comp1[i])
                e+=1
        for i in range(0,e):
            print('\n')
            print('             Song : ' + name2[i])
            print('         Language : ' + lang2[i])
            print('            Genre : ' + genre2[i])
            print('            Album : ' + album2[i])
            print('Composers/Singers : ' + comp2[i])
        print('******************************************')
        if(e==0):
            print("Data not available")
            print("******************************************")
    
            
            
    elif(Lang.get()!='' and Genre.get()!='' and Album.get()==''):
        for i in range(0,70):
            if(lang1[i]==Lang.get()):
                genre2.append(genre1[i])
                lang2.append(lang1[i])
                name2.append(name1[i])
                album2.append(album1[i])
                comp2.append(comp1[i])
                e+=1
        for i in range(0,e):
            if(genre2[i]==Genre.get()):
                genre3.append(genre2[i])
                lang3.append(lang2[i])
                name3.append(name2[i])
                album3.append(album2[i])
                comp3.append(comp2[i])
                q=q+1;
        for i in range(0,q):
            print('\n')
            print('             Song : ' + name3[i])
            print('         Language : ' + lang3[i])
            print('            Genre : ' + genre3[i])
            print('            Album : ' + album3[i])
            print('Composers/Singers : ' + comp3[i])
        print('******************************************')
        if(q==0):
            print("Data not available")
            print("******************************************")
    
    elif(Lang.get()!='' and Genre.get()=='' and Album.get()!=''):
        for i in range(0,70):
            if(lang1[i]==Lang.get()):
                genre2.append(genre1[i])
                lang2.append(lang1[i])
                name2.append(name1[i])
                album2.append(album1[i])
                comp2.append(comp1[i])
                e+=1
        for i in range(0,e):
            if(album2[i]==Album.get()):
                genre3.append(genre2[i])
                lang3.append(lang2[i])
                name3.append(name2[i])
                album3.append(album2[i])
                comp3.append(comp2[i])
                q=q+1;
        for i in range(0,q):
            print('\n')
            print('             Song : ' + name3[i])
            print('         Language : ' + lang3[i])
            print('            Genre : ' + genre3[i])
            print('            Album : ' + album3[i])
            print('Composers/Singers : ' + comp3[i])
        print('******************************************')
        if(q==0):
            print("Data not available")
            print("******************************************")


    elif(Lang.get()=='' and Genre.get()!='' and Album.get()!=''):
        for i in range(0,70):
            if(genre1[i]==Genre.get()):
                genre2.append(genre1[i])
                lang2.append(lang1[i])
                name2.append(name1[i])
                album2.append(album1[i])
                comp2.append(comp1[i])
                e+=1
        for i in range(0,e):
            if(album2[i]==Album.get()):
                genre3.append(genre2[i])
                lang3.append(lang2[i])
                name3.append(name2[i])
                album3.append(album2[i])
                comp3.append(comp2[i])
                q=q+1;
        for i in range(0,q):
            print('\n')
            print('             Song : ' + name3[i])
            print('         Language : ' + lang3[i])
            print('            Genre : ' + genre3[i])
            print('            Album : ' + album3[i])
            print('Composers/Singers : ' + comp3[i])
        print('******************************************')
        if(q==0):
            print("Data not available")
            print("******************************************")



    elif(Lang.get()!='' and Genre.get()!='' and Album.get()!=''):
        for i in range(0,70):
            if(lang1[i]==Lang.get()):
                genre2.append(genre1[i])
                lang2.append(lang1[i])
                name2.append(name1[i])
                album2.append(album1[i])
                comp2.append(comp1[i])
                e+=1
        for i in range(0,e):
            if(genre2[i]==Genre.get()):
                genre3.append(genre2[i])
                lang3.append(lang2[i])
                name3.append(name2[i])
                album3.append(album2[i])
                comp3.append(comp2[i])
                q=q+1
        for i in range(0,q):
            if(album3[i]==Album.get()):
                genre4.append(genre3[i])
                lang4.append(lang3[i])
                name4.append(name3[i])
                album4.append(album3[i])
                comp4.append(comp3[i])
                g=g+1;
        for i in range(0,g):
            print('\n')
            print('             Song : ' + name4[i])
            print('         Language : ' + lang4[i])
            print('            Genre : ' + genre4[i])
            print('            Album : ' + album4[i])
            print('Composers/Singers : ' + comp4[i])
        print('******************************************')
        if(g==0):
            print("Data not available")
            print("******************************************")          


        


#====================================================================


info=Label(Tops,font=('cambria',50),text="Audio Media Player",fg="Black",bd=10,anchor='w')
info.grid(row=0,column=0)
info=Label(Tops,font=('cambria',20,'bold'),text=localtime,fg="Black",bd=10,anchor='w')
info.grid(row=1,column=0)


song_name=StringVar()
Lang=StringVar()
Genre=StringVar()
Album=StringVar()




x = Label(f1,font=('cambria',16,'bold'),text='Song Name',bd=16,anchor='w')
x.grid(row=0,column=0,sticky=E)
name = Entry(f1,font=('cambria',16,'bold'),textvariable=song_name,insertwidth=4,bd=10,bg="powder blue",justify='right')

name.grid(row=0,column=1)



y = Label(f1,font=('cambria',16,'bold'),text='Language',bd=16,anchor='w')
y.grid(row=0,column=2,sticky=E)
lang = Entry(f1,font=('cambria',16,'bold'),textvariable=Lang,insertwidth=4,bd=10,bg="powder blue")
lang.grid(row=0,column=3)


w = Label(f1,font=('cambria',16,'bold'),text='Genre',bd=16,anchor='w')
w.grid(row=1,column=2,sticky=E)
TYPE = Entry(f1,font=('cambria',16,'bold'),textvariable=Genre,insertwidth=4,bd=10,bg="powder blue")
TYPE.grid(row=1,column=3)

v = Label(f1,font=('cambria',16,'bold'),text='Album',bd=16,anchor='w')
v.grid(row=2,column=2,sticky=E)
Categ = Entry(f1,font=('cambria',16,'bold'),textvariable=Album,insertwidth=4,bd=10,bg="powder blue")
Categ.grid(row=2,column=3)


detail = Button(f1,padx=16,pady=8,bd=8,fg="black",font=('cambria',16,'bold'),width=10,
               text="Enter",bg="powder blue",command=sorting)
detail.grid(row=3,column=3)





movie = Button(f1,padx=16,pady=8,bd=8,fg="black",font=('cambria',16,'bold'),width=10,
               text="Song details",bg="powder blue",command=fun1)
movie.grid(row=1,column=1)

play = Button(f1,padx=16,pady=8,bd=8,fg="black",font=('cambria',16,'bold'),width=10,
               text="Play",bg="powder blue",command=fun2)
play.grid(row=2,column=1)

rplay = Button(f1,padx=16,pady=8,bd=8,fg="black",font=('cambria',16,'bold'),width=10,
               text="Recently played",bg="powder blue",command=fun3)
rplay.grid(row=4,column=1)

stop = Button(f1,padx=16,pady=8,bd=8,fg="black",font=('cambria',16,'bold'),width=10,
               text="Stop",bg="powder blue",command=fun31)
stop.grid(row=3,column=1)



root.mainloop()
