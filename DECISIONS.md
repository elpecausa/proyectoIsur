# Decisiones de Diseño

## Refactorización de procesar_venta

Se refactorizó la función `procesar_venta()`
aplicando el principio de Responsabilidad Única (SRP).

### Problema identificado

La función original realizaba múltiples tareas:

1. Validar disponibilidad de stock.
2. Calcular subtotal y total con IGV.
3. Actualizar el stock después de la venta.

Esto concentraba varias responsabilidades
en una sola función.

### Solución aplicada

La lógica fue dividida en tres funciones especializadas:

- `validar_stock()`: verifica si existe stock suficiente.
- `calcular_total()`: calcula el monto total incluyendo IGV.
- `procesar_venta()`: coordina el flujo de la venta y actualiza el stock.

### Criterio arquitectónico utilizado

Se aplicó el principio de
**Responsabilidad Única (Single Responsibility Principle)**.

Cada función tiene una sola responsabilidad
y una única razón para cambiar.

### Beneficios

- Mayor legibilidad.
- Menor complejidad.
- Facilita pruebas unitarias.
- Permite reutilizar funciones.
- Mejora el mantenimiento del código.