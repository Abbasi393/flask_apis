class Post:
    def __init__(self, id, author, content):
        self.id = id
        self.author = author
        self.content = content

    def to_dict(self):
        return {
            "id": self.id,
            "author": self.author,
            "content": self.content
        }
