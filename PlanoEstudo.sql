-- Utilizando o select para retorno de dados da tabela DBSESA.EMPRE
SELECT * FROM DBSESA.EMPRE;

-- Utilizando o select para retorno de dados da tabela DBSESA.EMPRE, especificando colunas para retorno e filtrando valores 'S' pela coluna EMPRE_CDPARTO
SELECT EMPRE_CDCIA, EMPRE_NRAPOLICE 
FROM DBSESA.EMPRE 
WHERE EMPRE_CDPARTO ='S'
FETCH FIRST 100 ROWS ONLY;