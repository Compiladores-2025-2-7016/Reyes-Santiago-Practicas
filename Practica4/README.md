# Análisis de la Gramática G

## 1. Definición de la Gramática

La gramática G está definida por las siguientes producciones:

```
S  → num S'
S' → + num S' | ε
```

## 2. Conjuntos de la Gramática

- **No terminales (N):** `{ S, S' }`
- **Terminales (Σ):** `{ num, + }`
- **Producciones (P):** Como se describe arriba.
- **Símbolo inicial (S):** `S`

## 3. Análisis Predictivo LL(1)

### FIRST

- `FIRST(S)` = `{ num }`
- `FIRST(S')` = `{ +, ε }`

### FOLLOW

- `FOLLOW(S)` = `{ $ }`
- `FOLLOW(S')` = `{ $ }`

### Tabla LL(1)

|       | num         | +            | $           |
|-------|-------------|--------------|-------------|
| **S** | S → num S'  |              |             |
| **S'**|             | S' → + num S'| S' → ε      |
