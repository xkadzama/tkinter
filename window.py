from tkinter import *


def print_text():
    print('Hell')

print('GIT')
root = Tk()
root.resizable(width = False, height = False)
root.geometry( '400x300')
root.title('AEIOU')
# root['bg'] = 'green'

button = Button(text='Send message', command=print_text)
button.pack(side=RIGHT)
root.mainloop()
