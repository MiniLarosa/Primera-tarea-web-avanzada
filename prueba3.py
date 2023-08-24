def obtener_categoria(categorias, categoria_id):
    if categoria_id in categorias:
        return categorias[categoria_id]["nombre"]
    else:
        return "Categoría no encontrada"

productos = [
    {
        "id": 123,
        "nombre": "laptop",
        "precio": 1000.00,
        "categoria_id": 1
    },
    {
        "id": 124,
        "nombre": "smartphone",
        "precio": 500.00,
        "categoria_id": 1
    }
]

categorias = {
    1: {
        "id": 1,
        "nombre": "Tecnología"
    },
    2: {
        "id": 2,
        "nombre": "Electrónica"
    }
}

diccionario_resultante = []

for producto in productos:
    producto_id = producto["id"]
    producto_nombre = producto["nombre"]
    categoria_id = producto["categoria_id"]
    categoria_nombre = obtener_categoria(categorias, categoria_id)
    
    diccionario = {
        "id": producto_id,
        "nombre": producto_nombre,
        "Categoria": categoria_nombre
    }
    diccionario_resultante.append(diccionario)

print(diccionario_resultante)
