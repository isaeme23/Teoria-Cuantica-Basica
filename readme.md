# Teoria Cuantica Básica, Observables y Medidas
_El problema consiste en simular el primer sistema
cuantico definido en la seccion 4.1_

##**Pre-requisitos**

-Python, descargable en https://www.python.org/downloads/

-IDLE de su elección. Puede usarse el IDLE preinstalado con 
la version de python o para una mejor experiencia puede 
instalar Pycharm Community en 
https://www.jetbrains.com/es-es/pycharm/download/#section=mac
dependiendo de su sistema operativo.

##**Instalación**

Descargue los archivos observa.py y test.py y ejecutelos
en el IDLE de su elección.

##**Ejecución de pruebas**

Para las pruebas, tenemos los ejercicios planteados en la
sección 4 del libro "Quantum Computing for Computer Scientists"

En el archivo observa.py encontramos:

El sistema consiste en una partícula confinada a un conjunto 
discreto de posiciones en una línea. El simulador debe permitir 
especificar el número de posiciones y un vector ket de estado
asignando las amplitudes.

1. El sistema debe calcular la probabilidad de encontrarlo en 
   una posición en particular.
   
`Para esta simulacion se creo la funcion: Probabilities`

2. El sistema si se le da otro vector Ket debe buscar la probabilidad de transitar del primer vector al segundo.

`Para esta simulacion se creo la funcion: VecToVec`

Retos de Programación capitulo 4:

1. Sistema de la posición de la partícula en una recta. Usuario especifica el número de puntos posibles y 
   un vector ket y el sistema calcula las probabilidades de encontrar partícula en una posición. 
   El sistema puede recibir dos vectores y calcular la probabilidad de transitar de el uno al otro 
   después de hacer la observación
   
`Para este reto de programación se usaron las dos funciones anteriores.`

2. Ahora con una matriz que describa un observable y un vector ket, el sistema revisa que la matriz sea 
   hermitiana, y si lo es, calcula la media y la varianza del observable en el estado dado.
   
`Para este reto de programación se usó la funcion: Matrixket`

3. El sistema calcula los valores propios del observable y la probabilidad de que el sistema transite a 
   alguno de los vectores propios después de la observación.
   
`Para este reto de programación se usó la funcion: EigenvectorsProbability`

4. Se considera la dinámica del sistema. Ahora con una serie de matrices Un el sistema calcula el estado 
   final a partir de un estado inicial.
   
`Para este reto de programación se usó la funcion: FinalState`

_**Ejemplos:**_

Los ejercicios:

4.3.1 - Se deja como primera prueba en el archivo test.py

4.3.2 - Se deja como segunda prueba en el archivo test.py

4.4.1 - Se deja como tercera prueba en el archivo test.py

4.4.2 - Se deja como cuarta prueba en el archivo test.py

##**Ejecución de pruebas**

_Isabella Manrique, Ingenieria de Sistemas, Ciencias Naturales y Tecnologia_