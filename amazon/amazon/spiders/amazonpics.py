# -*- coding: utf-8 -*-
import scrapy
start_urls = input("Enter amazon URL : ")
class AmazonpicsSpider(scrapy.Spider):
   #name of spider
   name = 'amazonpics'

   #list of allowed domains
   allowed_domains = ['www.amazon.in/']
   #starting url
   start_urls = [start_urls]
   #location of csv file
   custom_settings = {
       'FEED_URI' : 'amazontv.csv'
   }

   def parse(self, response):
       #Extract product information
       titles = response.css('a h2::text').extract()
       images = response.css('a.a-link-normal.a-text-normal img::attr(src)').extract()
       prices = response.css('a span.a-size-base.a-color-price.s-price.a-text-bold::text').extract()


       for item in zip(titles,prices,images):
           scraped_info = {
               'title' : item[0],
               'price' : item[1],
               'image_urls' : [item[2]] #Set's the url for scrapy to download images
           }

           yield scraped_info