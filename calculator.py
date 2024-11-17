from tkinter import*

firstnu=secondnu=operator=None

root = Tk()
root.title('Calculator')
root.geometry('280x388')
root.resizable(0,0)
root.configure(background='black')

def getdi(digit):
    cur=result_lavel['text']
    new=cur+str(digit)
    result_lavel.config(text=new)

def clear():
    result_lavel.config(text='')


def getop(op):
    global firstnu,operator
    firstnu=int(result_lavel['text'])
    operator=op
    result_lavel.config(text='')

def result():
    global firstnu,secondnu,operator
    secondnu=int(result_lavel['text'])

    if operator=='+':
        result_lavel.config(text=str(firstnu+secondnu))
    elif operator=='-':
        result_lavel.config(text=(str(firstnu-secondnu)))
    elif operator=='*':
        result_lavel.config(text=(str(firstnu*secondnu)))
    elif operator=='/':
        if secondnu==0:
            result_lavel.config(text='Error')
        else:
            result_lavel.config(text=(str(round(firstnu/secondnu,2))))

result_lavel=Label(root,text='',bg='black',fg='white')
result_lavel.grid(row=0,column=0,columnspan=10,sticky='w',pady=(50,25))
result_lavel.config(font=('verdana',30,'bold'))

btn7=Button(root,text='7',bg='#00a65a',fg='white',width=5,height=2,command=lambda:getdi(7))
btn7.grid(row=1,column=0)
btn7.config(font=('verdana',14))

btn4=Button(root,text='4',bg='#00a65a',fg='white',width=5,height=2,command=lambda:getdi(4))
btn4.grid(row=2,column=0)
btn4.config(font=('verdana',14))

btn1=Button(root,text='1',bg='#00a65a',fg='white',width=5,height=2,command=lambda:getdi(1))
btn1.grid(row=3,column=0)
btn1.config(font=('verdana',14))

btn8=Button(root,text='8',bg='#00a65a',fg='white',width=5,height=2,command=lambda:getdi(8))
btn8.grid(row=1,column=1)
btn8.config(font=('verdana',14))

btn5=Button(root,text='5',bg='#00a65a',fg='white',width=5,height=2,command=lambda:getdi(5))
btn5.grid(row=2,column=1)
btn5.config(font=('verdana',14))

btn2=Button(root,text='2',bg='#00a65a',fg='white',width=5,height=2,command=lambda:getdi(2))
btn2.grid(row=3,column=1)
btn2.config(font=('verdana',14))

btn9=Button(root,text='9',bg='#00a65a',fg='white',width=5,height=2,command=lambda:getdi(9))
btn9.grid(row=1,column=2)
btn9.config(font=('verdana',14))

btn6=Button(root,text='6',bg='#00a65a',fg='white',width=5,height=2,command=lambda:getdi(6))
btn6.grid(row=2,column=2)
btn6.config(font=('verdana',14))

btn3=Button(root,text='3',bg='#00a65a',fg='white',width=5,height=2,command=lambda:getdi(3))
btn3.grid(row=3,column=2)
btn3.config(font=('verdana',14))

btnad=Button(root,text='+',bg='#00a65a',fg='white',width=5,height=2,command=lambda:getop('+'))
btnad.grid(row=1,column=3)
btnad.config(font=('verdana',14))

btnsu=Button(root,text='-',bg='#00a65a',fg='white',width=5,height=2,command=lambda:getop('-'))
btnsu.grid(row=2,column=3)
btnsu.config(font=('verdana',14))

btnmu=Button(root,text='x',bg='#00a65a',fg='white',width=5,height=2,command=lambda:getop('*'))
btnmu.grid(row=3,column=3)
btnmu.config(font=('verdana',14))

btncl=Button(root,text='C',bg='#00a65a',fg='white',width=5,height=2,command=lambda:clear())
btncl.grid(row=4,column=0)
btncl.config(font=('verdana',14))

btnze=Button(root,text='0',bg='#00a65a',fg='white',width=5,height=2,command=lambda:getdi(0))
btnze.grid(row=4,column=1)
btnze.config(font=('verdana',14))

btneq=Button(root,text='=',bg='#00a65a',fg='white',width=5,height=2,command=lambda:result())
btneq.grid(row=4,column=2)
btneq.config(font=('verdana',14))

btndi=Button(root,text='/',bg='#00a65a',fg='white',width=5,height=2,command=lambda:getop('/'))
btndi.grid(row=4,column=3)
btndi.config(font=('verdana',14))

root.mainloop()