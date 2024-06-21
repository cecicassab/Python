select e.nome Empresa, c.nome Cidade
from empresas e, cidades c, empresas_unidades eu
where e.id = eu.empresas_id
and c.id = eu.cidades_id
and sede