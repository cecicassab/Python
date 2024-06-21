from mysql.connector.errors import ProgrammingError
from bd import nova_conexao


sql = 'select * from contatos where tel=98877-3423'

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)

    for x in cursor:
        print(x)