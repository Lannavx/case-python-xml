# Repositório de Manutenção de Feed de Produtos

Este repositório contém scripts e dados para a manutenção de um feed de produtos, garantindo que as informações no feed estejam corretas e atualizadas.

## Arquivos

- `case.py`: Script Python que processa o arquivo `feed.xml` para realizar as seguintes operações:
  - Excluir produtos que estão fora de estoque.
  - Adicionar informações de cor aos produtos que estão com o campo cor como `null` usando o título do produto.
  - Corrigir links quebrados das imagens dos produtos.
- `feed.xml`: Arquivo XML que contém a lista de produtos. Cada item inclui ID, título, preço, link, link de imagem, tipo de produto, cor e disponibilidade.
- `feed_alterado.xml`: Resultado do Script após manipulação do XML

## Funcionamento

O script `case.py` utiliza a biblioteca `xml.etree.ElementTree` para parsear e manipular o arquivo `feed.xml`. As funções definidas no script são:
- `exclui_item_fora_estoque()`: Exclui itens que estão fora de estoque.
- `adiciona_cor_de_titulo()`: Adiciona a cor ao atributo `color` de produtos que estão com esse campo como `null`.
- `corrige_link_imagem()`: Corrige os links das imagens que estão incorretos.

## Como Usar

1. Certifique-se de que o Python está instalado em sua máquina.
2. Coloque os arquivos `case.py` e `feed.xml` no mesmo diretório.
3. Execute o script com o comando `python case.py`.

## Requisitos

- Python 3.x
- Biblioteca `xml.etree.ElementTree` (já inclusa com o Python)

