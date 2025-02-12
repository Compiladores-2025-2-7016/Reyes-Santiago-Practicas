// segundo programa, ejercicio 9 de la practica 0

#include <stdio.h>
#pragma GCC warning "Compilando este programa con advertencias activadas."

#define MAX(a, b) ((a) > (b) ? (a) : (b))

#ifndef DEBUG
    #define DEBUG 1
#endif

#ifdef DEBUG
    #define log_debug(msg) printf("DEBUG: %s\n", msg)
#else
    #define log_debug(msg)
#endif

int main(void) {
    int x = 5, y = 10;
    log_debug("Iniciando el programa.");

    printf("El máximo entre %d y %d es %d\n", x, y, MAX(x, y));
    log_debug("Programa finalizado.");

    return 0;
} 

