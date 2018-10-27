import sqlite3

# Crée une nouvelle base de donnée is elle n'existe pas
with sqlite3.connect("blog.db") as connection:
    # Crée un curseur objet pour utiliser les commandes sql
    c = connection.cursor()

    # Crée une table posts avec com colonne title et posts
    c.execute("CREATE TABLE posts(title TEXT, post TEXT)")

    # Innsere ces données à la table posts
    c.execute('INSERT INTO posts VALUES("Good", "I\'m good")')
    c.execute('INSERT INTO posts VALUES("Well", "I\'m well")')
    c.execute('INSERT INTO posts VALUES("Excellent", "I\' excellent")')
    c.execute('INSERT INTO posts VALUES("Okay", "I\'m okay")')
