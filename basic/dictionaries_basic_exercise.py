# Ejercicio Básico:
# Crea un diccionario con los datos de tu libro favorito. Incluye: título, autor, año de publicación y género.
# Imprime el autor de ese libro.

book = {
    "title": "Halo: New Blood",
    "author": "Matt Forbeck",
    "year": 2015,
    "genre": "Science Fiction"
}

for key, value in book.items():
    print(f"{key}: {value}")