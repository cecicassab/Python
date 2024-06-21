SELECT 
    regiao as 'Região',
    sum(populacao) as Total
FROM `estados`
GROUP BY regiao
order by Total desc

SELECT 
    sum(populacao) as Total
FROM `estados`

SELECT 
    avg(populacao) as Total
FROM `estados`