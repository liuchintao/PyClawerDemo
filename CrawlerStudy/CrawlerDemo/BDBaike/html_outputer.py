'''
Created on 2017年4月6日

@author: Magister
'''


class HtmlOutput(object):
    
    
    def __init__(self):
        self.data_set = []

    
    def collect_data(self,data):
        if data is None:
            return
        self.data_set.append(data)

    
    def output_table(self):
        fout = open("output.html", 'w',encoding='utf-8')
        
        fout.write('<html>')
        fout.write("<head><meta http-equiv=\"content-type\" content=\"text/html;charset=utf-8\"></head>")
        fout.write('<body>')
        fout.write('<table>')
        
        fout.write('<tr>')
        fout.write('<td>URL</td>')
        fout.write('<td>TITLE</td>')
        fout.write('<td>SUMMARY</td>')
        fout.write('</tr>')
        
        for data in self.data_set:
            fout.write('<tr>')
            fout.write('<td>%s</td>' %data['url'])
            fout.write('<td>%s</td>' %data['title'])
            fout.write('<td>%s</td>' %data['summary'])
            fout.write('</tr>')
        
        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')
    
    
    
    
    
    



