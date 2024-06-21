from bd import nova_conexao
from mysql.connector.errors import ProgrammingError


sql = 'alter table contatos add column id int auto_increment primary key'

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    
    