from mysql.connector.errors import ProgrammingError
from bd import nova_conexao


sql = 'select nome from contatos order by nome desc'

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)
    
    print('\n'.join(registro[0] for registro in cursor))