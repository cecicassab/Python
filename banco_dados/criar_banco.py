from mysql.connector import connect


conexao = connect( 
    host='localhost',
    port=3306,
    user='root',
    passwd='password'
)


cursor = conexao.cursor()
cursor.execute('CREATE DATABASE agenda')