Aplicação que busca os valores das ações das empresas que deseja e retorna como uma tabela.

O código irá utilizar selenium, bs4 e pandas.

Criamos uma lista com o nome das empresas que desjamos consultar o valor das ações, pedimos para que o selenium abra o navegador e acesse o link com o nome das empresas. Iremos realizar o WebScraping com o bs4 para retornar o valor da ação. Colocamos os valores em um dicionário e depois com o pandas transformamos em um Data Frame.

A utilidade está em conseguir as informações das ações que deseja rapidamente somente com o nome das empresas desejadas.