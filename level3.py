from turtle import*
import keyboard

def start(shap, colr):

    s = 8.00 # Visina
    k = 0 # Koraci
    m = 16.077 # Maksimum visine
    n = -0.077 # Minimum nizine

    #                              !PODESIVO!
    ht(); pensize(10); speed(10); shape(shap); title('Lebdeća Kornjača')

    screensize(canvwidth=980, canvheight=720, bg="lightblue") # Pozadina

    pu(); bk(500); lt(90); fd(480); rt(90); pd() # Namjesti olovku

    color('brown'); fd(980); rt(90); fd(720); rt(90); fd(980); rt(90); fd(721) # Okvir

    #               VISINA
    pu(); rt(180); fd(250); color('red'); pd(); lt(87); fd(980) ## PRVI ZID

    #                                               VISINA
    pu(); rt(87); fd(484); rt(90); fd(980); rt(90); fd(250); rt(87); pd(); fd(981) ## DRUGI ZID

    pu(); bk(984); lt(87); fd(140); rt(90); fd(20)
    #                                                        !PODESIVO!
    speed(2); color('orange'); st(); rt(360); lt(360); pd(); color(colr)
    pensize(5); speed(0)

    
    # IGRA ZAPOČINJE
    while True:
    
        if k >= 81: # Ako je level uspješno završen
            return(True)
            break

        if keyboard.is_pressed(' '): # Ako je pritisnut razmak
            lt(55); fd(21); rt(55) # Diži korljaću
            s += 1.00
        else:
            rt(55); fd(21); lt(55) # Spuštaj kornjaću
            s += -1.00
        k += 1
    
        n += 0.044
        m += -0.011

        # Ako se kornjača zabije
        if s >= m:
            return(False)
            break
        elif s <= n:
            return(False)
            break
