<h3>En el caso de clang vamos a usar los siguientes comandos</h3>
<code>clang -E programa.c -o programa.i</code>  # Preprocesar <br>
<code>clang -Wall -S programa.i -o programa.s</code>  # Compilar a ensamblador <br>
<code>clang -c programa.s -o programa.o</code>  # Generar código objeto <br>
<code>clang programa.o -o programa</code>   # Enlazar y crear el ejecutable <br>


<h2>3. Use el siguiente comando: <code>cpp programa.c programa.i</code> Revise el contenido de <code>programa.i</code> y conteste lo siguiente:</h2>
<h3>El preprocesador recopila y expande macros y otros fragmentos de código abreviado en el programa fuente.</h3>
<p>En este caso estamos usando clang, por lo que para este punto utilizamos <code>clang -E programa.c -o programa.i</code>.</p>
<ul>
    <li>¿Qué ocurre cuando se invoca el comando cpp con esos argumentos?</li>
        <p>Este comando ejecuta la fase de preprocesamiento del archivo <code>programa.c</code> y el resultado se guarda en <code>programa.i</code>.</p>
    <li>¿Qué similitudes encuentra entre los archivos <code>programa.c</code> y <code>programa.i</code>?</li>
        <p>No logramos encontrar mucha similitud entre los archivo, el archivo <code>programa.i</code> es mucho más grande que <code>programa.c</code>.</p>
    <li>¿Qué pasa con las macros y los comentarios del código fuente original en <code>programa.i?</code></li>
        <p>Las macros condicionales, definiciones y expansiones son resueltas. En el código, dado que la macro PI está comentada, el preprocesador elige la opción del 
        <code>#else</code>. Los comentarios, tanto los de linea como los de bloque son eliminados en el archivo preprocesado. Las cabeceras estándar <code>#include<stdio.h></code>, <code>#include<stdlib.h></code> son expandidas, es decir, todo el contenido de esas cabeceras es copiado al archivo <code>programa.i</code>, por esto el archivo <code>programa.i</code> es mucho más grande.</p>
    <li>Compare el contenido de <code>programa.i</code> con el de <code>stdio.h</code> e indique de forma general las similitudes entre ambos archivos.</li>
        <p>Tienen similitudes en las definiciones de funciones estándar, como <code>printf</code>, así como en la presencia de tipos y macros estándar. Sin embargo, 
        <code>programa.i</code> también contiene el código fuente del programa original y el contenido expandido de otras cabeceras (<code>stdlib.h</code>, etc.), mientras que <code>stdio.h</code> solo define las funciones y tipos relacionados con la entrada/salida estándar. Además, las directivas de preprocesador de <code>stdio.h</code> desaparecen en <code>programa.i</code>.</p>
    <li>¿A qué etapa corresponde este proceso?</li>
        <p>Corresponde a la fase de preprocesamiento del archivo <code>programa.c</code></p>
</ul>


<h2>4. Ejecute la siguiente instrucción: <code>gcc -Wall -S programa.i</code></h2>
<h3>El compilador transforma el código preprocesado en un programa objeto en lenguaje ensamblador</h3>
<p>En este caso estamos usando clang, por lo que para este punto utilizamos <code>clang -Wall -S programa.i -o programa.s</code>.</p>
<ul>
    <li>¿Para qué sirve la opción <code>-Wall</code>?
        <p>Activa la mayoría de las advertencias durante la compilación, lo que puede mostrar mensajes sobre posibles problemas en el código.</p>
    </li>
    <li>¿Qué le indica a gcc la opción <code>-S</code>?
        <p>Indica que el compilador debe detenerse después de la fase de generación de código ensamblador.</p>
    </li>
    <li>¿Qué contiene el archivo de salida y cuál es su extensión?
        <p>Contiene el código ensamblador del programa, es decir, una representación de bajo nivel que será utilizada por el ensamblador para crear el código objeto en el siguiente paso.</p>
    </li>
    <li>¿A qué etapa corresponde este comando?
        <p>Corresponde a la etapa de generación de código ensamblador.</p>
    </li>
</ul>


<h2>5. Ejecute la siguiente instrucción: <code>as programa.s -o programa.o</code></h2>
<h3>El archivo <code>programa.s</code> es convertido en código máquina por el ensamblador.</h3>
<p>En este caso estamos usando clang, por lo que para este punto utilizamos <code>clang -c programa.s -o programa.o</code>.</p>
<ul>
    <li>Antes de revisarlo, indique cuál es su hipótesis sobre lo que debe contener el archivo con extensión <code>.o</code>.
        <p>Código máquina en formato binario</p>
    </li>
    <li>Diga de forma general qué contiene el archivo <code>programa.o</code> y por qué se visualiza de esa manera.
        <p>El archivo <code>programa.o</code> contiene código máquina y estructura binaria específica para la arquitectura y sistema operativo. Y se visualiza así porque el archivo está en formato binario, no en texto plano.</p>
    </li>
    <li>¿Qué programa se invoca con <code>as</code>?
        <p>Al ensamblador puro de GNU Binutils, parte del conjunto de herramientas de GCC. Está diseñado solo para ensamblar archivos <code>.s</code>.</p>
    </li>
    <li>¿A qué etapa corresponde la llamada a este programa?
        <p>Ejecuta la etapa de ensamblado</p>
    </li>
</ul>


<h2>6. Encuentre la ruta de los siguientes archivos en el equipo de trabajo:</code></h2>
<p><code>Scrt1.o</code>, <code>crti.o</code>, <code>crtbeginS.o</code>, <code>crtendS.o</code>, <code>crtn.o</code>.</p>
<p>Estos archivos son específicos de sistemas Linux (glibc y GCC). En su lugar, macOS utiliza archivos equivalentes que están dentro del SDK del sistema de desarrollo. Sus equivalentes más importantes en macOS son los siguientes:</p>
<ul>
    <li><code>crt1.o</code> – Equivalente a <code>Scrt1.o</code>, inicializa el entorno de ejecución antes de llamar a main.</li>
    <li><code>dylib1.o</code>, <code>bundle1.o</code>, <code>lazydylib1.o</code> – Manejan bibliotecas dinámicas y otros tipos de binarios en macOS.</li>
    <li><code>crti.o</code>, <code>crtbeginS.o</code>, <code>crtendS.o</code>, <code>crtn.o</code> no están en macOS, pero sus funciones son reemplazadas por otros archivos de inicialización.</li>
</ul>



<h2>7. Ejecute el siguiente comando, sustituyendo las rutas que encontró en el paso anterior: <code>ld -o ejecutable -dynamic-linker /lib/ld-linux-x86-64.so.2 /usr/lib/crt1.o /usr/lib/crti.o programa.o -lc /usr/lib/crtn.o</code></h2>
<p>En este caso, como estamos usando clang, vamos a ejecutar simplemente <code>clang programa.o -o ejecutable</code>.</p>

<ul>
    <li>En caso de que el comando <code>ld</code> mande errores, investigue como enlazar un programa utilizando el comando <code>ld</code>. Y proponga una posible solución para llevar a cabo este proceso con éxito.
    </li>
    <li>Describa el resultado obtenido al ejecutar el comando anterior.
        <p>En un entorno Linux el comando hace lo siguiente</p>
        <ul>
            <li><code>-dynamic-linker /lib/ld-linux-x86-64.so.2</code>: Especifica el dynamic linker del sistema Linux (cargador dinámico), responsable de cargar las bibliotecas compartidas en tiempo de ejecución.
            </li>
            <li><code>/usr/lib/crt1.o</code>, <code>/usr/lib/crti.o</code>, <code>/usr/lib/crtn.o</code>: Archivos de inicialización utilizados para preparar el entorno de ejecución. <code>crt1.o</code>: Contiene el punto de entrada (_start) del programa. <code>crti.o</code> y <code>crtn.o</code>: Contienen código para la configuración inicial y final del programa.</li>
            <li><code>programa.o</code>: El archivo de objeto que contiene el código ensamblado del programa.</li>
            <li><code>-lc</code>: Indica que se debe enlazar con la biblioteca estándar de C (libc.so), la cual contiene funciones como printf, malloc, etc.</li>
        </ul>
    </li>
    <p>El comando genera el ejecutable nombrado <code>ejecutable</code>
</ul>




<h2>8. Una vez que se enlazó el código máquina relocalizable, podemos ejecutar el programa con la siguiente instrucción en la terminal: <code>./ejecutable</code></h2>


<h2>9. Quite el comentario de la macro <code>#define PI</code> en el código fuente original y conteste lo siguiente:</h2>
<ul>
    <li>Genere nuevamente el <code>archivo.i</code>. De preferencia asigne un nuevo nombre.
    </li>
    <li>¿Cambia en algo la ejecución final?
        <p>Si, como definimos <code># define PI 3.1415926535897</code> el resultado va a ser <code># define area(r) (3.1415926535897 * r * r)</code> no <code>(3.1416 * r * r)</code></p>
    </li>
</ul>


<h2>9. Escribe un segundo programa en lenguaje C en el que agregue 4 directivas del preprocesador de C (cpp). Las directivas elegidas deben jugar algún papel en el significado del programa, ser distintas entre sí y diferentes de las utilizadas en el primer programa (aunque no están prohibidas si las requieren).</h2>
<ul>
    <li>Explique su utilidad general y su función en particular para su programa.
        <p>El programa se encuentra en la carpeta <code>segundoPrograma</code> en este mismo directorio y su utilidad está explicada en su propio <code>README.md</code>.</p>
    </li>
</ul>

<h2>Redacte un informe detallado con sus resultados y conclusiones.</h2>
<h3>CONCLUSIONES</h3>
<p>Los programas deben de pasar por un proceso complejo que muchas veces pasa por alto antes de que este pueda ser ejecutado. El usuario experimenta el proceso de compilación en cuatro fases principales:</p>
<ul>
    <li>Preprocesamiento: Se ejecutan todas las directivas del preprocesador, se expanden macros y constantes definidas, se eliminan los comentarios del código, se insertan los contenidos de los archivos de cabecera, se genera un archivo .i.</li>
    <li>Compilación: Se traduce el código fuente de C a código ensamblador, se verifica la sintaxis del código fuente, se generan advertencias y errores de sintaxis, se produce un archivo .s con instrucciones en lenguaje ensamblador.
    </li>
    <li>Ensamblado: Se convierte el código ensamblador en código máquina binario, se genera un archivo objeto .o, que contiene instrucciones en lenguaje de máquina.</li>
    <li>Enlazado: Se combinan archivos objeto y bibliotecas necesarias, se resuelven referencias a funciones externas, se genera un ejecutable listo para ejecutarse.</li>
</ul>
<p>Es común que se presenten complicaciones durante alguno de estos procesos, sin embargo, el uso de herramientas adecuadas y la comprensión de errores y advertencias mejora la eficiencia del desarrollo.</p>










