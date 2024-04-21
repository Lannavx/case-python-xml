'''
Solicitações do Cliente: 

- Primeiramente, gostaríamos de solicitar a exclusão dos produtos fora de estoque do nosso feed, 
pois não queremos eles no feed no momento, já que não estão disponíveis.

- Alguns produtos estão sem a cor no atributo "color", o que faz com que esse campo seja enviado como "null". 
Segue abaixo a lista com os produtos que gostaríamos que adicionassem a cor, que já vem no título do produto:
    - ID: 261557
    - ID: 235840

- A plataforma identificou erros nos links das imagens de alguns produtos. 
Solicitamos uma análise e, se possível, a correção dos seguintes IDs:
    - ID: 246804
    - ID: 217865
'''

import xml.etree.ElementTree as ET 
conteudo_xml = ET.parse('feed.xml')
produtos = conteudo_xml.getroot()

def identifica_id_item(item_id):
    for item in conteudo_xml.findall('item'):
        if item_id == item.find('id').text:
            return item
        else:
            continue

def exclui_item_fora_estoque():
    for item in conteudo_xml.findall('item'):
        for disponibilidade in item.findall('availability'):
            if disponibilidade.text == '"Fora de estoque"':
                produtos.remove(item)

def atribui_cor(item_id):
    item = identifica_id_item(item_id)
    if item is not None:
        for cor in item.findall('color'):
            if cor.text == 'null':
                titulo =  item.findall('title')      
                for nome in titulo:
                    nome_cor = nome.text.strip().split()[-1].replace('"','')
                cor.text = nome_cor   
    else:
        print(f"Item com ID {item_id} não encontrado.")         

def altera_extensao_link_imagem(item_id):
    item = identifica_id_item(item_id)
    if item is not None:  
        for link in item.findall('image_link'):
            if '.mp3' in link.text:
                link_modificado = link.text.replace('.mp3', '.jpg') 
                link.text = link_modificado
    else:
        print(f"Item com ID {item_id} não encontrado.")            

exclui_item_fora_estoque()

atribui_cor('235840')
atribui_cor('261557')
altera_extensao_link_imagem('246804')
altera_extensao_link_imagem('217865')

conteudo_xml.write('feed.xml', encoding='utf-8', xml_declaration=True)