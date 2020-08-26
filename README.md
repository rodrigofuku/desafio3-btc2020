# desafio3-btc2020

Para utilizar os códigos, é preciso:
1) Ter instalado na máquina o Python e o Scrapy.
2) Salvar os arquivos na máquina.

Após seguir os passos anteriores, basta utilizar o seguinte comando no prompt de comando a partir da pasta onde os arquivos estão salvos:
```
scrapy runspider <nome do arquivo python> -t json -o <nome do arquivo json>
```
Exemplo: 
```
scrapy runspider Desafio3-Artigos.py -t json -o artigos.json
```
  
### Observação:
Estes scripts vão salvar as informações dos vídeos e dos artigos em um único documento para cada tipo de dado. Como a orientação é fazer o upload um por um, então é preciso salvar cada objeto json em arquivos diferentes manualmente.
