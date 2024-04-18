book_titles = [
    "A Tale of Two Cities",
    "Animal Farm",
    "Brave New World",
    "Catch-22",
    "Great Expectations",
    "Lord of the Flies",
    "Moby-Dick",
    "Pride and Prejudice",
    "The Catcher in the Rye",
    "The Great Gatsby",
    "To Kill a Mockingbird",
    "War and Peace"
]
def binary_search_books(target_book: str, books):
    left, right = 0, len(books) - 1
    # print(len(books))
    while left <= right:
        mid = (left + right) // 2
        mid_book = books[mid]

        if mid_book == target_book:
            return mid 
        elif mid_book < target_book:
            left = mid + 1
        else:
            right = mid - 1
    return -1000 

target_book = input("Tell me the name of book:")

result = binary_search_books(target_book, book_titles)

if result != -1000 :
    print("True")
else:
    print("False")
