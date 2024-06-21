from bd import nova_conexao
from mysql.connector.errors import ProgrammingError


tabela_grupo = """
    CREATE TABLE grupos(
        id int auto_increment primary key,
        descricao varchar(30)
    )
"""

alterar_contato_1 = """
    alter table contatos add grupo_id int
"""

alterar_contato_2 = """
    alter table contatos add foreign key (grupo_id)
    references grupos(id)
"""

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(tabela_grupo)
        cursor.execute(alterar_contato_1)
        cursor.execute(alterar_contato_2)

    except ProgrammingError as e:
        print(f'erro {e.msg}')