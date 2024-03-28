from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Josh Henrietta! I am adding my first code change'

@app.route('/hello')
def hello():
    return render_template('hello.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/about-css')
def about_css():
    return render_template('about-css.html')

@app.route('/favorite-course')
def about_css():
    favorite_course = ['BMGT302', 'BMGT402', 'BMGT403', 'BMGT407']

    return render_template('favorite-course.html', courses=favorite_course)

@app.route('/contact')
def about_css():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run()
