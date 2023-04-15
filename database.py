from flask import g
import sqlite3

# database connection module.

def connect_db():
    sql = sqlite3.connect('/home/aamathenge/forms/data.db')
    sql.row_factory = sqlite3.Row
    return sql

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

