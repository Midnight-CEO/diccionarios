catalogo = {
    "P01": {"nombre": "Cuaderno argollado", "precio": 6500, "stock": 20},
    "P02": {"nombre": "Caja de micropuntas", "precio": 18000, "stock": 12},
    "P03": {"nombre": "Resma de papel", "precio": 15000, "stock": 8}
}


def mostrar_menu():
    print()
    print("===== CATALOGO DE LA TIENDA =====")
    print("1. Buscar producto")
    print("2. Ingresar existencias")
    print("3. Registrar producto nuevo")
    print("4. Calcular valor del inventario")
    print("5. Mostrar catálogo completo")
    print("6. Salir")


def pedir_codigo():
    codigo = input("Código del producto: ").strip().upper()
    while codigo == "":
        print("El código no puede estar vacío.")
        codigo = input("Código del producto: ").strip().upper()
    return codigo


def buscar_producto():
    codigo = pedir_codigo()
    producto = catalogo.get(codigo)

    if producto is None:
        print("AAviso: el código", codigo, "no existe en el catálogo.")
        print("Códigos disponibles:")
        for codigo_disponible in catalogo.keys():
            print("-", codigo_disponible)
    else:
        print("Código:", codigo)
        print("Nombre:", producto["nombre"])
        print("Precio: $", producto["precio"])
        print("Existencias:", producto["stock"])


def ingresar_existencias():
    codigo = pedir_codigo()
    producto = catalogo.get(codigo)

    if producto is None:
        print("Aviso: el código", codigo, "no existe en el catálogo.")
    else:
        print("Existencias actuales de", producto["nombre"], ":", producto["stock"])
        cantidad = int(input("Cantidad a ingresar: "))
        while cantidad <= 0:
            print("La cantidad debe ser mayor que cero.")
            cantidad = int(input("Cantidad a ingresar: "))

        catalogo[codigo]["stock"] = catalogo[codigo]["stock"] + cantidad
        print("Nuevas existencias:", catalogo[codigo]["stock"])


def registrar_producto():
    codigo = pedir_codigo()
    guardar = True

    if catalogo.get(codigo) is not None:
        print("El código", codigo, "ya existe:", catalogo[codigo]["nombre"])
        confirmacion = input("¿Desea sobrescribirlo? (s/n): ").strip().lower()
        while confirmacion != "s" and confirmacion != "n":
            print("Responda s o n.")
            confirmacion = input("¿Desea sobrescribirlo? (s/n): ").strip().lower()
        if confirmacion == "n":
            guardar = False
            print("Registro cancelado.")

    if guardar:
        nombre = input("Nombre del producto: ").strip()
        while nombre == "":
            print("El nombre no puede estar vacío.")
            nombre = input("Nombre del producto: ").strip()

        precio = int(input("Precio unitario: "))
        while precio <= 0:
            print("El precio debe ser mayor que cero.")
            precio = int(input("Precio unitario: "))

        existencias = int(input("Cantidad en bodega: "))
        while existencias < 0:
            print("La cantidad no puede ser negativa.")
            existencias = int(input("Cantidad en bodega: "))

        catalogo.update({codigo: {"nombre": nombre, "precio": precio, "stock": existencias}})
        print("Producto guardado.")


def calcular_valor_inventario():
    total = 0
    for producto in catalogo.values():
        total += producto["precio"] * producto["stock"]
    print("Valor total del inventario: $", total)


def mostrar_catalogo():
    print(f"{'Código':<8}{'Nombre':<24}{'Precio':>10}{'Existencias':>13}")
    print("-" * 55)
    for codigo, producto in catalogo.items():
        print(f"{codigo:<8}{producto['nombre']:<24}{producto['precio']:>10}{producto['stock']:>13}")


opcion = 0

while opcion != 6:
    mostrar_menu()
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        buscar_producto()
    elif opcion == 2:
        ingresar_existencias()
    elif opcion == 3:
        registrar_producto()
    elif opcion == 4:
        calcular_valor_inventario()
    elif opcion == 5:
        mostrar_catalogo()
    elif opcion == 6:
        print("Programa finalizado.")
    else:
        print("Opción inválida. Elija un número del 1 al 6.")
