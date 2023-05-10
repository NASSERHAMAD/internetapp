from flask import Flask,render_template
from postsdata import posts

app = Flask(__name__)

# Page Routes
@app.route("/")
def homePagex():
   return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')
        
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/mobiles")
def mobiles():
    return render_template('mobiles.html')

@app.route("/reqres-data")
def reqresData():
    return render_template('reqres-data.html')

@app.route("/posts")
def home():
    return render_template('post-all.html',
                           title='all posts',
                           posts=posts)

@app.route("/404")
def error():
    return render_template('404.html')

@app.route('/posts/<int:post_id>')
def show_post(post_id):
    if post_id < len(posts):
       p = posts[post_id]
       return render_template('post-single.html',
       title= f"Post#{post_id}", p = p )
    else:
        return render_template('404.html'), 404

    
#to get favicon working on layout instead of html page
import os
from flask import send_from_directory
from json import dumps

@app.route("/favicon.ico") 
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/json_posts")
def json_posts():
    data = {
        'data': posts,
        'total': len(posts)
    }
    return dumps(data)


# Setting up Flask-Mail
from flask_mail import Mail, Message
from flask import request

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True

app.config['MAIL_USERNAME'] = 'ubttester1@gmail.com'
app.config['MAIL_PASSWORD'] = 'cjnwhlfllfvkwdtc'

mail = Mail(app)

@app.route('/send_email', methods=['post'])
def send_reset_email(user_email):

   msg = Message('email title',
                 sender = 'noreply@demo.com',
                 recipients = [user_email] )

   msg.body = f'''
   	Hello { user_email }
   '''
   mail.send(msg)

#Implementing flask to the second form of the contact us page
@app.route('/contact', methods=['POST'])
def contact_us():
    name = request.form['Contact-Name']
    email = request.form['Contact-Email']
    message = request.form['Contact-Message']

    # Send email using Flask-Mail
    msg = Message('Contact Us Form Submission',
                  sender='noreply@demo.com',
                  recipients=['ubttester1@gmail.com'])
    msg.body = f'''
        Name: {name}
        Email: {email}
        Message: {message}
    '''
    mail.send(msg)

    # Return a success message to the user
    return 'Thank you for your message!'\
        '<a href="/contact"> Click here to submit another message.'\
        '</a> <br> Or click <a href="/index">Home</a> to return to the main page'

#debug tool
if __name__ == '__main__':
	app.run( debug=True )

