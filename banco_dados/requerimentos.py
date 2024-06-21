try:
    from mysql import connector
except ModuleNotFoundError:
    print('Mysql não instalado')
else:
    print('Mysql connector instalado e pronto!')