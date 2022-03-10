from turtle import* 
import keyboard
import level1, level2, level3, level4, level5

shap = 'turtle'
colr = 'green'

def paste(text, size, style, sped, x, y):
    pu(); ht(); shapesize(2); goto(x, y); color('purple'); st(); speed(sped)
    write((text),move=True,font=('Arial', size, style)); ht()

def pad():
    paste('Pad!', 111, 'italic bold', 1, -200, 35)
    reset()
    start(shap, colr)

def start(shp, clr):
    global shap; global colr
    shap = shp; colr = clr
    
    ht(); pensize(10); speed(10); shape(shap); title('Lebdeća Kornjača')
    screensize(canvwidth=980, canvheight=720, bg="lightblue") # Pozadina
    ht(); paste('Razina 1...', 89, 'bold', 2, -300, 35);
    reset()
    
    if level1.start(shap, colr):
        paste('Razina Završena', 89, 'bold italic', 2, -479, 35)
        reset()
        paste('Razina 2...', 89, 'bold', 2, -300, 35)
        reset()
    else:
        pad()

    if level2.start(shap, colr):
        paste('Razina Završena', 89, 'bold italic', 2, -479, 35)
        reset()
        paste('Razina 3...', 89, 'bold', 2, -300, 35)
        reset()
    else:
        pad()

    if level3.start(shp, clr):
        paste('Razina Završena', 89, 'bold italic', 2, -479, 35)
        reset()
        paste('Razina 4...', 89, 'bold', 2, -300, 35)
        reset()
    else:
        paste('Pad!', 111, 'italic bold', 1, -200, 35)
        reset()
        paste('Razina 2...', 89, 'bold', 2, -300, 35)
        reset()
        if level2.start(shap, colr):
            paste('Razina Završena', 89, 'bold italic', 2, -479, 35)
            reset()
            paste('Razina 3...', 89, 'bold', 2, -300, 35)
            reset()
            if level3.start(shap, colr):
                paste('Razina Završena', 89, 'bold italic', 2, -479, 35)
                reset()
                paste('Razina 4...', 89, 'bold', 2, -300, 35)
                reset()
            else:
                pad()
        else:
            pad()

    if level4.start(shap, colr):
        paste('Razina Završena', 89, 'bold italic', 2, -479, 35)
        reset()
        paste('Razina 5...', 89, 'bold', 2, -300, 35)
        reset()
    else:
        paste('Pad!', 111, 'italic bold', 1, -200, 35)
        reset()
        paste('Razina 3...', 89, 'bold', 2, -300, 35)
        reset()
        if level3.start(shap, colr):
            paste('Razina Završena', 89, 'bold italic', 2, -479, 35)
            reset()
            paste('Razina 4...', 89, 'bold', 2, -300, 35)
            reset()
            if level4.start(shap, colr):
                paste('Razina Završena', 89, 'bold italic', 2, -479, 35)
                reset()
                paste('Razina 5...', 89, 'bold', 2, -300, 35)
                reset()
            else:
                pad()
        else:
            pad()

    if level5.start(shap, colr):
        paste('Razina Završena', 89, 'bold italic', 2, -479, 35)
        reset()
        paste('Igra Završena!', 89, 'bold', 1, -400, 35)
    else:
        paste('Pad!', 111, 'italic bold', 1, -200, 35)
        reset()
        paste('Razina 5...', 89, 'bold', 2, -300, 35)
        reset()
        if level5.start(shap, colr):
            paste('Razina Završena', 89, 'bold italic', 2, -479, 35)
            reset()
            paste('Igra Završena!', 89, 'bold', 1, -400, 35)
        else:
            paste('Pad!', 111, 'italic bold', 1, -200, 35)
            reset()
            paste('Razina 4...', 89, 'bold', 2, -300, 35)
            reset()
            if level4.start(shap, colr):
                paste('Razina Završena', 89, 'bold italic', 2, -479, 35)
                reset()
                paste('Razina 5...', 89, 'bold', 2, -300, 35)
                reset()
            else:
                paste('Pad!', 111, 'italic bold', 1, -200, 35)
                reset()
                paste('Razina 3...', 89, 'bold', 2, -300, 35)
                reset()
                if level3.start(shap, colr):
                    paste('Razina Završena', 89, 'bold italic', 2, -479, 35)
                    reset()
                    paste('Razina 4...', 89, 'bold', 2, -300, 35)
                    reset()
                    if level4.start(shap, colr):
                        paste('Razina Završena', 89, 'bold italic', 2, -479, 35)
                        reset()
                        paste('Razina 5...', 89, 'bold', 2, -300, 35)
                        reset()
                        if level5.start(shap, colr):
                            paste('Razina Završena', 89, 'bold italic', 2, -479, 35)
                            reset()
                            paste('Igra Završena!', 89, 'bold', 1, -400, 35)
                        else:
                            pad()
                    else:
                        pad()
                else:
                    pad()
