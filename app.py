from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Add this line if not already present

@app.route('/')
def landing():
    logged_in = 'user_id' in session
    return render_template('landing.html', logged_in=logged_in)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Simulate successful login
        session['user_id'] = 1  # Set user_id in session
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Simulate successful registration
        session['user_id'] = 1  # Set user_id in session
        return redirect(url_for('dashboard'))
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

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    user = {'username': 'YourName', 'email': 'your@email.com'}
    if request.method == 'POST':
        # Handle profile update logic here
        return redirect(url_for('profile'))
    return render_template('profile.html', user=user)

@app.route('/logout')
def logout():
    session.pop('user_id', None)  # Log out the user
    return redirect(url_for('landing'))

if __name__ == '__main__':
    app.run(debug=True)