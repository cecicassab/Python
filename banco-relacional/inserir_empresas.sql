alter table empresas modify cnpj varchar(14);

insert into empresas
    (nome,cnpj)
values
    ('Bradesco', 12345678909876),
    ('Vale', 09876543212345),
    ('Cielo', 67584930219283)

select * from empresas

insert into empresas_unidades
    (empresas_id, cidades_id, sede)
values
    (1,1,1),
    (1,2,0),
    (2,1,0),
    (2,2,1);