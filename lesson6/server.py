from flask import Flask,abort,request, render_template





my_flask_app = Flask(__name__)

@my_flask_app.route('/')  # определяем страницу 

def index():    
    return render_template('index.html', title = "Свежие Новости")


@my_flask_app.route('/all/')  # определяем страницу 

def all_news():    
    return render_template('all_the_news.html')

@my_flask_app.route('/sponsor/')  # определяем страницу 

def sponsor_news():    
    return render_template('sponsor_the_news.html')


@my_flask_app.route('/login/', methods = ['POST'])  # определяем страницу 

def login():
    return render_template('login.html', email = request.form.get('email'), password = request.form.get('passwd'))

if __name__ == '__main__':
    my_flask_app.run(port=5010,debug=True)
