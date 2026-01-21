#链接数据库
import pymysql
conn = pymysql.connect(host='192.168.146.129', port=3306, user='root', password='root', db='ecshop')
cursor = conn.cursor()

sql = ("INSERT INTO ecs_users(user_id,email,user_name,`password`) "
       "VALUES(null,'{}@qq.com','辣条{}','e10adc3949ba59abbe56e057f20f883e')")

for i in range(1, 1000):
    cursor.execute(sql.format(i, i))
cursor.close()
conn.close()
