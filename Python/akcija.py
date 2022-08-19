nr_books = int(input())

book_prices = []

for i in range(nr_books):
    book_prices.append(int(input()))

book_prices.sort()
price = sum([x for i, x in enumerate(reversed(book_prices)) if (i+1) % 3 != 0])
print(price)