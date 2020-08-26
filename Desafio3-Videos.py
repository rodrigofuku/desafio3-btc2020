# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 19:20:16 2020

@author: RODRIGO
"""

import scrapy


class Desafio_3_Videos(scrapy.Spider):

    name = 'Desafio 3 - Behind the Code - Videos'
    
    start_urls = [
        'https://www.ted.com/talks/helen_czerski_the_fascinating_physics_of_everyday_life/transcript?language=pt-br#t-81674',
        'https://www.ted.com/talks/kevin_kelly_how_ai_can_bring_on_a_second_industrial_revolution/transcript?language=pt-br',
        'https://www.ted.com/talks/sarah_parcak_help_discover_ancient_ruins_before_it_s_too_late/transcript?language=pt-br',
        'https://www.ted.com/talks/sylvain_duranton_how_humans_and_ai_can_work_together_to_create_better_businesses/transcript?language=pt-br',
        'https://www.ted.com/talks/chieko_asakawa_how_new_technology_helps_blind_people_explore_the_world/transcript?language=pt-br',
        'https://www.ted.com/talks/pierre_barreau_how_ai_could_compose_a_personalized_soundtrack_to_your_life/transcript?language=pt-br',
        'https://www.ted.com/talks/tom_gruber_how_ai_can_enhance_our_memory_work_and_social_lives/transcript?language=pt-br'
    ]

    
    def parse(self, response):
    
        title = response.xpath("/html/head/meta[@name='title']/@content").extract()[0].split(":")[1].strip()
    
        author = response.xpath("/html/head/meta[@name='title']/@content").extract()[0].split(":")[0].strip()
        
        text_content = response.xpath("//div[@class='Grid__cell flx-s:1 p-r:4']/p")
        
        body_content = ''
        
        for paragraph in text_content:
            text = str(paragraph.extract())
            text = text[3:len(text)]
            text = text.replace("\t", "")
            text = text.replace("\n", " ")
            text = text.replace("</p>", "\n")
            text = text.replace('"', '\"')
            body_content += text
        
        file_json = {
          "author": author,
          "body": body_content,
          "title": title,
          "type": "video",
          "url": response.url
        }
        
        yield file_json
    
