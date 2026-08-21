class Livro():
    def __init__(self, titulo: str, autor: str, paginas: int, isbn: str):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.isbn = isbn

    def __str__(self):
        return f'titulo: {self.titulo}\nautor: {self.autor}\npaginas: {self.paginas}\nisbn: {self.isbn}'
    
    def __eq__(self, objeto):
        return self.isbn == objeto.isbn
    
objLivro1 = Livro("titulo1", "autor1", 1, "1")
objLivro2 = Livro("titulo2", "autor2", 2, "2")

objLivro1 == objLivro1
