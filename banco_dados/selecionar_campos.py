from mysql.connector.errors import ProgrammingError
from bd import nova_conexao


sql = 'select tel,nome from contatos'

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)

    for contato in cursor.fetchall():
        print(f'{contato[0]}')
        print('\t'.join(str(campo) for campo in contato))