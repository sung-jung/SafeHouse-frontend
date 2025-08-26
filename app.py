from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Here you would check credentials
        # For now, just redirect to dashboard
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Handle registration logic here
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    user = {'username': 'YourName'}
    logs = [
        {'timestamp': '2025-08-26 10:00', 'message': 'System started.'},
        {'timestamp': '2025-08-26 10:05', 'message': 'User logged in.'}
    ]
    return render_template('dashboard.html', user=user, logs=logs)

@app.route('/upload_images', methods=['POST'])
def upload_images():
    # Handle file upload here
    return redirect(url_for('dashboard'))

@app.route('/profile')
def profile():
    # If you have a profile.html, render it here
    return render_template('profile.html') if 'profile.html' in app.jinja_loader.list_templates() else "Profile Settings Page"

@app.route('/logout')
def logout():
    return "Logged out"

if __name__ == '__main__':
    app.run(debug=True)