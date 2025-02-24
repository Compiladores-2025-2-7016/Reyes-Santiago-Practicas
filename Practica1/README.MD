<h1>Práctica 1: Analizadores léxicos con Lex (PLY)</h1>

<h2>Ejercicios</h2>
<h3>¿Qué ocurre si agregamos una regla simple como t_espacio = r'\ +' y nada más? (0.5 pts)</h3>
Obtenemos un ERROR: Rule 't_ESPACIO' defined for an unspecified token ESPACIO. Esto es porque siempre que se agrega una regla debemos agregar su equivalente en la lista de tokens

<h3>¿Qué ocurre si quitamos algún elemento de la lista de tokens? (0.5 pts)</h3>
En este caso obtendríamos el mismo error del ejercicio anterior

<h3>¿Cómo podemos calcular la posición en columna en caso de un error léxico? (0.5 pts)</h3>
Para este punto utilicé el atributo <code>t.lexpos</code> que proporciona la posición absoluta del caractér en el código fuente. Para obtener la posición en la que se encuentra el error opté por imprimir lo siguiente:<br>
<code>print(f"Error léxico en línea {t.lexer.lineno}, columna {t.lexpos}: '{t.value[0]}'")</code><br>
<code>- t.lexer.lineno nos proporciona la línea</code><br>
<code>- t.lexpos nos proporciona la columna</code>


<h3>¿Qué significa el valor que se aloja en t.value? (0.5 pts)</h3>
<h3>¿Qué pasa al ejecutar el programa e introducir cadenas de caracteres y de dígitos sin espacios en el archivo de entrada? (0.5 pts)</h3>
<h3>¿Qué ocurre si introducimos caracteres como "*" en el archivo de entrada? (0.5 pts)</h3>
<h3>Modificar al código anterior en un archivo nuevo, de tal manera que ejecute una acción léxica al detectar lo siguiente: (2 pts)</h3>
La expresión regular para los hexadecimales en lenguaje C.
5 palabras reservadas del lenguaje Python.
Los identificadores válidos del lenguaje Java, con longitud máxima de 32 caracteres (Sugerencia: use el operador {m,n}).
Los espacios en blanco.