import mariadb
import dbcreds

username = input('type in your username: ')
content = input('write a post: ')

conn = mariadb.connect(
    user=dbcreds.user,
    host= dbcreds.host,
    password = dbcreds.password,
    port = dbcreds.port,
    database = dbcreds.database)
cursor = conn.cursor()
cursor.execute("INSERT INTO command_line.command_line_blog(username, content, id)VALUES(?, ?, NULL)", [username, content])
conn.commit()
cursor.close()
conn.close()