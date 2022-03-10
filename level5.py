from turtle import*
import keyboard

def setsc(shp, clr):
    shap = shp
    colr = clr

def start(shap, colr):

    s = 5.00 # Visina
    k = 0 # Koraci
    m = 10.2 # Maksimum visine
    n = -0.2 # Minimum nizine

    #                              !PODESIVO!
    ht(); pensize(10); speed(10); shape(shap); title('Lebdeća Kornjača')

    screensize(canvwidth=980, canvheight=720, bg="lightblue") # Pozadina

    pu(); bk(500); lt(90); fd(480); rt(90); pd() # Namjesti olovku

    color('brown'); fd(980); rt(90); fd(720); rt(90); fd(980); rt(90); fd(720) # Okvir

    #               VISINA
    pu(); rt(180); fd(240); color('red'); pd(); lt(86); fd(980) ## PRVI ZID

    #                                               VISINA
    pu(); rt(86); fd(484); rt(90); fd(978); rt(90); fd(280); rt(86); pd(); fd(982) ## DRUGI ZID

    pu(); bk(982); lt(86); fd(140); rt(90); fd(20)
    #                                                        !PODESIVO!
    speed(2); color('orange'); st(); rt(360); lt(360); pd(); color(colr)
    pensize(5); speed(0)

    
    # IGRA ZAPOČINJE
    while True:
    
        if k >= 77: # Ako je level uspješno završen
            return(True)
            break

        if keyboard.is_pressed(' '): # Ako je pritisnut razmak
            lt(68); fd(28); rt(63) # Diži korljaću
            s += 1.00
        else:
            rt(63); fd(28); lt(58) # Spuštaj kornjaću
            s += -1.00
        k += 1

        n += 0.04
        m += -0.044

        # Ako se kornjača zabije
        if s >= m:
            return(False)
            break
        elif s <= n:
            return(False)
            break
