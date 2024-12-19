from flask import Flask, render_template, request, redirect
import firebase_admin
from firebase_admin import credentials, db

app = Flask(__name__)



# Route for the form
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # Push data to Firebase
        ref = db.reference('form_submissions')
        ref.push({
            'name': name,
            'email': email,
            'message': message
        })
        return redirect('/success')
    return render_template('form.html')

# Success Page
@app.route('/success')
def success():
    return "Form submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)


