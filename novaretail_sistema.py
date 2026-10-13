"""Sistema de ventas Nova Retail.
Este módulo contiene funciones para validar stock,
calcular totales con IGV y procesar ventas."""

def validar_stock(stock_actual, cantidad):
    """valida el stock"""
    return stock_actual >= cantidad

def calcular_total(precio_unitario, cantidad, igv_porcentaje):
    """calcula el precio total"""
    subtotal = precio_unitario * cantidad
    total = subtotal + (subtotal * igv_porcentaje)
    return total

def procesar_venta(cantidad, stock_actual, precio_unitario, igv_porcentaje):
    """pricesa la venta"""
    if not validar_stock(stock_actual, cantidad):
        return None
    total = calcular_total(precio_unitario, cantidad, igv_porcentaje)
    nuevo_stock = stock_actual - cantidad
    return total, nuevo_stock
