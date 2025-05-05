# Total de entradas por estado e ano
QUERY_TOTAL_POR_ESTADO_ANO = """
SELECT 
    state, 
    year, 
    SUM(total_value) AS total_entradas
FROM dados_fronteira
GROUP BY state, year
ORDER BY year, total_entradas DESC
"""

# Total de entradas por categoria de veículo e mês
QUERY_TOTAL_POR_CATEGORIA_MES = """
SELECT 
    vehicle_category, 
    month, 
    SUM(total_value) AS total_mes
FROM dados_fronteira
GROUP BY vehicle_category, month
ORDER BY vehicle_category, month
"""

# Top 10 portos com maior volume total de entradas
QUERY_TOP10_PORTOS = """
SELECT 
    port_name, 
    SUM(total_value) AS total
FROM dados_fronteira
GROUP BY port_name
ORDER BY total DESC
LIMIT 10
"""

# Evolução mensal de entradas por estado (útil para gráficos de linha)
QUERY_EVOLUCAO_MENSAL_ESTADO = """
SELECT 
    state, 
    year, 
    month, 
    SUM(total_value) AS total_mensal
FROM dados_fronteira
GROUP BY state, year, month
ORDER BY state, year, month
"""

# Comparação de uso por tipo de veículo em cada estado
QUERY_COMPARACAO_ESTADO_VEICULO = """
SELECT 
    state, 
    vehicle_category, 
    SUM(total_value) AS total
FROM dados_fronteira
GROUP BY state, vehicle_category
ORDER BY state, total DESC
"""
