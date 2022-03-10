from tkinter import*
import game

shap = 'turtle'
colr = 'green'

def shapeA():
    global shap
    shap='turtle'
def shapeB():
    global shap
    shap='square'
def shapeC():
    global shap
    shap='circle'
def shapeD():
    global shap
    shap='triangle'


def colorA():
    global colr
    colr='green'
def colorB():
    global colr
    colr='red'
def colorD():
    global colr
    colr='blue'
def colorE():
    global colr
    colr='black'

def enter():
    game.start(shap, colr)

root = Tk()
root.title('Lebdeća kornjača')

Canvas(root, height=0, width=520).pack()

Label(root, text='Odaberite figuricu', fg='orange', font=('Arial', 18)).pack()

Radiobutton(root, text="Kornjača", variable=shap, value='turtle', command=shapeA).pack(anchor = W)
Radiobutton(root, text="Kocka", variable=shap, value='square', command=shapeB).pack(anchor = W)
Radiobutton(root, text="Krug", variable=shap, value='circle', command=shapeC).pack(anchor = W)
Radiobutton(root, text="Trokut", variable=shap, value='triangle', command=shapeD).pack(anchor = W)

Label(root, text='Odaberite boju figurice', fg='orange', font=('Arial', 18)).pack()

Radiobutton(root, text="Zelena", variable=colr, value='green', command=colorA).pack(anchor = W)
Radiobutton(root, text="Crvena", variable=colr, value='red', command=colorB).pack(anchor = W)
Radiobutton(root, text="Plava", variable=colr, value='blue', command=colorD).pack(anchor = W)
Radiobutton(root, text="Crna", variable=colr, value='black', command=colorE).pack(anchor = W)

start = Button(root, text='Zaigraj', bg='brown', fg='white', command=enter, padx=20, pady=4)
start.pack()

Canvas(root, height=4, width=520).pack()

root.mainloop()
