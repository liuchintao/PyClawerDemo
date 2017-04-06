'''
Created on 2017年4月6日

@author: Magister
'''
from bs4 import BeautifulSoup
import re
import urllib

#This method is used to extract useful information as dict type
class HtmlParser(object):
    
    
    def __get_new_urls(self, url, soup):
        new_urls = set()
        links = soup.find_all('a',href=re.compile(r"/item/.*"))
        for link in links:
            new_url = link['href']
            new_full_url = urllib.parse.urljoin(url, new_url)
            new_urls.add(new_full_url)
        return new_urls
    
    
    def __get_new_data(self, url, soup):
        res_data = {}
        
        #URL
        res_data['url'] = url
        
        #Title
        title_node = soup.find('dd', class_ = 'lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title'] = title_node.get_text()
        
        #lemma-summary
        summary_node = soup.find('div', class_ = 'lemma-summary')
        res_data['summary'] = summary_node.get_text()
        
        return res_data
    
    
    def parse(self, url, html_cont):
        if url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        new_urls = self.__get_new_urls(url, soup)
        new_data = self.__get_new_data(url,soup)
        return new_urls, new_data
    
    
    
    



