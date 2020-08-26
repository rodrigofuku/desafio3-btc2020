# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 19:20:16 2020

@author: RODRIGO
"""

import scrapy
import re


class Desafio_3_Articles(scrapy.Spider):

    name = 'Desafio 3 - Behind the Code - Artigos'
    
    start_urls = [
        'https://olhardigital.com.br/colunistas/wagner_sanchez/post/o_futuro_cada_vez_mais_perto/78972',
        'https://olhardigital.com.br/colunistas/wagner_sanchez/post/os_riscos_do_machine_learning/80584',
        'https://olhardigital.com.br/ciencia-e-espaco/noticia/nova-teoria-diz-que-passado-presente-e-futuro-coexistem/97786',
        'https://olhardigital.com.br/noticia/inteligencia-artificial-da-ibm-consegue-prever-cancer-de-mama/87030',
        'https://olhardigital.com.br/ciencia-e-espaco/noticia/inteligencia-artificial-ajuda-a-nasa-a-projetar-novos-trajes-espaciais/102772',
        'https://olhardigital.com.br/colunistas/jorge_vargas_neto/post/como_a_inteligencia_artificial_pode_mudar_o_cenario_de_oferta_de_credito/78999',
        'https://olhardigital.com.br/ciencia-e-espaco/noticia/cientistas-criam-programa-poderoso-que-aprimora-deteccao-de-galaxias/100683',
        'https://www.startse.com/noticia/startups/mobtech/deep-learning-o-cerebro-dos-carros-autonomos'
    ]
    
    
    
    def parse(self, response):
        
        if response.url == 'https://www.startse.com/noticia/startups/mobtech/deep-learning-o-cerebro-dos-carros-autonomos':
            
            title = response.xpath("//h2[@class='title-single__title__name text-white fw-600']/text()").get()
        
            author = response.xpath("//h4[@class='title-single__info__author__about__name']/a/text()").get()
            
            text_content = response.xpath("//div[@class='content-single__sidebar-content__content']/p")
        
            body_content = ''
            
            for paragraph in text_content:
                text = str(paragraph.extract())
                text = text[35:len(text)]
                text = text.replace("</p>", "\n")
                text = re.sub(r'<\w*\W*\w*\W*>', "", text)
                body_content += text
        
        else:
 
            title = response.xpath("/html/body/div[@id='main']/div[@id='content']/div[@id='materia']/div[@class='inner-wrapper'][1]/article[@class='mat-container']/div[@class='mat-columns']/div[@class='mat-content']/div[@class='mat-header']/h1[@class='mat-tit']/text()").get()
        
            author = response.xpath("/html/body/div[@id='main']/div[@id='content']/div[@id='materia']/div[@class='inner-wrapper'][1]/article[@class='mat-container']/div[@class='mat-columns']/div[@class='mat-content']/div[@class='mat-header']/div[@class='hdr-bottom']/div[@class='hdr-meta']/div[@class='mat-meta']/span[@class='meta-item meta-aut']/text()").get()
            if author.find(","):
                author = author.split(",")[0]
            
            text_content = response.xpath("/html/body/div[@id='main']/div[@id='content']/div[@id='materia']/div[@class='inner-wrapper'][1]/article[@class='mat-container']/div[@class='mat-columns']/div[@class='mat-content']/div[@class='mat-txt']/p")
        
            body_content = ''
            
            for paragraph in text_content:
                text = str(paragraph.extract())
                text = text.replace("</p>", "\n")
                text = re.sub(r'<\w*\W*\w*\W*>', "", text)
                body_content += text
        
        file_json = {
                    "author": author,
                    "body": body_content,
                    "title": title,
                    "type": "article",
                    "url": response.url
                    }
        
        yield file_json
        