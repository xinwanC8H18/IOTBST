 MongoClient('127.0.0.1', 27017)
db = conn.wx  #连接wx数据库，没有则自动创建
mongo_wx = db.article  #使用article集合，没有则自动创建
 
for i in list:
    app_msg_ext_info = i['app_msg_ext_info']
    # 标题
    title = app_msg_ext_info['title']
    # 文章地址
    content_url = app_msg_ext_info['content_url']
    # 封面图
    cover = app_msg_ext_info['cover']
 
    # 发布时间
    datetime = i['comm_msg_info']['datetime']
    datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(datetime))
 
    mongo_wx.insert({
        'title': title,
        'content_url': content_url,
        'cover': cover,
        'datetime': datetime
    })
