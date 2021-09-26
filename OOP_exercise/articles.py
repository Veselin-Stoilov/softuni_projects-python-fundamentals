class Article:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def edit(self, new_content):
        self.content = new_content

    def change(self, new_author):
        self.author = new_author

    def rename(self, new_title):
        self.title = new_title

    def __repr__(self):
        output = f"{self.title} - {self.content}: {self.author}"
        return output


article_01 = Article('Dear John', 'Romance', 'David Moore')
article_01.edit('Drama')
print(article_01)