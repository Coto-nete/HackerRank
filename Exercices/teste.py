if __name__ == '__main__':
    book={}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        book[name]=score
    rank = list(set(sorted(book.values(),reverse=True)))
    print(rank)
    print(book.items())