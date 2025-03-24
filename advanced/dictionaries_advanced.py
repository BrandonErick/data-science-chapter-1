library = {
    "books": [
        {
            "title": "1984",
            "author": "George Orwell",
            "year": 1949,
            "genre": "Dystopian",
            "rating": 9,
            "comments": [
                {"user": "Alice", "comment": "A chilling portrayal of the future.", "date": "2022-05-01"},
                {"user": "Bob", "comment": "A must-read book!", "date": "2022-05-02"}
            ],
            "is_available": True,
            "borrowed_by": None,
            "borrow_date": None
        },
        {
            "title": "Brave New World",
            "author": "Aldous Huxley",
            "year": 1932,
            "genre": "Science Fiction",
            "rating": 8,
            "comments": [
                {"user": "Charlie", "comment": "Interesting, but too pessimistic.", "date": "2022-06-01"}
            ],
            "is_available": False,
            "borrowed_by": "Dave",
            "borrow_date": "2022-06-15"
        }
    ]
}

library["books"][0]["comments"].append({"user": "David", "comment": "Incredibly relevant to today's politics.", "date": "2022-07-01"})

library["books"][1]["rating"] = 9

library["books"][0]["is_available"] = False
library["books"][0]["borrowed_by"] = "Eve"
library["books"][0]["borrow_date"] = "2022-08-01"

del library["books"][1]["comments"][-1]

for book in library["books"]:
    if book["is_available"]:
        print(f"\nTitle: {book['title']}")
        print(f"Author: {book['author']}")
        print(f"Year: {book['year']}")
        print(f"Genre: {book['genre']}")
        print(f"Rating: {book['rating']}")
        print("Comments:")
        for comment in book["comments"]:
            print(f"  {comment['user']} ({comment['date']}): {comment['comment']}")
