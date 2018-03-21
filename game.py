from Tkinter import *
from dictionary import *

global i
i=0
global string
string=""

list1=["c","a","t","d","o","g","e","b","i"]

def click(ele):
    global i
    global string
    if ele not in string:
        string+=ele
    #else:

    e1.insert(i,ele)
    i+=1


def Refresh(list1):
    global i
    global string
    temp=list1[0]
    list1[0]=list1[1]
    list1[1]=list1[2]
    list1[2]=list1[3]
    list1[3]=list1[4]
    list1[4]=list1[5]
    list1[5]=list1[6]
    list1[6]=list1[7]
    list1[7]=list1[8]
    list1[8]=temp
    string=""
    i=0
    e1.delete(0, END)
    e2.delete(0, END)
    main(list1)


def isValid(string):
    if string in dict[string[0]]:
        e2.insert(0,"Valid")
    else:
        e2.insert(0,"InValid")
    main(list1)



def main(list1):

    b1=Button(window,text=list1[0],width=12,command=lambda: click(list1[0]))
    b1.grid(row=2,column=0)
    b2=Button(window,text=list1[1],width=12,command=lambda: click(list1[1]))
    b2.grid(row=2,column=1)
    b3=Button(window,text=list1[2],width=12,command=lambda: click(list1[2]))
    b3.grid(row=2,column=2)
    b4=Button(window,text=list1[3],width=12,command=lambda: click(list1[2]))
    b4.grid(row=3,column=0)
    b5=Button(window,text=list1[4],width=12,command=lambda: click(list1[4]))
    b5.grid(row=3,column=1)
    b6=Button(window,text=list1[5],width=12,command=lambda: click(list1[5]))
    b6.grid(row=3,column=2)
    b7=Button(window,text=list1[6],width=12,command=lambda: click(list1[6]))
    b7.grid(row=4,column=0)
    b8=Button(window,text=list1[7],width=12,command=lambda: click(list1[7]))
    b8.grid(row=4,column=1)
    b9=Button(window,text=list1[8],width=12,command=lambda: click(list1[8]))
    b9.grid(row=4,column=2)


    b11=Button(window,text="OK",width=10,command=lambda: isValid(string))
    b11.grid(row=6,column=0,padx=10,pady=20)

    b12=Button(window,text="REFRESH",width=10,command=lambda: Refresh(list1))
    b12.grid(row=6,column=1,padx=10,pady=20)

    b13=Button(window,text="QUIT",width=10,command=window.quit)
    b13.grid(row=6,column=2,padx=10,pady=20)

    window.mainloop()


window = Tk()
l1=Label(window,text="input String")
l1.grid(row=0,column=0)
l2=Label(window,text="Output")
l2.grid(row=1,column=0)

e1=Entry()
e1.grid(row=0,column=1)
e2=Entry(window)
e2.grid(row=1,column=1,padx=10,pady=10)

main(list1)

