import sqlite3

def connect_to_database():
    conn = sqlite3.connect('robot_db')
    return conn

def initialize_database(conn):
    # If table faces does not yet exist, create a new one
    result = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='faces';").fetchone()
    if not result:
        conn.execute("CREATE TABLE faces (user_id INTEGER PRIMARY KEY NOT NULL, face_ref VARCHAR(400) NOT NULL, preference INTEGER);")
        conn.commit()

def get_similar_faces(conn):

    return

def add_new_face(conn, face_data, preference):
    conn.execute("INSERT INTO faces(user_id, face_ref, preference) VALUES({},{},{})".format('NULL', face_data, preference))
    conn.commit()

def get_user_preference(conn, user_id):
    result = conn.execute("SELECT preference FROM faces WHERE faces.user_id == {}".format(user_id)).fetchone()
    return result


if __name__ == '__main__':
    conn = connect_to_database()
    initialize_database(conn)

    # Add new face (for testing now)
    add_new_face(conn, 2, 0)

    # Display all stored data
    print(conn.execute("SELECT * FROM faces").fetchall())