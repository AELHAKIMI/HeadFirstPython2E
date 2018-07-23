from flask import Flask
import vsearch

app = Flask(__name__)

@app.route('/')
def hello() ->str:
    return "hello world from Flask!"

@app.route('/search4')
def do_search() ->str:
    found = vsearch.search4letters("life, the universe, and everything!", 'eiru,!')
    return str(found)

app.run()