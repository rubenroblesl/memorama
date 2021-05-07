from random import *
from turtle import *
from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
tiles = ['Acura', 'Alfa Romeo','Audi', 'BMW','Bentley', 'Buick','Chevrolet', 'Chrysler','Dodgle', 'Fiat','Ford', 'GMC','Genesis', 'Honda','Hyundai', 'Infiniti','Jaguar', 'Jeep','Kia', 'Land Rover','Lexus', 'Lincoln','Lotus', 'Maserati','Mazda', 'Mercedes-Benz','Mercury', 'Mini','Mitsubishi', 'Nissan','Pontiac', 'Porsche']
tiles = tiles * 2
state = {'mark': None}
hide = [True] * 64
taps = 0


def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    global mark, taps
    
    # imprime las coordenadas donde se dio el click
    print(x,y)
    
    taps = taps + 1
    
    
    "Update mark and hidden tiles based on tap."
    # retorna el indice correspondiente a (x,y) en tiles[spot]
    spot = index(x, y)
    
    # saca el valor de state - al inicio es None
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        #cambia el estado a la carta que se le dio click
        state['mark'] = spot
    else:
        # Son pares ( visibles )
        hide[spot] = False
        hide[mark] = False
        
        # mark se regresa a none
        state['mark'] = None

def draw():
    global mark
    "Draw image and tiles."
    # clear window
    clear()
    
    # move turtle 0,0
    goto(0, 0)
    
    #carga la imagen del coche
    shape(car)
    stamp()
    
    # cartas escondidas al principio
    contador = 0
    for count in range(64):
        # si la carta esta cerrada es True
        if hide[count]:
            # calcula esquina inf. izq para dibujar carta
            x, y = xy(count)
            # dibuja un square en x,y en esq inf izq
            
            # dibuja valor de la casilla
            contador = contador + 1

    mark = state['mark']
    
    # Si estado no es none y la carta no visible
    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        #despliega en esa posicion x + 2 y el numero de la carta escondida
        write(tiles[mark], font=('Arial', 30, 'normal'))
    
    escondidas = hide.count(True)
    
    #si ya encontraron todo
    if escondidas == 0:
        up()
        goto(-140,150)
        color('white')
        write('GANASTE UN AUTO', font=('Arial', 30, 'normal'))
        goto(-100,100)
        color('white')
        write('FELICIDADES!!', font=('Arial', 30, 'normal'))
        goto(-100,50)
        color('white')
        write(f'Hiciste {taps} taps', font=('Arial', 30, 'normal'))
        return
    
    # show window
    update()
    # call draw
    ontimer(draw, 100)
    

# shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
