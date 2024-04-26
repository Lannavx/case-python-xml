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

def exclui_item_fora_estoque():
    '''Itera sobre os itens do arquivo XML e exclui os itens "Fora de estoque"'''
    for item in conteudo_xml.findall('item'):                 
        for disponibilidade in item.findall('availability'):      
            if disponibilidade.text == '"Fora de estoque"':       
                produtos.remove(item)                             

def atribui_cor(conteudo_xml):                
    '''Itera sobre os itens do arquivo XML identificando a cor nos titulos, 
    exclui os espaços no titulo e substitui a cor identificada no lugar de null'''                         
    for item in conteudo_xml.findall('item'):     
        for cor in item.findall('color'):                                            
            if cor.text == 'null':          
                titulo =  item.findall('title')        
                for nome in titulo:                          
                    nome_cor = nome.text.strip().split()[-1].replace('"','') 
                cor.text = nome_cor                     
                                             
def altera_extensao_link_imagem(conteudo_xml):          
    '''Itera sobre os itens do arquivo XML identificando o texto '.mp3' e substituindo para 'jpg' '''
    for item in conteudo_xml.findall('item'):                                       
        for link in item.findall('image_link'):                                     
            if '.mp3' in link.text:                                                 
                link_modificado = link.text.replace('.mp3', '.jpg')                 
                link.text = link_modificado                                         

exclui_item_fora_estoque()
atribui_cor(conteudo_xml)
altera_extensao_link_imagem(conteudo_xml)

# Salva as alterações no arquivo XML
conteudo_xml.write('feed_alterado.xml', encoding='utf-8', xml_declaration=True)

# encoding define o formato de codificação de caracteres
# xml_declaration adiciona a declaração de XML no início do arquivo.