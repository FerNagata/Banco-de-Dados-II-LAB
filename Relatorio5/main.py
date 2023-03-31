from database import Database
from writeAJson import writeAJson
from booksModel import BookModel
from cli import BookCLI

db = Database(database="relatorio_05", collection="livros")
# db.resetDatabase()
bookModel = BookModel(database=db)

bookCLI = BookCLI(bookModel) 
bookCLI.run()