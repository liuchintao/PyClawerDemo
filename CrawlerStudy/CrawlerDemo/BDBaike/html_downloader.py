'''
Created on 2017年4月6日

@author: Magister
'''
import urllib.request


class HtmlDownloader(object):
        
    #download page with urllib
    def download(self, url):
        if url is None:
            return
        response = urllib.request.urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read()
    
    
    
    



