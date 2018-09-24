## Sishir ##
import sys

library = []
def make_book(book_id, title, author, genre):
        library_book = {
        'book_id' : book_id,
        'title': title,
        'author': author,
        'genre': genre,
        }
        library.append(library_book)
        
name = input("What is your name? ")
print("%s, Welcome to Sishir's Library 3.0" %(name))
while True:
        interface = input("Do you want to add a [N]ew book, [R]emove a new book, [C]heck books in the Library?, [E]xit Program ")
        if interface == "N" :
                book_id = input( "Make a book id? ")
                title = input("What is the title? ")
                author = input("Who is the author? ")
                genre = input("What is the genre? ")
                add_book = make_book(book_id, title, author, genre)
        if interface == "C" :
                print(library)
        if interface == "R" :
                id_checker = input("Enter book ID to remove. ")
                for dictionary in library:
                        if dictionary['book_id'] == id_checker:
                                library.remove(dictionary)
                print(library)
        if interface == "E" :
                exit()

                        
                                
                                   
                
                
                

                
                              
                
                        


    

         
