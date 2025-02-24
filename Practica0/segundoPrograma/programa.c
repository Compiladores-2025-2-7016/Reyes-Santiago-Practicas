#include <stdio.h>

// Anula cualquier definición externa de MULTIPLICADOR, asegurando que se use el valor por defecto.
#undef MULTIPLICADOR

// Informa al compilador que se usará el multiplicador por defecto.
#pragma message ("Usando el multiplicador por defecto; se ignorarán definiciones externas de MULTIPLICADOR.")

// Establece un nuevo número de línea y nombre de archivo para mejorar la legibilidad de los mensajes del compilador.
#line 42 "programa_final.c"

// Emite una advertencia en tiempo de compilación para notificar que se ha anulado la macro MULTIPLICADOR.
#warning "La macro MULTIPLICADOR ha sido anulada. Se usará el valor por defecto 2."

// Función que calcula el área de un círculo dado su radio.
double calcular_area(double radio) {
    return 3.141592653589793 * radio * radio;
}

int main(void) {
    double radio = 3.0;
    double area = calcular_area(radio);
    int multiplicador = 2; // Valor por defecto, garantizado por #undef y la advertencia.
    double resultado = area * multiplicador;
    
    printf("Radio: %.2f\nArea: %f\nMultiplicador: %d\nResultado: %f\n",
           radio, area, multiplicador, resultado);
    return 0;
}
