'''
Created on 2017年4月6日

@author: Magister
'''
#coding:utf8
import urllib.request

url = 'http://www.baidu.com'

print('First method!')
response1 = urllib.request.urlopen('http://baike.baidu.com/item/java/85979')
print(response1.getcode())
# print(len(response1.read()))
# z_DATA = response1.decode('UTF-8')
# print(z_DATA)
# print(len(response1))
# print(len(z_DATA))

# Second METHOD
print('Second Method')
req = urllib.request.Request(url)
response2 = urllib.request.urlopen(req)
print(response2.getcode())
print(len(response2.read()))

#Third Method For Send Message & Header
print('Third Method')
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values={
    'act' : 'login',
    'Login[email]' :'',
    'Login[password]' : ''
    }
headers = {'User-Agent' : user_agent}
#this fragment is important: 
#data.encode(encoding='utf_8', errors='strict')
data = urllib.parse.urlencode(values).encode(encoding='utf_8', errors='strict')
req = urllib.request.Request(url,data,headers)
print('test1')
response3=urllib.request.urlopen(req)
print('test2')
print(response3.getcode())


#HTTP Authentication
print('HTTP AUTHENTICATION')
#create a password manager
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
#create a user and password
# If we knew the realm, we could use it instead of None.
top_lvl_url = ''
password_mgr.add_password(None, url, '来此荡漾', 'woaichiNM!!@@')
print(password_mgr.passwd)
handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
#create "opener" (OpenerDirector instance)
opener = urllib.request.build_opener(handler)
#use opener to fetch a URL
a_url = 'http://www.baidu.com'
x = opener.open(a_url)
# print(x.read())
#Install the opener.  
# Now all calls to urllib.request.urlopen use our opener. 
urllib.request.install_opener(opener)
a = urllib.request.urlopen(a_url).read().decode('utf8')
# print(a)
