from flask import Flask, render_template, request, redirect
from datetime import date
from pymongo import MongoClient

app = Flask(__name__)


#Conexion a la BBDD
cliente = MongoClient("mongodb+srv://afercor2806:LCrXK9Mqkj78BJY8@cluster0.t9bfnum.mongodb.net/")
db = cliente["tecknomarket"]
productos_coleccion = db["productos"]





# Datos generales
nombre_admin = "Alejandro Fernandez"
tienda = "TecnoMarket"
fecha = date.today()



#  Por defecto la pagina te redirige a inicio
@app.route("/")
def hola():
    
    return render_template("dashboard.html", 
                           nombre_admin = nombre_admin, 
                           tienda = tienda, fecha = fecha, 
                           pagina="inicio")




#Inicio
@app.route("/inicio")
def pagina_inicio():
    
    return render_template("dashboard.html", 
                           nombre_admin = nombre_admin, 
                           tienda = tienda, fecha = fecha, 
                           pagina="inicio")


#Clientes
@app.route('/clientes')
def pagina_clientes():
    pagina = "clientes"

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

    return render_template("dashboard.html", 
                           pagina = pagina,
                           clientes=clientes,
                           clientes_activos=clientes_activos,
                           cliente_top=cliente_top,)




#Pedidos
@app.route('/pedidos')
def pagina_pedidos():
    pagina = "pedidos"
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
        pagina = pagina,
        nombre_admin=nombre_admin,
        tienda=tienda,
        fecha=fecha,
        
        
        pedidos=pedidos,
        ingreso_total=ingreso_total
    )
    



#Productos
@app.route("/productos")
def pagina_productos():

    pagina = "productos"
    # Lista de productos
    productos = list(productos_coleccion.find())

    # Total de unidades en stock
    total_stock = 0
    for producto in productos:
        total_stock += producto["stock"]
    
    return render_template('dashboard.html', 
                           pagina = pagina,
                           productos=productos,
                           total_stock=total_stock
                           )



#Formulario
@app.route("/productos_nuevo", methods=["POST"])
def nuevo_producto():
    nombre = request.form.get("nombre")
    precio = float(request.form.get("precio"))
    categoria = request.form.get("categoria")
    stock = int(request.form.get("stock"))

    nuevo_producto = {
        "nombre": nombre,
        "precio": precio,
        "categoria": categoria,
        "stock": stock
    }
    #Insertar el producto nuevo en la BBDD
    productos_coleccion.insert_one(nuevo_producto)


    print(f"Nuevo producto: {nombre}, ${precio}, {categoria}, Stock: {stock}")

    return redirect("/productos")


@app.route("/productos/nuevo", methods=["GET"])
def formulario_nuevo_producto():
    return render_template("dashboard.html", 
                           pagina="productos_nuevo",
                           nombre_admin=nombre_admin,
                           tienda=tienda,
                           fecha=fecha)



if __name__ == '__main__':
    app.run(debug=True)
