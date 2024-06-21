create table if not exists empresas (
    id int unsigned not null auto_increment,
    nome varchar(255) not null,
    cnpj int unsigned,
    primary key (id),
    unique key (cnpj)
);

-- cidades_empresas
create table if not exists empresas_unidades (
    cidades_id int unsigned not null,
    empresas_id int unsigned not null,
    sede tinyint(1) not null,
    primary key (cidades_id, empresas_id)
);