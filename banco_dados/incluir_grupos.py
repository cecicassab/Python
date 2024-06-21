from bd import nova_conexao
from mysql.connector.errors import ProgrammingError


sql = 'insert into grupos (descricao) values (%s)'
args = (
    ('Casa',),
    ('Trabalho',)
)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.executemany(sql,args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print(f'{cursor.rowcount} registro incluído, id ')