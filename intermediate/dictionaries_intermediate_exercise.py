# Ejercicio Intermedio:
# Crea un diccionario con la información de tu libro favorito. El diccionario debe incluir las siguientes claves:
# title (título del libro)
# author (autor del libro)
# year (año de publicación) 
# genre (género del libro) 
# rating (calificación del libro de 1 a 10)
# is_read (booleano que indique si ya has leído el libro)
# Imprime el título y el autor del libro.
# Modifica el campo rating para reflejar tu calificación actual del libro.
# Añade un campo adicional que indique si recomendarías el libro (recommendation), y asigna el valor True o False.
# Agrega un nuevo campo review donde puedes escribir una breve reseña sobre el libro.
# Elimina el campo is_read, ya que ya no te interesa esa información.
# Modifica el año de publicación del libro para que sea más reciente, si es necesario.
# Imprime toda la información del libro utilizando un ciclo for que recorra el diccionario. 
# Añade un nuevo campo publisher con el nombre de la editorial que publicó el libro.
# Imprime solo los valores de las claves title, author, y rating.

book = {
    "title": "Halo: The Fall Of Reach",
    "author": "Eric Nylund",
    "year": 2001,
    "genre": "Sci-Fi",
    "rating": 9,
    "is_read": True
}

print("Title:", book["title"],
      "\nAuthor:", book["author"])

book["rating"] = 10

book["recommendation"] = True

book["review"] = "This book is a must-read for Halo fans!"

del book["is_read"]

print("\nHalo Volume 1: The Fall Of Reach")
for key, value in book.items():
    print(f"{key}: {value}")

book["publisher"] = "Del Rey Books"

print("\nTitle:", book["title"],
      "\nAuthor:", book["author"],
      "\nRating:", book["rating"])


