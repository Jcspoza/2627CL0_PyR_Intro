# Taller Programación y Robótica en CMM BML – 2025 -2026 - Clase 0
# Programa: DEMO neopixel x8 con show menu en sh1106
# Hardware platform: Pico _ & W / funciona igual sin cambios
# Librerias : sh1106.py, rotary_irq_rp2, 
# Ref librerias: https://github.com/robert-hh/SH1106
# Fecha JCSP 2025 09 12
# Licencia : CC BY-NC-SA 4.0
# Programa base para hacer otros con Display sh1106 + Rotary encoder + 3 switchs


from os import uname
# Informative block - start
p_keyOhw = "Neopx x8 GPIO15 + SH1106 I2C GPIO4&5+ RE GPIO16/17 + 3switch 18,19 20"
p_project = "DEMO neopixel x 8 using show menu bbase prog"
p_version = "2.0"
p_library = "neopixel"
print(f"uPython version: {uname()[3]} ")
print(f"uC: {uname()[4]} - Key other HW: {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
print(f"Key Library: {p_library}")

from machine import Pin, I2C
import sh1106
# import array # necesario para coor de poligonos 
import time
from rotary_irq_rp2 import RotaryIRQ
from writer import Writer
# Font
import inkfree20 as font
from neopixel import NeoPixel

# 0.0 - Constates y varaibles globales
WIDTH =128 
HEIGHT= 64
FREQ = 400_000   # Try lowering this value in case of "Errno 5"
# we use the same brightness for each color
brillo = 100
delay = .2

# here we define variables for each color
red = (brillo, 0, 0)
green = (0, brillo, 0)
blue = (0, 0, brillo)
yellow = (brillo, brillo, 0)
whitelow = (15,15,15)
apagado = (0, 0, 0)

# 0.1- los 2 pines del Rotary Encoder, si el incremento es decremento -> invertir
TRA = 16
TRB = 17

# 0. 1 Definition de los 3 switchs
listaPul = ['confirm', 'back', 'push']

CONFIRM = 18
BACK = 19
PUSH = 20
confPul = Pin(CONFIRM, Pin.IN) # pull up por circuito
backPul = Pin(BACK, Pin.IN) # pull up por circuito
pushPul = Pin(PUSH, Pin.IN) # pull up por circuito

# 0.3 Configura interrupciones asociadas a los pulsadores
teclas = [] # guarda las teclas presionadas
last_time = 0 # guarda la ultima marca de tiempo en que se presiono el pulsador

def manejaPulsadores(pin):
    
    global teclas, last_time
    new_time = time.ticks_ms()
    # Si ha pasado mas de 200ms desde el ultimo evento, temenos un nuevo evento. Evita los REBOTES
    if time.ticks_diff(new_time, last_time) > 400: 
        teclas.append(listaPul[int(str(pin).split(",")[0][8:]) - CONFIRM])
        # Si la interrupcion vien del pulsador 'back' en GPIO19
        # objeto 'pin' devuelve por ejemplo 'Pin(GPIO19, mode=IN)' si lo pasamos a str
        # slip(",") parte por la coma en una lista ['Pin(GPIO19', ' mode=IN)']
        # [0][8:] toma del primero de la lista los caracteres del 8 al final, y lo pasa a int
        # 'Pin(GPIO19'[8:] -> '19'
        # y resta el valor de CONFIRM = 18 , dando 1
        # busca en listaPul[1] => 'back'
        last_time = new_time
        
confPul.irq(trigger=Pin.IRQ_FALLING, handler=manejaPulsadores)

backPul.irq(trigger=Pin.IRQ_FALLING, handler=manejaPulsadores)

pushPul.irq(trigger=Pin.IRQ_FALLING, handler=manejaPulsadores)

# MENU - definicion de procedimientos que ejecutan cada opcion del menu
def Secuencia_Roja():
    """Color rojo en secuencia"""
    
    tira.fill(apagado)
    tira.write()
    for i in range(0, NUMERO_PIXELS-1):
        tira[i] = red
        tira.write()
        time.sleep(delay) 
        tira[i] = whitelow
        
    tira[NUMERO_PIXELS-1] = red
    tira.write()     
    return "Secuencia Rojo"

def Secuencia_Verde():
    """Color verde en secuencia"""
    
    tira.fill(apagado)
    tira.write()
    for i in range(0, NUMERO_PIXELS-1):
        tira[i] = green
        tira.write()
        time.sleep(delay) 
        tira[i] = whitelow
        
    tira[NUMERO_PIXELS-1] = green
    tira.write()     
    return "Secuencia Verde"

def Secuencia_Azul():
    """Color azul en secuencia"""
    
    tira.fill(apagado)
    tira.write()
    for i in range(0, NUMERO_PIXELS-1):
        tira[i] = blue
        tira.write()
        time.sleep(delay) 
        tira[i] = whitelow
        
    tira[NUMERO_PIXELS-1] = blue
    tira.write()     
    return "Secuencia Azul"

def Secuencia_Amar():
    """Color Amarillo en secuencia"""
    
    tira.fill(apagado)
    tira.write()
    for i in range(0, NUMERO_PIXELS-1):
        tira[i] = yellow
        tira.write()
        time.sleep(delay) 
        tira[i] = whitelow
        
    tira[NUMERO_PIXELS-1] = yellow
    tira.write()     
    return "Sec. Amarillo"

def Secuencia_Multi():
    """Gradacion de colores"""
    gradacionCol = ((250,0,0),
                    (160,80,0),
                    (80,160,0),
                    (0,250,0),
                    (0,160,80),
                    (0,80,160),
                    (0,0,250),
                    (100,100,100))
    
    tira.fill(apagado)
    tira.write()
    for i in range(0, NUMERO_PIXELS):
        tira[i] = gradacionCol[i]
        tira.write()
        time.sleep(delay)       
    
    return "Multicolor"

MENU = [[Secuencia_Roja, 'Rojo en sec.'],
        [Secuencia_Verde, 'Verde en sec.'],
        [Secuencia_Azul, 'Azul en sec.'],
        [Secuencia_Amar, 'Amarillo en sec.'],
        [Secuencia_Multi, 'Gradacion color']]

# FIN MENU

# 0.1 Objeto I2C y LCD
i2c = I2C(0, sda = Pin(4), scl = Pin(5), freq = FREQ)
print('Info del bus i2c: ',i2c)

oledsh = sh1106.SH1106_I2C(WIDTH, HEIGHT , i2c, addr = 0x3c, rotate = 0) # constructor - I2C direccion 3C por defecto
oledsh.sleep(False)

#0.2- Creacion  del objeto RE
rotary = RotaryIRQ(
    pin_num_clk=TRB,
    pin_num_dt=TRA,
    min_val=0,
    max_val=(len(MENU)-1),
    reverse=False,
    incr=1,
    range_mode=RotaryIRQ.RANGE_WRAP,
    # pull_up=True, # si pull up por circuito -> comenta
    half_step=False,
    )
# 0.3 Creacion del objeto writer
wri = Writer(oledsh, font, verbose = False) # verbose = False to suppress console output

# 0.4 Creacion del objeto neopixel
NUMERO_PIXELS = 8
NEOPIXEL_PIN = 15
tira = NeoPixel(Pin(NEOPIXEL_PIN),NUMERO_PIXELS )
tira.fill(apagado)
tira.write()

# 1- Programa Principal - Presentacion
oledsh.fill(0) # clear screen
oledsh.show()

oledsh.fill(0)
oledsh.text("Demo", (WIDTH - len("Demo")*8) // 2, 0)
oledsh.text("de Neopixel 8 y", (WIDTH - len("de Neopixel 8 y")*8) // 2, 16)
oledsh.text("Display i2c b/n", (WIDTH - len("Display i2c b/n")*8) // 2, 32)
oledsh.text("version " + p_version, 0, 44)
msgL8 = "Tecla->comenzar"
oledsh.text(msgL8, (WIDTH - len(msgL8)*8) // 2, 55, 1)
oledsh.show()
while True:
    #utime.sleep(1)
    if teclas != []:        
        teclas = []
        oledsh.fill(0)
        oledsh.show()
        break

opcion = rotary.value()

try:
    while True:
        oledsh.fill(0)
        oledsh.text("Test de Menus",0,0,1)
        Writer.set_textpos(oledsh, 16, 8)
        msgL4 = MENU[opcion][1]
        wri.printstring(msgL4)        
        msgL7 = 'Ver->Confirm'
        oledsh.text(msgL7, (WIDTH - len(msgL7)*8) // 2, 45, 1)
        msgL8 = 'Apagar->Back'
        oledsh.text(msgL8, (WIDTH - len(msgL8)*8) // 2, 55, 1)        
        oledsh.show(True) # hace que se actualicen todas las paginas, si no no funciona
        opcion = rotary.value()
        
        if teclas != [] and teclas[0] == 'back': # sale del programa
            teclas = []
            raise KeyboardInterrupt
        
        if teclas != [] and teclas[0] == 'confirm':
            teclas = []
            oledsh.fill(0)
            orden = MENU[opcion][0]
            msgL1 = orden()
            msgL8 = 'Volver->Back'
            oledsh.text(msgL1, (WIDTH - len(msgL1)*8) // 2, 0, 1)
            oledsh.text(msgL8, (WIDTH - len(msgL8)*8) // 2, 55, 1)
            oledsh.show(True) # hace que se actualicen todas las paginas, si no no funciona
            while not('back' in teclas):
                pass
            teclas = []
                                                      
except KeyboardInterrupt: #  si CTRL+C se presiona - > limpiar display
    tira.fill(apagado)
    tira.write()
    oledsh.fill(0)
    oledsh.show()

