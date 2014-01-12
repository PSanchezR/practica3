#Práctica 3: Diseño de máquinas virtuales

En esta práctica la tarea que se nos pide es montar una aplicación sencilla sobre una máquina virtual completa creada por nosotros con cualquiera de los medios y herramientas vistas a lo largo de los temas, en mi caso voy a utilizar VirtualBox y Vmware ya que se manejan de forma muy sencilla y permiten cambiar las características de la maquina virtual de forma dinámica, es decir, se puede aumentar o disminuir la ram que se le asigna, el tamaño de disco o incluso el número de procesadores que utiliza y esto me va a ser muy útil ya que en ésta práctica se nos pide también ajustar las características de la máquina al servicio que ofrezcamos.

Para ajustar las características primero crearé una máquina base sobre la cuál iré aumentando o disminuyendo los datos de la configuración hasta que se ajusten a la tarea que realizará la misma de forma óptima, es decir, tendré que probar las distintas configuraciones hasta dar con una que soporte la aplicación de forma eficiente.

Lo primero que tengo que hacer es instalar VirtualBox lo cuál se hace de forma sencilla con "sudo apt-get install virtualbox", una vez instalado paso a la configuración de la nueva máquina, cómo el sistema que he escogido para ésta práctica es Ubuntu 13.10 comenzaré construyendo la máquina con los requisitos mínimos de dicho sistema:

![](https://dl.dropboxusercontent.com/u/27418257/practica%203/practica3%20-%20captura%201.png)

![](https://dl.dropboxusercontent.com/u/27418257/practica%203/practica%203%20-%20captura%202.png)

![](https://dl.dropboxusercontent.com/u/27418257/practica%203/practica3%20-%20captura%203.png)

![](https://dl.dropboxusercontent.com/u/27418257/practica%203/practica%203%20-%20captura%204.png)

![](https://dl.dropboxusercontent.com/u/27418257/practica%203/practica%203%20-%20captura%205.png)

![](https://dl.dropboxusercontent.com/u/27418257/practica%203/practica%203%20-%20captura%206.png)

![](https://dl.dropboxusercontent.com/u/27418257/practica%203/practica%203%20-%20captura%207.png)

![](https://dl.dropboxusercontent.com/u/27418257/practica%203/practica%203%20-%20captura%208.png)

Una vez finalizado el proceso de instalación de esta máquina paso a instalar los paquetes que necesito para que mi aplicación funcione, en este caso como la aplicación que voy a montar en la máquina es una pagina web siguiendo el paradigma MVC (modelo vista controlador) gestionada desde python, que maneja la api de google charts desde javascrypt, necesito todos los paquetes referentes a dichas tecnologías a parte de instalar y activar los servicios de ftp y de ssh para poder subir archivos y manejar la máquina en remoto, etc.

Como lo que se me pide en esta práctica es lo relacionado con las características de las máquinas virtuales y la eficiencia de éstas con respecto de sus características no voy a poner en este wiki las capturas de la instalación de los paquetes que necesito para mi aplicación así como las configuraciones necesarias para ello, puesto que se alargaría demasiado la extensión de este documento.


Por otra parte la configuración de la máquina virtual en vmware se hace:

![](https://dl.dropboxusercontent.com/u/27418257/practica%203/practica%203%20-%20captura%201%20vmware.png)

![](https://dl.dropboxusercontent.com/u/27418257/practica%203/practica%203%20-%20captura%202%20vmware.png)

![](https://dl.dropboxusercontent.com/u/27418257/practica%203/practica%203%20-%20captura%203%20vmware.png)

![](https://dl.dropboxusercontent.com/u/27418257/practica%203/practica%203%20-%20captura%204%20vmware.png)

![](https://dl.dropboxusercontent.com/u/27418257/practica%203/practica%203%20-%20captura%205%20vmware.png)

![](https://dl.dropboxusercontent.com/u/27418257/practica%203/practica%203%20-%20captura%206%20vmware.png)

![](https://dl.dropboxusercontent.com/u/27418257/practica%203/practica%203%20-%20captura%207%20vmware.png)

![](https://dl.dropboxusercontent.com/u/27418257/practica%203/practica%203%20-%20captura%208%20vmware.png)

Una vez creada ésta última máquina en vmware exportamos el sistema operativo de la anterior a ésta para no tener que repetir el proceso de instalación de paquetes, etc.

Ahora paso a probar la aplicación en ambos entornos virtuales, la aplicación genera un gráfico con los datos que se le introduzcan quedando de la forma:

![](https://dl.dropboxusercontent.com/u/27418257/practica%203/aplicacion%201.png)

![](https://dl.dropboxusercontent.com/u/27418257/practica%203/aplicacion%202.png)


Probada ya la aplicación y teniendo todas las configuraciones necesarias listas paso a pasarle los benchmark a ambos sistemas, los fichero de salida de los benchmark se encuentran en este mismo repositorio, en este documento sólo voy a poner los tiempos de ejecución totales de cada test para compararlos entre sí:


![](https://dl.dropboxusercontent.com/u/27418257/practica%203/tiempos.png)


Como se puede ver los tiempos son muy similares, aunque con variaciones, seguramente estas variaciones se harían mas notables si el peso de la página web a cargar fuera superior pero nos sirven para extrapolar lo que ocurriría en ese caso.

En primera instancia las máquinas con un giga de ram se diferencian en 70 milisegundos siendo la montada sobre vmware la más rápida pero cuando aumentamos a 2 gigas es la montada sobre virtualbox la que sufre una mejora mayor reduciendo su tiempo en mas de 200 milisegundos mientras que la de vmware sólo mejora alrededor de los 100 milisegundos.

Con estos resultados se puede decir que para sistemas de características muy reducidas es mejor vmware puesto que da resultados mejores con menos potencia, pero cuando la máquina está menos "estresada" los resultados son mejores en virtualbox, en mi caso ambas máquinas con un solo giga funcionan de forma lenta quedandose bloqueadas en algunas ocasiones por lo que la configuración que eligiría sería la de dos gigabytes de ram y en este caso virtualbox sería mi hipervisor elegido para llevar a cabo la puesta en marcha de mi aplicación.

