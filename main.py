from flask import Flask
from flask import request
from flask import url_for
from flask import redirect
from flask_bootstrap import Bootstrap
from flask import make_response
from flask import render_template
import leancloud
leancloud.init("2C2xis80wMsTyMrkyi1cQIxG-gzGzoHsz", "sYMaOVyBxA81KTXMXQYwDDIg")

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/',methods=['GET', 'POST'])
def index():

    #     with open('test.txt','a') as f:
    #         f.writelines(text+'\n')
    # with open('test.txt', 'r') as f:
    #     a = f.readlines()
    # return 'yes'
    Todo = leancloud.Object.extend('flask_web')
    query = Todo.query
    query.select('comment', 'createdAt').add_descending('createdAt')
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


    return render_template('index.html',list = list)
#

@app.route('/api',methods=['GET', 'POST'])
def api():
    if request.method == 'POST':
        text = request.form['text']
        Comment = leancloud.Object.extend('flask_web')
        comment = Comment()
        query = comment.get('comment')

        comment.set('comment',str(text))
        comment.save()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)