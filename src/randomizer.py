# #!/usr/bin/env python3

# RANDOMIZER FOR LAB MEETINGS
# Generates random list of meeting participants to take notes and quotes.
# Also generates a separate list for Journal Club presenters.

# Author: S Machaca, smachac2@jh.edu
# Last update: 9/24/2024

from platform import system
from tkinter import Tk, Label, Text, Button
from random import shuffle

# if system() == 'Darwin':
#     from tkmacosx import Button
# else:
#     from tkinter import Button

# create window
root = Tk()
root.title('Randomizer')
root.eval('tk::PlaceWindow . center')

# functions
def copy_nq():
    root.clipboard_clear()
    root.clipboard_append(nq_text.get('1.0','end-1c'))

def copy_jc():
    root.clipboard_clear()
    root.clipboard_append(jc_text.get('1.0','end-1c'))

def clear_input():
    entry_text.delete('1.0', 'end')
    nq_text.delete('1.0', 'end')
    jc_text.delete('1.0', 'end')

def generate():
    # prepare output text boxes
    nq_text.delete('1.0', 'end')
    jc_text.delete('1.0', 'end')
    nq_text.insert('end', 'Notes' + '\t  ' + 'Quotes' + '\n', 'underlined')

    # get and process input text
    raw_input = entry_text.get('1.0','end-1c')
    notes_list = raw_input.split()

    # randomize for Notes/Quotes
    shuffle(notes_list)

    # create quotes duty list
    quotes_list = notes_list[-2:] + notes_list[:-2]

    # print output (Notes/Quotes)
    for person in range(len(notes_list)):
        nq_text.insert('end', notes_list[person] + '\t  ' + quotes_list[person] + '\n')

    # randomize again for Journal Club
    shuffle(notes_list)

    # print output (Journal Club)
    for person in range(len(notes_list)):
        jc_text.insert('end', notes_list[person] + '\n')

# create labels and text boxes
entry_label = Label(root, text='First names:', font=('ArialBold', 14))
entry_text = Text(root, height = 16, width = 20, wrap = 'none', font=('Arial', 12))
nq_label = Label(root, text='Notes/Quotes', font=('ArialBold', 14))
nq_text = Text(root, height = 16, width = 24, wrap = 'none', font=('Arial', 12))
nq_text.tag_configure('underlined',font=('Arial', 12, 'underline'))
jc_label = Label(root, text='Journal Club', font=('ArialBold', 14))
jc_text = Text(root, height = 16, width = 16, wrap = 'none', font=('Arial', 12))

# create buttons
b1 = Button(root, text = 'Generate lists', font = ('Arial', 12), bg = 'orange', command = generate)
b2 = Button(root, text = 'Clear', font = ('Arial', 12), command = clear_input)
b3 = Button(root, text = 'Copy', font = ('Arial', 12), command = copy_nq)
b4 = Button(root, text = 'Copy', font = ('Arial', 12), command = copy_jc)
b5 = Button(root, text = 'Quit', font = ('Arial', 12), command = root.destroy)

# pack objects
entry_label.grid(row = 0, column = 0, columnspan = 1, padx = 14, pady = 4)
entry_text.grid(row = 1, column = 0, rowspan = 20, padx = 14, pady = 4, sticky = 'w')
nq_label.grid(row = 0, column = 2, columnspan = 1, padx = 14, pady = 4)
nq_text.grid(row = 1, column = 2, rowspan = 20, padx = 14, pady = 4)
jc_label.grid(row = 0, column = 3, columnspan = 1, padx = 14, pady = 4)
jc_text.grid(row = 1, column = 3, rowspan = 20, padx = 14, pady = 4, sticky = 'e')
b1.grid(row = 1, column = 1, columnspan = 1, padx = 10, pady = 0)
b2.grid(row = 2, column = 1, columnspan = 1, padx = 10, pady = 0)
b3.grid(row = 21, column = 2, columnspan = 1, padx = 10, pady = 0)
b4.grid(row = 21, column = 3, columnspan = 1, padx = 10, pady = 0)
b5.grid(row = 3, column = 1, columnspan = 1, padx = 10, pady = 0)

# auto resize window
root.update()
w = root.winfo_width()
h = root.winfo_height()
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws / 2) - (w / 2)
y = (hs / 2) - (h / 2)
root.geometry('+%d+%d' % (x, y))
root.resizable(False, False)

# main loop
root.mainloop()