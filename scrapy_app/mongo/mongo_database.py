import pymongo

connection = None
db = None


def save_to_database(database_name, news):
    global connection
    __connect(database_name)
    for i in news:
        __save(i)
    __close_connection()


def __save(news):
    db['khabaronline_DB'].insert_one(news)


def __connect(database):
    global connection, db
    connection = pymongo.MongoClient()
    db = connection[database]


def __close_connection():
    if connection:
        connection.close()


