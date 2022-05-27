import Pyro4
from colors import greenText, yellowText, redText, blueText

def printColor (serverMessage):
    if serverMessage[0] == 'G':
        greenText(serverMessage[1])
    elif serverMessage[0] == 'Y':
        yellowText(serverMessage[1])
    elif serverMessage[0] == 'R':
        redText(serverMessage[1])
    elif serverMessage[0] == 'B':
        blueText(serverMessage[1])
    else:
        redText('Data sending ERROR')


if __name__ == '__main__':
    ns = Pyro4.locateNS()
    uri = ns.lookup('library')
    library = Pyro4.Proxy(uri)

    while True:
        greenText("1. Load and print data from the DB \n" +
                 "2. Add a new author \n" +
                 "3. Add a new book \n" +
                 "4. Edit an author \n" +
                 "5. Edit a book \n" +
                 "6. Delete an author \n" +
                 "7. Delete a book \n" +
                 "8. Find an author by id \n" +
                 "9. Find a book by id \n" +
                 "10. Print all authors \n" +
                 "11. Get books number \n" +
                 "12. Print all books \n" +
                 "13. Print all books of author \n" +
                 "14. Exit")
        greenText('Enter command:')
        command = int(input())

        if command == 1:
            serverMessage = library.loadFromDB()
        elif command == 2:
            greenText("Enter author's name: ")
            name = input()
            serverMessage = library.addAuthor(name)
        elif command == 3:
            greenText("Enter the author id: ")
            author_id = int(input())
            greenText("Enter the title: ")
            title = input()
            greenText("Enter the genre: ")
            genre = input()
            greenText("Enter the number of pages: ")
            pages = int(input())
            serverMessage = library.addBook(author_id, title, genre, pages)
        elif command == 4:
            greenText("Enter the author id: ")
            authorId = int(input())
            greenText("Enter new author name: ")
            authorName = input()
            serverMessage = library.editAuthor(authorId, authorName)
        elif command == 5:
            greenText("Enter the book id: ")
            bookId = int(input())
            greenText("What do you want to edit? \n" +
                        "1. Title \n" +
                        "2. Genre \n" +
                        "3. Pages number")
            choice = int(input())
            if choice == 1:
                greenText("Enter new title: ")
                bookTitle = input()
                serverMessage = library.editBook(bookId, choice, bookTitle)
            elif choice == 2:
                greenText("Enter new genre: ")
                bookGenre = input()
                serverMessage = library.editBook(bookId, choice, bookGenre)
            elif choice == 3:
                greenText("Enter new number of pages: ")
                bookPages = int(input())
                serverMessage = library.editBook(bookId, choice, bookPages)
            else:
                redText("Unknown command")
        elif command == 6:
            greenText("Enter the author id: ")
            authorId = int(input())
            serverMessage = library.deleteAuthor(authorId)
        elif command == 7:
            greenText("Enter the book id: ")
            bookId = int(input())
            serverMessage = library.deleteBook(bookId)
        elif command == 8:
            greenText("Enter the author id: ")
            authorId = int(input())
            serverMessage = library.getAuthor(authorId, True)
        elif command == 9:
            greenText("Enter the book id: ")
            bookId = int(input())
            serverMessage = library.getBook(bookId, True)
        elif command == 10:
            serverMessage = library.printAllAuthors()
        elif command == 11:
            serverMessage = library.getBooksNumber()
        elif command == 12:
            serverMessage = library.printAllBooks()
        elif command == 13:
            greenText("Enter the author id: ")
            authorId = int(input())
            serverMessage = library.printAllBooksOfAuthor(authorId)
        elif command == 14:
            exit()
        else:
            redText('Unknown command')
            continue

        printColor(serverMessage.split('#'))