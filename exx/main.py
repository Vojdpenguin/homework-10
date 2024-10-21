import json
from connect import connect_to_db
from models import Author, Quote
from mongoengine import ValidationError


def save_data():
    with open('authors.json', 'r') as authors_file, open('quotes.json', 'r') as quotes_file:
        authors_data = json.load(authors_file)
        quotes_data = json.load(quotes_file)

        authors_dict = {}
        for author in authors_data:
            for fullname in author['author']:
                try:
                    if fullname not in authors_dict:
                        author_instance = Author(fullname=fullname)
                        author_instance.save()
                        authors_dict[fullname] = author_instance
                except ValidationError as e:
                    print(f"Помилка валідації автора {fullname}: {e}")

        for quote in quotes_data:
            quote_text = quote['text']
            for author_name in authors_dict.keys():
                author_instance = authors_dict[author_name]
                try:
                    quote_instance = Quote(quote=quote_text, author=author_instance)
                    quote_instance.save()
                except ValidationError as e:
                    print(f"Помилка валідації цитати '{quote_text}' для автора {author_name}: {e}")

    print("Дані успішно збережено в MongoDB!")


if __name__ == "__main__":
    connect_to_db()
    save_data()
