from mysql.connector.errors import ProgrammingError
from bd import nova_conexao


sql = "select * from contatos where nome like %s"

with nova_conexao() as conexao:
    nome = input('Contato a verificar: ')
    args = (f'%{nome}%',)
    cursor = conexao.cursor()
    cursor.execute(sql, args)

    for x in cursor:
        print(x)