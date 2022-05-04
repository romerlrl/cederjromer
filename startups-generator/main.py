import sys


data = [
["Banco digital","Criação e Gerenciamento de e-commerce","Plataforma de contratação de profissionais","Certificado Digital","Rede social focada em divulgação profissional","Especialista em Crowdsourcing","Plataforma de Biblioteca Digital","Segurança da informação para pequenasempresas","Educação Online de Graduação","Podcast (canal profissional)"],
["Dobrar seus lucros","Dobrar suas vendas","Reduzir seus custos pela metade","Abrir uma nova filial","Quitar as dívidas","Adquirir novos clientes","Dobrar seus lucros","Dobrar suas vendas","Reduzir seus custos pela metade","Abrir uma nova filial"],
["3 meses", "6 meses",	"9 meses", "12 meses", "2 anos", "3 meses", "6 meses", "9 meses", "12 meses", "2 anos"], 
["nenhum ", "1", "2", "3", "nenhum ", "1", "2",	"3", "nenhum",	"1"],
["nenhum ", "1", "2", "3", "5",	"10", "nenhum ", "1", "2", "3" ], 
["nenhum", "1", "2", "3", "nenhum", "1", "2", "3", "nenhum", "1"],
["1 mês","3 meses","6 meses","1 ano","2 anos","5 anos","1 mês","3 meses","6 meses","1 ano"], 
["R$ 20.000,00", "R$ 10.000,00", "R$ 6.000,00", "R$ 2.000,00", "R$ -2.000,00", "R$ -5.000,00", "R$ 20.000,00","R$ 10.000,00","R$ 6.000,00","R$ 2.000,00",], 
["R$ 4.000,00","R$ 8.000,00","R$ 12.000,00","R$ 20.000,00","R$ 50.000,00","R$ 4.000,00","R$ 8.000,00","R$ 12.000,00","R$ 20.000,00","R$ 50.000,00"], 
["R$ 10.000,00","R$ 20.000,00","R$ 200.000,00","R$ -50.000,00","R$ 100.000,00","R$ -100.000,00","R$ 50.000,00","R$ 10.000,00","R$ 20.000,00","R$ 200.000,00"]]

template = """O contratante (a sua empresa) é uma empresa especializada em Tecnologia da Informação, localizada na cidade de CIDADE, e atua na área de {}.
A empresa contratante busca {} em um horizonte de {}. Foi feito um levantamento dos dados da empresa, onde se chegaram às seguintes conclusões:
A empresa possui um sócio administrador, {} sócio(s) (todos com participação igual na empresa), {} funcionário(s), e {} estagiário(s).
Possui {} de existência. 
Sua média de lucro bruto mensal (sem descontar os custos fixos) no último ano (ou meses) foi de {};
Possui um custo fixo mensal de funcionamento de {}; 
Possui ainda em caixa, um saldo de {}.
Sabe-se também, que a empresa não possui um produto principal. Seus serviços são dispersos, e as competências não estão claramente definidas. O contratante não conseguiu levantar todos os detalhes, pois não possui sistema de gestão. Sendo assim, cabe ao consultor estimar ou supor as informações que
não constam nesse relatório."""


sys.argv.append("Rio de Janeiro")
cpf = sys.argv[1]
cidade = sys.argv[2]

table = [row[int(v)] for row, v in zip(data, cpf)]
print(template.format(*table).replace("CIDADE", cidade))
