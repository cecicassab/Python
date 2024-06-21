from mysql.connector.errors import ProgrammingError
from bd import nova_conexao


sql = 'update contatos set nome = %s where id = %s'
args = ('Otávio', 1)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql,args)
        cursor.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print(f'{cursor.rowcount} registro(s) atualizado(s)')