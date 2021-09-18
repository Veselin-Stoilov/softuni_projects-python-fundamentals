n = int(input())
synonyms_list = []
synonym_book = {}
for _ in range(n):
    word = input()
    synonym = input()
    synonyms_list = []
    if word not in synonym_book:
        synonym_book[word] = synonyms_list
        synonym_book[word].append(synonym)
    else:
        synonym_book[word].append(synonym)

for key, value in synonym_book.items():
    print(f"{key} - {', '.join(value)}")




