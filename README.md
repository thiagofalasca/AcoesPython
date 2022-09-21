# AcoesPython
Como gosto muito da área de investimentos, resolvi desenvolver esse programa python de web scrapping para me ajudar.
Sempre passei muito tempo analisando ações em sites, onde eu precisava abrir uma página para cada ação para ver os 
indicadores e compara-las.
A partir disso, percebi que seria muito melhor se eu conseguisse apenas escrever um arquivo de texto com as ações 
que quero buscar os indicadores e um programa me retornasse com uma planilha com tudo organizado.
E foi exatamente isso que fiz, de uma forma mais simples e que atendesse as minhas necessidades.

Requisitos para conseguir rodar o programa:

1->Ter o python instalado;
2->Ter as bibliotecas utilizadas pelo programa;
  -pip install requests
  -pip install bs4
  -pip install lxml

Como utilizar o programa:

1->Primeiro você precisará colocar o programa em uma pasta à sua escolha.
2->Nesta mesma pasta, crie um arquivo de texto chamado "acoes.txt", exatamente desta forma como escrevi.
3->Abra o arquivo de texto e liste as ações das quais quer buscar pelos indicadores.
  **Atenção: -Coloque apenas uma ação por linha.
             -Atualmente o programa funciona apenas para bdrs e ações, contudo, ativos diverentes provavelmente não serão encontrados.
             -Dê preferência para colocar o código do ativo, pois o programa pode não conseguir encontra-lo sozinho.
4->Salve o arquivo de texto, execute o programa e espere ele terminar as buscas.

Convertendo a planilha:

Após executar o programa, será criado um arquivo chamado "indicadoresAcoes.csv". 
Fiz o programa pensado para planilhas Excel, por isso gerei o csv dessa forma.
Com isso, será necessário converter o .csv para .xslx

1-> Acesse o site https://convertio.co/pt/csv-xlsx/ 
   **Atenção: -Precisa ser este site, pois alguns realizam a conversão de forma incorreta
              -Caso atinja o limite máximo de conversões por dia, pode abrir o site pela guia anônima que continua funcionando 
2-> Coloque o arquivo .csv
3-> Realize a conversão

Pronto, a planilha já esta finalizada!
