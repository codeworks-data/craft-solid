class Database:
    __online = True

    def save(self, client):
        if self.__online:
            print(client)
            return True
        else:
            return False

