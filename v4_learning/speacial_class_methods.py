class Book:
    def __init__(self, title, author, pages):
        print("A books is created")
        self.title  = title
        self.author = author
        self.pages  = pages

    def __str__(self):
        return f"Title {self.title} and name of the author is {self.author} with number of pages {self.pages}"

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book is destroyed")

book = Book("Winning", "Tim Grover", 200)

print(book)
print(len(book))
del book
