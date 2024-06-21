from bd import nova_conexao
from mysql.connector.errors import ProgrammingError


sql = 'insert into contatos (nome,telefone) values (%s,%s)'
args = ('Lucas, 98877-3423')

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql,args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print('1 registro incluído, id ', cursor.lastrowid)
    