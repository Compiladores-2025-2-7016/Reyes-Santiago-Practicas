### 1. Determina los conjuntos N, Σ y el símbolo inicial S. ###
N = {
  programa, declaraciones, declaraciones’, declaracion,
  tipo, lista_var, sentencias, sentencias’, sentencia,
  expresion
}
∑ = {
  int, float, identificador, numero, if, else, while,
  (, ), +, -, *, /, =, ;, ,
}
S = programa

### 2. Proceso de eliminación de ambigüedad o justificar, en caso de no ser necesario. ###
sentencia → if ( expresion ) sentencia | if ( expresion ) sentencia else sentencia
Es ambigüa porque else puede asociarse a múltiples if.

Podemos solucionarlo:
sentencia → if ( expresion ) sentencia else sentencia
          | if ( expresion ) sentencia_no_else
          | while ( expresion ) sentencia
          | identificador = expresion ;

sentencia_no_else → if ( expresion ) sentencia_no_else
                  | while ( expresion ) sentencia
                  | identificador = expresion ;

De esta manera el else siempre se asocia al if más cercano.

### 3. Proceso de eliminación de la recursividad izquierda o justificar, en caso de no ser necesario. ###
Pasamos de: 
declaraciones → declaraciones declaracion | declaracion
sentencias → sentencias sentencia | sentencia
lista_var → lista_var , identificador | identificador

A: 
declaraciones → declaracion declaraciones’
declaraciones’ → declaracion declaraciones’ | ε
sentencias → sentencia sentencias’
sentencias’ → sentencia sentencias’ | ε
lista_var → identificador lista_var’
lista_var’ → , identificador lista_var’ | ε

### 4. Proceso de factorización izquierda o justificar, en caso de no ser necesario. ###
No hay factores comunes al inicio de múltiples producciones 
de una misma regla, por lo tanto no es necesaria la factorización.

### 5. Nuevos conjuntos N y P ###
N = {
  programa, declaraciones, declaraciones’, declaracion,
  tipo, lista_var, lista_var’, sentencias, sentencias’,
  sentencia, sentencia_no_else, expresion
}
P = {
    programa → declaraciones sentencias

    declaraciones → declaracion declaraciones’
    declaraciones’ → declaracion declaraciones’ | ε

    declaracion → tipo lista_var ;

    tipo → int | float

    lista_var → identificador lista_var’
    lista_var’ → , identificador lista_var’ | ε

    sentencias → sentencia sentencias’
    sentencias’ → sentencia sentencias’ | ε

    sentencia → if ( expresion ) sentencia else sentencia
              | if ( expresion ) sentencia_no_else
              | while ( expresion ) sentencia
              | identificador = expresion ;

    sentencia_no_else → if ( expresion ) sentencia_no_else
                       | while ( expresion ) sentencia
                       | identificador = expresion ;

    expresion → expresion + expresion
              | expresion - expresion
              | expresion * expresion
              | expresion / expresion
              | identificador
              | numero
              | ( expresion )
}

## En el directorio img se encuentran las pruebas de ejecución del programa ##