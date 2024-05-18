# b3-tracker
desafio para processo seletivo da Inoa 

O objetivo do sistema é auxiliar um investidor nas suas decisões de comprar/vender de ativos.
Para tal, o sistema deve registrar periodicamente a cotação atual de ativos da B3 e também avisar, via e-mail, caso haja oportunidade de negociação.

Os seguintes requisitos funcionais são necessários:

Expor uma interface web para permitir que o usuário configure:
os ativos da B3 a serem monitorados;
os parâmetros de [túnel de preço](www.b3.com.br/pt_br/solucoes/plataformas/puma-trading-system/para-participantes-e-traders/regras-e-parametros-de-negociacao/tuneis-de-negociacao) de cada ativo;
a periodicidade da checagem (em minutos) de cada ativo.
O sistema deve obter e armazenar as cotações dos ativos cadastrados de alguma fonte pública qualquer, respeitando a periodicidade configurada por ativo.
A interface web deve permitir consultar os preços armazenados dos ativos cadastrados.
Enviar e-mail para o investidor sugerindo a compra sempre que o preço de um ativo monitorado cruzar o seu limite inferior do túnel, e sugerindo a venda sempre que o preço de um ativo monitorado cruzar o seu limite superior do túnel
