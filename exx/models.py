from mongoengine import Document, StringField, ReferenceField



class Author(Document):
    fullname = StringField(required=True)


    def __str__(self):
        return self.fullname


class Quote(Document):
    quote = StringField(required=True)
    author = ReferenceField(Author, required=True)
    def __str__(self):
        return f'"{self.quote}" - {self.author.fullname}'




