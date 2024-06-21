from bd import nova_conexao
from mysql.connector.errors import ProgrammingError


sql = 'insert into contatos (nome,telefone) values (%s,%s)'
args = (
    ('Luan, 98877-3423'),
    ('Lara, 98871-3423'),
    ('Maria, 98677-3423'),
    ('Thiago, 93877-3423'),
    ('João, 98897-3423'),
    ('Bia, 98875-3423')
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
    