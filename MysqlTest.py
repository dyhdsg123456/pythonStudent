import mysql.connector

conn = mysql.connector.connect(user='root', password='123456', database='test')
# conn_cursor = conn.cursor()
# cursor = conn_cursor
#
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
# conn.commit()
# cursor.close()

c = conn.cursor()
c.execute('select * from user where id = %s', ('1',))
values = c.fetchall()
print(values)
c.close();
conn.close()
