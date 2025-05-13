
# 🛒 Aplicación **TecnoMarket**

**TecnoMarket** es un **panel de gestión web** desarrollado con **Flask** que permite administrar de forma sencilla una tienda desde una interfaz web centralizada.

## 🔧 Funcionalidades Principales

### 🏠 Inicio
- Muestra un **saludo personalizado** al administrador.
- Visualiza la **fecha actual**.

---

### 📦 Productos
- Consulta de un **catálogo de productos** almacenados en **MongoDB**.
- Visualización del **stock total disponible**.
- Formulario para **añadir nuevos productos**.
- (En desarrollo) Funcionalidad para **eliminar productos**.

---

### 👥 Clientes
- Muestra una **lista de clientes** con:
  - Nombre y correo electrónico.
  - Estado: **activo/inactivo**.
  - Número de **pedidos realizados**.
- Cálculo de:
  - Número total de **clientes activos**.
  - Cliente con **mayor cantidad de pedidos**.

---

### 📑 Pedidos
- Lista de **pedidos recientes** con:
  - Cliente asociado.
  - Total del pedido.
  - Fecha del pedido.
- Cálculo del **ingreso total** generado por los pedidos.

---

## 💡 Estructura del Proyecto

- Toda la lógica se integra en una única plantilla HTML: `dashboard.html`.
- El contenido se actualiza dinámicamente según la sección seleccionada, gracias al uso de condicionales en Jinja2.

---

## 🧰 Tecnologías Utilizadas

- **Python + Flask** (Backend)
- **MongoDB** (Base de datos NoSQL)
- **HTML + CSS** (Frontend)
- **Jinja2** (Motor de plantillas)
