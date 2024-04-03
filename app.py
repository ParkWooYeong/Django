from flask import Flask, request, render_template, redirect
import os
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')

db = SQLAlchemy(app)   

# db 정보 
class board(db.Model):   
    id = db.Column(db.Integer, primary_key=True) 
    user = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    date = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)

class Writing(db.Model):   
    id = db.Column(db.Integer, primary_key=True) 
    category = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    detail = db.Column(db.String, nullable=False)

class textarea(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    username = db.Column(db.String, nullable=False)
    comment = db.Column(db.String, nullable=False)
    comment_date = db.Column(db.String, nullable=False)

with app.app_context():
    db.create_all()

@app.route('/write', methods=['GET', 'POST'])
def write():
    if request.method == 'POST':
        # POST 요청으로부터 데이터를 가져옴
        user = request.form['user']
        title = request.form['title']
        content = request.form['content']
        
        # 데이터베이스에 게시물 추가
        new_post = Writing(user=user, title=title, content=content)
        db.session.add(new_post)
        db.session.commit()
        
        # 게시물 작성 후 리다이렉트 asd
        return redirect('/category/free')
    else:
        # GET 요청인 경우 작성 페이지 렌더링
        return render_template('write.html')

if __name__ == '__main__':
    app.run(debug=True)