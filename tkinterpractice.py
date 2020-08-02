# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 06:21:08 2020

@author: Rabbitking
"""

import tkinter
import tkinter.ttk
import pandas as pd

ScoreTable = pd.read_excel("D:/grade.xlsx")


ColumnsInfo = list(ScoreTable)


root=tkinter.Tk()
root.title("Student")
root.geometry("800x500+100+100")
root.resizable(False,False)

lbl=tkinter.Label(root, text='class notice')
lbl.pack()

treeview=tkinter.ttk.Treeview(root, columns=ColumnsInfo, displaycolumns=ColumnsInfo)
treeview.pack()

def CreateColumn(colindex,colname,header):
    treeview.column(colindex, width=100)
    treeview.heading(colname, text=header, anchor="center")


for i in range(len(list(ScoreTable))):
    CreateColumn(i,list(ScoreTable)[i],list(ScoreTable)[i])
    



# print(ScoreTable)
# print(ScoreTable.values.tolist()) # DataFrame에서 값들을 List(List) 형태로 만들고 싶을 때


treelist=ScoreTable.values.tolist() 


for i in range(len(treelist)):
    treeview.insert("",'end',text=i, values=treelist[i])

root.mainloop()