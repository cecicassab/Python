from mysql.connector.errors import ProgrammingError
from bd import nova_conexao


sql = "select * from contatos where nome like 'Lu%'"

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)

    for x in cursor:
        print(x)