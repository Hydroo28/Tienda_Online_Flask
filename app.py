from flask import Flask, render_template
from datetime import date

app = Flask(__name__)

@app.route('/dashboard')
def dashboard():
    # Datos generales
    nombre_admin = "Alejandro Fernandez"
    tienda = "InfoMatica"
    fecha = date.today()

    # Lista de productos
    productos = [
        {"nombre": "Ordenador Gaming", "precio": 1500.0, "stock": 5, "categoria": "Computadoras"},
        {"nombre": "Iphone 15", "precio": 800.0, "stock": 0, "categoria": "Celulares"},
        {"nombre": "Teclado Mecánico", "precio": 120.0, "stock": 10, "categoria": "Periféricos"},
        {"nombre": "Mouse Gaming", "precio": 45.0, "stock": 3, "categoria": "Periféricos"}
    ]

    # Total de unidades en stock
    total_stock = 0
    for producto in productos:
        total_stock += producto["stock"]

    # Lista de clientes
    clientes = [
        {"nombre": "Ana Torres", "email": "ana@mail.com", "activo": True, "pedidos": 4},
        {"nombre": "Luis Pérez", "email": "luis@mail.com", "activo": False, "pedidos": 1},
        {"nombre": "Marta García", "email": "marta@mail.com", "activo": True, "pedidos": 7},
        {"nombre": "Carlos Ruiz", "email": "carlos@mail.com", "activo": False, "pedidos": 0}
    ]

    # Conteo de clientes activos
    clientes_activos = 0
    for cliente in clientes:
        if cliente["activo"]:
            clientes_activos += 1

    # Cliente con más pedidos
    cliente_top = clientes[0]
    for cliente in clientes:
        if cliente["pedidos"] > cliente_top["pedidos"]:
            cliente_top = cliente

    # Lista de pedidos
    pedidos = [
        {"cliente": "Ana Torres", "total": 1500.0, "fecha": "2025-05-01"},
        {"cliente": "Marta García", "total": 240.0, "fecha": "2025-05-03"},
        {"cliente": "Luis Pérez", "total": 800.0, "fecha": "2025-04-30"},
        {"cliente": "Marta García", "total": 120.0, "fecha": "2025-05-05"}
    ]

    # Cálculo de ingreso total
    ingreso_total = 0
    for pedido in pedidos:
        ingreso_total += pedido["total"]

    return render_template(
        'dashboard.html',
        nombre_admin=nombre_admin,
        tienda=tienda,
        fecha=fecha,
        productos=productos,
        total_stock=total_stock,
        clientes=clientes,
        clientes_activos=clientes_activos,
        cliente_top=cliente_top,
        pedidos=pedidos,
        ingreso_total=ingreso_total
    )

if __name__ == '__main__':
    app.run(debug=True)
