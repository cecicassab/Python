from bd import nova_conexao


with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute('show tables')
    
    for i,database in enumerate(cursor, start=1):
        print(f'tabela {i}: {database[0]}')