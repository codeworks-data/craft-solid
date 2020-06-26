# Liskov Substitution Principle


from tools.Database import Database


def parse_user(message):
    return message[0:10]


class Post:
    def create_post(self, database, post_message):
        database.add(post_message)


class TagPost(Post):
    def create_post(self, database, post_message):
        database.add_as_tag(post_message)


class MentionPost(Post):
    def create_post(self, database, post_message):
        user = parse_user(post_message)
        database.notify_user(user)
        super().create_post(database, post_message)


class PostHandler:
    def handle_new_posts(self):
        database = Database()

        new_posts = database.get_unhandled_posts()

        for i, new_post in range(new_posts):
            if new_post[0] == "#":
                post = TagPost()
            elif new_post[0] == "@":
                post = MentionPost()
            else:
                post = Post()

            post.create_post(database, new_post)
