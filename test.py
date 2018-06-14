import leancloud


#请输入您的leancloud，如果不需要上传到云端，请关闭上传函数
leancloud.init("2C2xis80wMsTyMrkyi1cQIxG-gzGzoHsz", "sYMaOVyBxA81KTXMXQYwDDIg")

Todo = leancloud.Object.extend('flask_web')
query = Todo.query
query.select('comment','createdAt')
query_list = query.find()
list = []

for todo in query_list:
    w = {}
    content = todo.get('comment')
    date = todo.get('createdAt')
    # 如果访问没有指定返回的属性（key），则会返回 null
    # print(content)
    w['comment'] = content
    w['createdAt'] = str(date)[0:19]
    list.append(w)
print(list)