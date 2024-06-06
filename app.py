from flask import Flask, request, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Replace with a secret key

# Dictionary to store group members
group_members = []

# Define routes

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_member', methods=['POST'])
def add_member():
    name = request.form['member-name']
    mobile = request.form['member-mobile']
    group_members.append({'name': name, 'mobile': mobile})
    return 'Member added successfully!'

@app.route('/upload_bill', methods=['POST'])
def upload_bill():
    if 'bill' in request.files:
        bill_file = request.files['bill']
        # Process the uploaded bill file here
        return 'Bill uploaded successfully!'
    return 'No file uploaded.'

if __name__ == '__main__':
    app.run(debug=True)
