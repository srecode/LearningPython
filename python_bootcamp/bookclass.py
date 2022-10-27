from operator import le


class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self) -> str:
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

    def __del__(self):
         print("An instance of Book deleted")
        

b = Book("Python", "Sam", 200)

print(b)
print(len(b))

# del b   

print(b)