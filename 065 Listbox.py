from tkinter import *

def handleSubmit():
  food = []
  for index in listbox.curselection():
    food.insert(index, listbox.get(index))
  print('Ordered Items:')
  for i in food:
    print(i)

def handleAdd():
  # print(listbox.size())
  listbox.insert(listbox.size(), entryBox.get())
  # print(listbox.size())
  listbox.config(height=listbox.size())

def handleDelete():
  for index in reversed(listbox.curselection()):
    listbox.delete(index)
  # listbox.delete(listbox.curselection())
  listbox.config(height=listbox.size())
window=Tk()

listbox = Listbox(window,
                  bg='#f7ffde',
                  font = ('Constantia',25),
                  width = 12,
                  selectmode=MULTIPLE)
listbox.pack()
listbox.insert(1,'Pizza')
listbox.insert(2,'Hotdog')
listbox.insert(3,'Coke')
listbox.insert(4,'Water')
listbox.insert(5,'Burger')
listbox.insert(6,'Pasta')
listbox.config(height = listbox.size())

submitButton = Button(window,
                text='Submit',
                command=handleSubmit)
submitButton.pack()

entryBox = Entry(window)
entryBox.pack()
addButton = Button(window,
                text='Add',
                command=handleAdd)
addButton.pack()
deleteButton = Button(window,
                      text= 'Delete',
                      command= handleDelete)
deleteButton.pack()
window.mainloop()