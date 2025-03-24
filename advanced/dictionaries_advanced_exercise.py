# Ejercicio: Gestión de una tienda en línea
# Instrucciones:
# Crea un diccionario store que contenga una lista de productos.
# Cada producto debe ser un diccionario con las siguientes claves:
# name: nombre del producto.
# category: categoría del producto.
# price: precio del producto.
# availability: True o False, dependiendo de si el producto está disponible.
# reviews: una lista de diccionarios que contienen user, rating, y comment.
# Crea un diccionario users que contenga una lista de usuarios.
# Cada usuario debe tener un nombre, correo electrónico y una lista de productos comprados.
# Añadir funcionalidad para agregar un producto al carrito de compras de un usuario. Cada producto en el carrito debe tener name, quantity, y price.
# Crear una función para calcular el total de la compra de un usuario (precio * cantidad de productos en el carrito).
# Imprime la lista de productos y las reseñas de un producto, solo si está disponible.
# Imprime el total de la compra de un usuario después de agregar productos al carrito.

store = {
    "products": [
        {
            "name": "Laptop",
            "category": "Electronics",
            "price": 800,
            "availability": True,
            "reviews": [
                {"user": "Brandon", "rating": 9, "comment": "Great laptop for work."},
                {"user": "Erick", "rating": 8, "comment": "Fast and reliable."}
            ]
        },
        {
            "name": "Headphones",
            "category": "Electronics",
            "price": 100,
            "availability": False,
            "reviews": [
                {"user": "Juan", "rating": 7, "comment": "Good sound quality."}
            ]
        },
        {
            "name": "T-shirt",
            "category": "Clothing",
            "price": 20,
            "availability": True,
            "reviews": [
                {"user": "David", "rating": 8, "comment": "Comfortable and stylish."}
            ]
        }
    ]
}

users = {
    "user_1": {
        "name": "Brandon",
        "email": "brandon@gmail.com",
        "purchased_products": [
            {"name": "Laptop", "quantity": 1, "price": 800.00}
        ]
    },
    "user_2": {
        "name": "Erick",
        "email": "erick@outlook.com",
        "purchased_products": [
            {"name": "Laptop", "quantity": 2, "price": 800.00}
        ]
    },
    "user_3": {
        "name": "Juan",
        "email": "juan@yahoo.com",
        "purchased_products": [
            {"name": "Headphones", "quantity": 1, "price": 100.00}
        ]
    },
    "user_4": {
        "name": "David",
        "email": "david@hotmail.com",
        "purchased_products": [
            {"name": "T-shirt", "quantity": 3, "price": 20.00}
        ]
    }
}

def add_to_cart(user_id, product_name, quantity):
    product = next((product for product in store["products"] if product["name"] == product_name), None)
    if product and product["availability"]:
        total_price = product["price"] * quantity
        if user_id in users:
            users[user_id].setdefault("cart", []).append({
                "name": product_name,
                "quantity": quantity,
                "price": product["price"]
            })
            print(f"{quantity} {product_name}(s) added to {user_id}'s cart.")
            return total_price
        else:
            print(f"User {user_id} not found.")
            return None
    else:
        print(f"Product {product_name} is not available.")
        return None

total = add_to_cart("user_1", "Laptop", 2)
if total is not None:
    print("Total price:", total)
else:
    print("No products added to cart.")
