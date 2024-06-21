SELECT * FROM estados

SELECT Sigla, nome as 'Nome do Estado' FROM estados
WHERE regiao='Sul'

SELECT nome,populacao FROM estados 
WHERE populacao >=3
order by populacao desc