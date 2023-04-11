from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

# Configure email settings
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # or your email provider's SMTP server
app.config['MAIL_PORT'] = 587  # or the appropriate port for your email provider
app.config['MAIL_USE_TLS'] = True  # use TLS for secure connection
app.config['MAIL_USERNAME'] = 'tb0016@st.ubt.edu.sa'  # your email address
app.config['MAIL_PASSWORD'] = 'qwe@12345'  # your email password

mail = Mail(app)

# Route for contact us page
@app.route('/contact-us', methods=['GET', 'POST'])
def contact_us():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Create and send email
        msg = Message('Contact Us Form Submission', sender='your_email@gmail.com', recipients=['your_email@gmail.com'])
        msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
        mail.send(msg)

        return 'Message sent successfully!'
    return render_template('contact-us.html')

if __name__ == '__main__':
    app.run()
