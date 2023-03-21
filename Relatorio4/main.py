from database import Database
from writeAJson import writeAJson
import analise

db = Database(database="mercado", collection="compras") 
# db.resetDatabase()

analiseProduto = analise.ProductAnalyzer(db)
writeAJson(analiseProduto.totalVendas(), "totalDeVendas") #1 - Total de vendas por dia
writeAJson(analiseProduto.produtoMaisVendidos(), "ProdutoMaisVendido") # 2 - Produto mais vendido em todas as compras
writeAJson(analiseProduto.clienteMaisGastou(), "ClienteQueMaisGastou") #3 - Cliente que mais gastou em uma unica compra
writeAJson(analiseProduto.listaProdutos(), "ListaDeProdutos") #4 - Lista de produtos vendidos com quantidade maior que 1