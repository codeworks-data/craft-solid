class Database:
    __online = True

    def save(self, client):
        if self.__online:
            print(client)
            return True
        else:
            return False

    def add(self, message):
        pass

    def add_as_tag(self, message):
        pass

    def get_unhandled_posts(self):
        pass
