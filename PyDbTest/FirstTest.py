import pymysql
'''
Created on 2017年4月5日

@author: Magister
'''
conn = pymysql.connect(host='127.0.0.1',
                       port=3306,
                       passwd='root',
                       user='root',
                       db='try'
                       )
cur = conn.cursor()
print(conn)
print(cur)
# insertStr = "insert into try.pytest(userId,userName) values('101','Pom')"
# cur.execute(insertStr)
selectStr = "select * from try.pytest"
# print(selectStr)
cur.execute(selectStr)
conn.commit()
infoOne = cur.fetchone()
print(infoOne[0],infoOne[1])
print('This is fetch_all method')
infoRest = cur.fetchall()
for i in infoRest:
    print('USERNAME: %s USERID: %s' %(i[0], i[1]))
cur.close()
conn.close()