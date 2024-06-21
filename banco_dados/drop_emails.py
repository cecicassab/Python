from bd import nova_conexao
from mysql.connector.errors import ProgrammingError


with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute('drop table emails')
    except ProgrammingError as e:
        print(f'erro {e.msg}')