# --*-- Encoding: UTF-8 --*--
import re
import requests
import os
import shutil
import sqlite3
import img
import json

#cursor.execute('delete from girls where id <> \'\' ')

def db_insert(sn_index,dbfile):
    '''insert girls info to db'''
#    conn = sqlite3.connect('./beauty360.db')
    conn = sqlite3.connect(dbfile)
    cursor = conn.cursor()
    url=r'http://image.so.com/zj?ch=beauty&t1=625&sn=%s' % (sn_index)
    index=sn_index
    for l in img.req_get_json(url):
        index=index+1
#        print('-------------',index,l)
        insert_string1=''
        insert_string2=''
        update_string1=''
        for a in l:
            # print(a)
#            print(a,l[a])
            if insert_string1!='':
                insert_string1+=','
            if insert_string2!='':
                insert_string2+=','
            insert_string1=insert_string1+'\''+a+'\''
            insert_string2=insert_string2+'\''+str(l[a])+'\''
            if update_string1!='':
                update_string1+=','
            update_string1+='\''+a+'\'=\''+str(l[a])+'\''

        insert_string='insert into girls (%s) values (%s)' % (insert_string1,insert_string2)
#        print (insert_string)
        insert=True
        try :
            cursor.execute(insert_string)
            conn.commit()
            print("插入数据库成功",str(l['id']))
        except sqlite3.Error as e:
            print ("插入数据库失败",str(l['id']), e)
            insert = False
        if insert==False:
            update_string='update girls set %s where id=\'%s\'' % (update_string1,str(l['id']))
            # print('update sql:' , update_string)
            try:
                cursor.execute(update_string)
                conn.commit()
                print("更新数据库成功", str(l['id']))
            except sqlite3.Error as e:
                print("更新数据库失败", str(l['id']), e)

    cursor.close()
    conn.close()


#for i in xrange(10):
#    db_insert(i*30)

def db_girlsall(dbfile):
    '''select all info from girls table'''
    print ('select start ......')
    conn = sqlite3.connect(dbfile)
    cursor = conn.cursor()
    select_string='select * from girls'
    cursor.execute(select_string)
    i=0
    for row in cursor:
        i=i+1
        print ('[',i,']','--',row[2],'--',row[6],'--',row[7])
#        for item in row:
#            print item
    cursor.close()
    conn.close()
    print ('select down')





def create_db(dbfile):
    conn = sqlite3.connect(dbfile)
    cursor = conn.cursor()
    s='''
    create table girls(    
id TEXT PRIMARY KEY NOT NULL ,
imageid TEXT ,
group_title TEXT ,
tag TEXT ,
grpseq TEXT ,
cover_imgurl TEXT ,
cover_height TEXT ,
cover_width TEXT ,
total_count TEXT ,
'index' TEXT ,
qhimg_url TEXT ,
qhimg_thumb_url TEXT ,
qhimg_width TEXT ,
qhimg_height TEXT ,
dsptime TEXT
);
    '''
    try:
        cursor.execute(s)
        conn.commit()
        print("新建数据库成功")
    except sqlite3.Error as e:
        print("新建数据库失败", e)


