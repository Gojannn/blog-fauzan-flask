# import aplikasi flask untuk dipakai web ita
from flask import Flask 

# mengatur nama aplikasi
app = Flask(__name__)

# mengatur URI (universal resource identifier), dan apa yang ditampilkan jika URI tersebut diakses
@app.route('/')# ketika alamat http://127.0.0.1:500/ dipanggil, maka server akan mengeksekusi fungsi hello()
def hello(): # function dengan nama hello
    return 'Hello, World'

# mengatur URI ke http://127.0.0.1:500/login, dan mengeksekusi fungsi login() jika diakses di alamat URI http://127.0.0.1:500/login
@app.route('/login')
def login():
    return 'halaman login'