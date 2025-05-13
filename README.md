Aplicación "TecnoMarket"

Es un panel de gestión web desarrollado con Flask que permite administrar una tienda llamada TecnoMarket. Sus funciones principales son:

    Inicio: Muestra un saludo personalizado al administrador, junto con la fecha actual.

    Productos:

        Consulta de un catálogo de productos almacenados en MongoDB.

        Visualización del stock total.

        Formulario para añadir nuevos productos.

    Clientes:

        Muestra una lista de clientes con su estado (activo/inactivo) y número de pedidos.

        Calcula cuántos clientes están activos y quién es el que ha hecho más pedidos.

    Pedidos:

        Lista de pedidos recientes con sus totales y fechas.

        Calcula el ingreso total generado por esos pedidos.

Todo el sistema está centralizado en una sola plantilla HTML (dashboard.html) que cambia dinámicamente según la sección seleccionada.
