select * from estados

insert into cidades (nome,area,estado_id)
values ('Juiz de Fora', 545, 25)

select * from cidades

insert into cidades (nome,area,estado_id)
values ('Palmas', 325, (select id from estados where sigla = 'TO'))

insert into cidades 
    (nome,area,estado_id)
values 
    ('Montes Claros', 520, (select id from estados where sigla = 'MG')),
    ('Rio de Janeiro', 789, (select id from estados where sigla = 'RJ'))