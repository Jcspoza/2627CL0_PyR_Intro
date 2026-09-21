# CL0 - Presentación Taller PyR 2026 - 2027 +Demos (actualizado 26_27)

Indice evolutivo del las clases del taller + libros y webs de referencia:

[GitHub - Jcspoza/26_27Prog_RobotCMMBML_Index: Indice - Taller Programacion y Robotica 2026 - 2027 en CMM Benito Martin Lozano · GitHub](https://github.com/Jcspoza/26_27Prog_RobotCMMBML_Index)

Indice curso 25 - 26 

[GitHub - Jcspoza/2526_PyR_Index: Curso Programación y Robotica 2025 2026 - CMM BML](https://github.com/Jcspoza/2526_PyR_Index)

## Clase 0 - Indice - 90 minutos

- Requisitos de los alumnos/as
  
  - Necesarios
  
  - Deseables

- Presentación profesor – 10 minutos

- ¿Qué es la robótica?

- Enfoque: ¿Por qué Programación y Robotica simultáneamente? – 10 min

- Presentación alumnos -20 mins
  (Este es un taller personalizado para alumnos según sus intereses y formación previa => puesta en común)

- ¿Qué vamos a necesitar (minimo)?

- Clases : Contenido y plan + Formato en Web (github) + Dinámica + Reglas

- Demos

- Tabla resumen de programas

- TO DO

## Requisitos de los alumnos

Sintiéndolo mucho y para evitar que todos perdamos el tiempo, diré antes de nada, que el curso requiere unos requisitos mínimos por parte de los alumnos:

### **<u>Necesarios</u>**

#### 1- Familiaridad con los PC con Windows

Este taller requiere que tengas un manejo de un ordenador tipo PC de nivel medio, es decir debes ser capaz de:

- Escribir en programas en una aplicación de editor de texto (como un word, pero mas sencillo)

- Manejar ficheros de ordenador con windows : copiar, mover , borrar, etc.

- Navegar por la web, bajar ficheros etc.

- Conectar al puerto USB cables o pendrives y manejar los ficheros y programas dentro del pen

==> **No es necesario, pero si muy conveniente disponer de un ordenador propio preferentemente un portátil que puedas traer a las clases**. 

==> Si no tienes un portátil, te indicaré como usar un ordenador fijo con un pendrive.

#### 2- Habilidades manipulativas manuales y cognitivas mínimas

Sintiéndolo mucho, si tienes **dificultades motoras serias con las manos**, este curso no es adecuado para ti.

Mismo caso, si tienes **deterioro cognitivo severo**.

**Aceptamos sin problemas, a personas con leves problemas de memoria**:  no me importa repetir los conceptos si tu memoria no anda fina.

#### 3- No tener miedo a la electricidad a bajo voltaje

Manejaremos como máximo voltajes de 12 voltios y 1 amperio. La mayor parte del tiempo el voltaje será de 3,3 voltios o 5 voltios y la corriente del orden de decenas de miliamperios: es decir menos que inocuo 

#### 4- Inversión económica mínima

Vamos a trabajar con un microcontrolador llamado **Pico 2 W** que no proporciona el centro, y tiene un coste minimo de unos 14 -19 euros (con gastos de envio) . Además es necesario disponer de materiales electrónicos individuales, con un coste variable. Este material más el microcontrolador se han comprado otros años como kits y sale mas económico, material + microcontrolador precio 56 - 72 euros.

Para un detalle de precios, consulta al final apartado **<u>Actualización de precios de Kits y solo micro</u>**

También pueden ser necesarias algunas herramientas básicas como alicates o pelacables, o disponer de un multímetro básico. El profesor proporcionará de estas herramientas para las clases de cualquier forma

### <u>Deseables</u>

- Leer en ingles

- Haber programado con anterioridad (no importa el lenguaje)

- Manitas eléctrico

<u>**Si no crees cumplir alguno de los requisitos , te invito a quedarte para experimentar. decide si te quedas o no al final de la clase de hoy**</u>

---

## Presentación del profesor – 10 minutos

Currículo de Voluntario tecnológico del profesor [CV](./CV_JCSP_Voluntario_202607.pdf) 

## ¿Qué es la robótica?

Si  preguntáis a copilot (una IA)  diría: 

---

### 🤖 ¿Qué es la robótica?

La **robótica** es una rama de la ingeniería y la ciencia que se encarga del diseño, construcción, programación y uso de **robots**. Un robot es una máquina capaz de realizar tareas de manera automática, ya sea siguiendo instrucciones programadas o tomando decisiones por sí mismo mediante sensores e inteligencia artificial.

### 🧠 Disciplinas que combina

La robótica es un campo multidisciplinario que une varias áreas del conocimiento:

- **Ingeniería mecánica**: para construir la estructura y los mecanismos del robot.

- **Electrónica**: para controlar motores, sensores y circuitos.

- **Informática**: para programar el comportamiento del robot.

- **Inteligencia artificial**: para que el robot pueda aprender, adaptarse y tomar decisiones.

---

Yo diría que la robotica es la **ultima evolución del afán de los ser humanos por construir objetos útiles** (maquinas) **que le hagan la vida mas facil.**

La robotica **usa electricidad** tanto como **fuerza motriz** como para **comunicar informacion** entre los distintas componentes de un a maquina, como con el/los ser/es humano/s que la maneja/n

Concretando, la robotica usa:

- **sensores** (que leen informacion del mundo) 

- **actuadores** , como motores, luces calentadores etc que cambian el mundo circundandente

- dispositivos de **entrada y salida** para intercambiar informacion con los humanos, como teclados y pantallas

En todos estos dispositivos se aprovechan todos los avances de la física: electromagnetismo y cuántica principalmente, del siglo IXX al  XXI, junto con los desarrollos industriales derivados, por ejemplo el led ( las bombillas led) se basan en la física cuántica del principios del s XX y un desarrollo de ingeniería que abarco desde  el primer led en 1962, hasta el led azul de 1992 ( premio nobel 2014)

Si seguimos la definición más estándar de arriba, he de decir que **NO vamos a aprender ingeniería mecánica** en este curso de robótica. Tampoco creo que vaya a dar tiempo a aprender Inteligencia artificial. <u>Asi que nos vamos a centrar en : Electrónica e informática</u>

## Enfoque: ¿Por qué Programación y Robotica simultáneamente? – 10 min

La frontera es difusa, hay diferencias al comienzo del aprendizaje de Programación o
Robotica, que luego cuando se avanza se reducen. Lo ideal sería aprender tanto
Programación como Robótica.

| PROGRAMACION                                                                                                                                                  | ROBÓTICA                                                                                                            |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Mas Abstracto, los programas se ejecutan en un ordenador y no interactúan con el mundo salvo el teclado y la pantalla (hasta que se hacen cosas con internet) | Mos concreto, se pueden hacer "cacharros" como termostatos, estaciones meteorológicas, etc                          |
| Rápidamente se avanza a programas más complejos y más “inteligentes”                                                                                          | Los programas que se cargan en el microcontrolador son relativamente simples, aunque poco a poco se van complicando |
| No se necesita hardware para empezar (microcontrolador y materiales de robótica), salvo un PC o similar                                                       | Se NECESITA hardware para empezar: materiales de robótica y microcontrolador                                        |

En <u>programación</u>, **Python** es sin duda el lenguaje mas adecuado para aprender (en edad adulta) porque es :

- **Gratis** (al igual que su código fuente y sus bibliotecas).

- **Fácil de aprender y de usar**. Beneficia tanto a los principiantes como a los expertos.

- **Sintaxis legible**.

- **Libre** y de **código abierto** (open source).

- Amplias **bibliotecas**.

- **Creación rápida** de programas: ***es un lenguaje Interpretado***

- **Extensible e integrable** con otros lenguajes

- Funciona en los principales sistemas operativos y plataformas informáticas

Mas razones en los siguientes videos

[Video corto en castellano 1 ](https://www.tiktok.com/@edteam/video/7410916311821323526?is_from_webapp=1&web_id=7343715684931307040)

[Video corto en castellano 2](https://www.tiktok.com/@edteam/video/7410916311821323526?is_from_webapp=1&web_id=7343715684931307040)

[3 Reasons to Learn Python - AI and LLMs is One of Them, but There are MORE!](https://www.youtube.com/watch?v=EHsLuHbE_9s)

En <u>Robotica</u>, hasta hace poco tiempo había que usar para programar los microcontroladores (el cerebro de los proyectos de robotica), lenguajes relativamente oscuros como "C" o derivadas de C ( IDE Arduino) . Afortunadamente, en 2013 el físico Australiano Damien George, desarrollo junto a otros personas **micropython** para el microcontrolador PyBoard, y rápidamente se ex- "porto" a otros microcontroladores como ESP32 o **RPI Pico, que es el que usaremos**

**Micropython** es una implementación del lenguaje de programación Python 3, escrita en C, optimizada para poder ejecutarse en un microcontrolador. Es decir **permite programar los microcontroladores con "programas" escritos en un sub-conjunto de Python con alguna peculiaridad del microcontrolador** por lo que son aplicables todas las ventajas de Python

***En este curso se aprende simultáneamente Python y microPython con lo cual el aprendizaje se realimenta y multiplica***

## Presentación alumnos -20 mins

Es el momento de conocernos un poco, porque este es un taller personalizado para alumnos según sus intereses y formación previa 

--> Hagamos una puesta en común de 20 mins

## ¿Qué vamos a necesitar (minimo)?

Resumen:

1. PC portátil / pendrive con un IDE cargado

2. Microcontrolador Raspberry Pico 2 W o W

3. Material electrónico vario como protoboard, cables, sensores etc.
   
    Se recomienda comprar en conjunto el microcontrolador y el material electrónico en un KIT 

Detalle:

*Herramientas SW* : <u>**IDE:**</u> Para programar **tanto en Python como en micropython** vamos usar **<u>Thonny</u>** que es un IDE: Entorno integrado de Desarrollo. Es gratis y solo necesitamos instalarlo en un **PC o en un pendrive** : lo contaremos en la clase 1.

NOTA : **los alumnos de otros años anteriores, han optado por traer a clase un PC portátil** 

*Herramientas HW*: **<u>Microcontrolador</u>**: ya hemoos comentado que es como el cerebro de todos los proyectos de robotica, es también donde se conectan todos los sensores, displays, etc. El **año pasado decidimos usar el microcontrolador <u>Raspberry Pi Pico W</u>** 

Seguiremos con él el curso 2024 - 2025, pero **a los nuevos alumnos se les recomendara usar la versión nueva <u>Raspberry Pico 2W</u>**, porque el precio es aproximadamente el mismo, es mucho mas potente y ya no se encuentra la Pico 1 w.  Lo ideal es comprar un kit, pero se puede empezar solo con el microcontrolador + una Protoboard y algunas cosas (muy baratas) más. Comentaremos este tema en próximas clases. 

Lo ideal es comprar un kit, pero se puede empezar solo con el microcontrolador + una Protoboard y algunas cosas (muy baratas) más.

## Clases : Contenido y plan + Formato en Web (github) + Dinámica + Reglas

### Contenido y Plan de clases

1. Las clases tendrán **unidad temática** con la idea de explicar y practicar en 1 clase

2. Si el contenido lo requiere, una unidad temática podrá darse en 1, 2 o máximo 3 sesiones

3. El plan de clases a 2 clases vista estará disponible en la pagina indice
   
   Indice evolutivo del las clases del taller + libros y webs de referencia:
   
   [GitHub - Jcspoza/26_27Prog_RobotCMMBML_Index: Indice - Taller Programacion y Robotica 2026 - 2027 en CMM Benito Martin Lozano · GitHub](https://github.com/Jcspoza/26_27Prog_RobotCMMBML_Index)

4. El plan a partir de  la 2da o 3ra clases **se adaptara y acordará con los alumnos**, es decir el programa de clases se ira concretando y adaptando a los alumnos. Hay mucho material de años anteriores cubriendo un amplio abanico de complejidad, desde lo mas sencillo a lo mas complejo

5. Habrá clases dedicadas completa o parcialmente a resolver dudas o ver montajes hechos en casa de los alumnos, ...

### Formato en Web (github)

Las clases se publicaran en web en un repositorio llamado **Github**, bajo la raíz

[Jcspoza (Jose Carlos Santamaria Poza) · GitHub](https://github.com/Jcspoza)

En cada mini-web habrá 3 tipos de archivos 

* readme.md : es donde esta el desarrollo de la clase en un lenguaje llamado markdown. Es opcional bajarlo, porque siempre se puede leer en la web. Si lo bajáis hay muchos conversores y visores
* xxxx.py : son archivos de programas tanto de python como de micropython **==> Esta es la única parte que es imprescindible copiar a vuestro PC o pendrive**
* imágenes y esquemas o fichero gráficos  similares que estarán en una carpeta llamada 'doc' o similar
* xx.pdf libros o similares si no se encuentran con facilidad. Estarán en un directorio 'por debajo' llamado 'doc'

Para copiar los programas y algun otro material, hay 2 opciones

* bajar la web entera en formato zip

* baja cada fichero 1 a 1
  
  **==> Se explicará durante la clase inicial**

### Dinámica

1. Las clases se publicaran en internet antes de ser impartidas (como es el caso de esta clase) y tendrán unidad temática.

2. La duración será de 1.5 horas, con la siguiente distribución, tentativamente:
   
   1. Teoría o similar :30 min
   
   2. Demos de profesor : 30 min
   
   3. Trabajo de lo alumnos/as : montaje , probar los programas en sus uC, etc

3. Se trabajara individualmente en principio, cada alumno con su propio material, salvo excepción.

4. Los programas de python o micropython usados en cada clase estarán disponibles en la pagina web de esa clase en una tabla ***[Tabla resumen de programas](https://github.com/Jcspoza/2526CL0_PyR_Intro#tabla-resumen-de-programas)***

5. **Robotica**: La idea es que el prototipo robótico se construya por cada alumno/a durante la/s clase/s y que se entienda el funcionamiento del programa en microPyton

6. **Programación**: Los conceptos de programación en Python se probaran por cada alumno/a en durante la clase con el interprete si son comandos simples , o con pequeños programas ejemplo , en ambos casos indicados en la documentación de la clase

7. **Programación**: Los programas mas complejos serán explicados en clase y se pedirá como trabajo de 'casa', hacer algun pequeño cambio en el programa y ver los efectos.

8. Se dispone de una pagina web Indice de las clases y de contenido general como libros/webs de referencia, que ira evolucionado durante el curso 

9. [GitHub - Jcspoza/26_27Prog_RobotCMMBML_Index: Indice - Taller Programacion y Robotica 2026 - 2027 en CMM Benito Martin Lozano · GitHub](https://github.com/Jcspoza/26_27Prog_RobotCMMBML_Index)

### Reglas de funcionamiento

1. Se llevara control de las faltas porque lo exigen las reglas del CMM
2. Se dispondrá de un grupo de WA para avisos e info relacionada con la programación o robotica. Se ruega NO publicar contenidos ajenos
3. Se ruega avisar por WA de las ausencias caso de no haberlo avisado con antelación

---

## Demos

### Demo de Robotica : Tira Led (x8) de colores controlada por display, pulsadores y botón rotativo

He preparado sobre un montaje con el que acabamos el curso anterior de un 'display' mas 3 pulsadores y botón de rueda . he añadido una tira neopixel de ledes de colores controlables individualmente ( también vista el curso pasado)

[Tira 8 led de colores y control con display](./Rdemo_neopx8_showMenu_2_0.py)

### Demo de Programación : Juego 'Mata-puntos'

Es del curso 2023 a 2024, incluye programación grafica ( sencilla) . es un juego que podría servir para evaluar las habilidades de manejo del ratón de ordenador : 

    Se trata simplemente de clicar en los puntos rojos ( bastante grandes) que aparecen en pantalla, y que van aumentando su velocidad de aparición, hasta ver cuantos puedes 'matar'

[Juego Mata puntos](./Pdemo_MataPuntos_GZch7_2_0.py)

## Tabla resumen de programas

| Programa                                                                      | Lenguaje                    | HW si Robotica y Notas                                                                                                                           | Objetivo de Aprendizaje   |
| ----------------------------------------------------------------------------- | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------- |
| [Tira 8 led de colores y control con display](./Rdemo_neopx8_showMenu_2_0.py) | micropython (uPython, o uP) | Display SH1106 I2C GPIO4&5 + Tira neopixel en GPIO15 + REncoder GPIO16/17 + 3switch 18,19 20                                                     | Programa demo de robotica |
| [Juego Mata puntos](./Pdemo_MataPuntos_GZch7_2_0.py)                          | Python                      | Libreria: 'guizero'. Programa ejemplo del libro [Create Graphical User Interfaces with Python](https://github.com/themagpimag/createguis)- cap 7 | Programa demo de  Python  |

---

## Actualización de precios de Kits y solo micro

### Kits pico 2w

- [Aliexpres Freemove con PICO 2  W 56 eur](https://www.aliexpress.com/p/tesla-landing/index.html?_immersiveMode=true&scenario=c_ppc_item_bridge_gmv&productId=1005004336772445&src=google&aff_short_key=_c3iN9Lxl&withMainCard=true&aff_platform=true&isdl=y&traffic_server_nav=true&key=_3in1&src=google&albch=shopping&acnt=752-015-9270&isdl=y&slnk=&plac=&mtctp=&albbt=Google_7_shopping&aff_platform=google&aff_short_key=_c3iN9Lxl&gclsrc=aw.ds&&albagn=888888&&ds_e_adid=776106029446&ds_e_matchtype=search&ds_e_device=c&ds_e_network=g&ds_e_product_group_id=2440549163942&ds_e_product_id=es1005004336772445&ds_e_product_merchant_id=5660123851&ds_e_product_country=ES&ds_e_product_language=es&ds_e_product_channel=online&ds_e_product_store_id=&ds_url_v=2&albcp=23060876789&albag=186920513438&isSmbAutoCall=false&needSmbHouyi=false&gad_source=1&gad_campaignid=23060876789&gbraid=0AAAAA_eFwRChESAFBatUkAX8xwmuP4zIQ&gclid=Cj0KCQjw0Y3HBhCxARIsAN7931XtuIIu_pNjkdboq6rrK_G82yOxTrVqLatZyvxQOE3jfQlkRxciFyoaAuS4EALw_wcB)     Tutorial detallado de 767 páginas en total

- [Amazon Freemove ultimate con  PICO 2 w 64](https://www.amazon.es/Freenove-Raspberry-Compatible-Tutoriales-Detallados/dp/B0DR2GDKJ4?ref_=ast_sto_dp&th=1)

- [Sunfounder Ultimate Pico 2W](https://www.sunfounder.com/collections/pico-w-pico/products/raspberry-pi-pico-ultimate-starter-kit-euler-copy) en su propia tienda 65 eur +  gastos

- [Amazon Sunfounder Ultimate  Pico 2W](https://www.amazon.es/SunFounder-Raspberry-tutoriales-MicroPython-compatible/dp/B0DYJ6L46J/ref=sr_1_1?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3UNVEJGK2SDYS&dib=eyJ2IjoiMSJ9.BO4h1OeAL0vD6sE_ov98RA.jeDkE1VaXDdJUqMa04r3J4BLnrh5LmzWMyZh-RxgahY&dib_tag=se&keywords=Sunfounder+Ultimate+Pico+2W&qid=1759772400&s=electronics&sprefix=sunfounder+ultimate+pico+2w%2Celectronics%2C64&sr=1-1) - 72  eur con gastos incluidos

### Pico 2W NO kit

- [Raspberry Pi Pico 2WH - kubii  9+4 eur](https://www.kubii.com/es/microcontroladores/4377-2357-raspberry-pi-pico-2-2w-2h-2wh-3272496319394.html#/version_pico-pico_2_wh)

- [Raspberry Pico 2wh - Tiendatec 9+5](https://www.tiendatec.es/raspberry-pi-pico/2423-1403-raspberry-pi-pico-2-w.html#/250-version-con_pines_presoldados)

- [Amazon : 19 eur - Waveshare  Pi-Pico-2-W-M Package, RPi Official Pico 2 W Microcontroller Board with  Pre-Soldered Header (Mono), RP2350 Chip, Dual-Core & Dual-Architecture Design, Supports WiFi & BT5.2](https://www.amazon.es/dp/B0DP42Q5K5/ref=sspa_dk_hqp_detail_aax_0?psc=1&sp_csd=d2lkZ2V0TmFtZT1zcF9ocXBfc2hhcmVk)

### Informacion y Comparación Pico W vs Pico 2W

[Pico-series Microcontrollers - Raspberry Pi Documentation](https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html#pico-2-family)

[Get Started Raspberry Pi Pico 2 and Pico 2 W | Random Nerd Tutorials](https://randomnerdtutorials.com/getting-started-raspberry-pi-pico-2-w/)

[VIDEO- Raspberry Pi Pico 2 W más POTENTE y capaz que nunca.  Intro](https://youtu.be/W8A2qDFkfEw?si=m5sNF7x4ACZvfTOu) - ver solo hasta el minuto 8

## TO DO :

- Funciones complejas de Neopixel como secuencia, ejecutarlas con interrupciones y timers, para que sean independientes del programa ( sin display por simplicidad) 
- Funciones complejas de Neopixel como secuencia, ejecutarlas con interrupciones y timers, para que sean independientes del programa ( CON display y resto menús)w
