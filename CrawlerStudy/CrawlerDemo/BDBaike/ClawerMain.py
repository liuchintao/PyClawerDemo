'''
Created on 2017年4月6日

@author: Magister
'''
from CrawlerStudy.CrawlerDemo.BDBaike import url_manager, html_downloader,\
    html_parser, html_outputer
import time



def performance(f):
    def wrapper(*args):
        t1 = time.time()
        r = f(*args)
        t2 = time.time()
        t = t2 - t1
        print('We begin crawling at: %s' %t1)
        print('We stop crawling at: %s' %t2)
        print('this time we crawl about %ss' %t)
        return r
    return wrapper


class CrawlerMain(object):
    
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.output = html_outputer.HtmlOutput()
    
    @performance
    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_next_url():
            try:
                new_url = self.urls.get_new_url()
                print('crawling %d: %s' %(count,new_url))
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.output.collect_data(new_data)
                
                if count == 100:
                    break
                count += 1
            except:
                print('%d crawl failed!' %count)
        self.output.output_table()



if __name__ == '__main__':
    #root url for start spider
    root_url = 'http://baike.baidu.com/item/java/85979'
    obj_crawler = CrawlerMain()
    obj_crawler.craw(root_url)