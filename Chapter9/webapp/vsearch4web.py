from flask import Flask, render_template, request, redirect, escape
from vsearch import search4letters
from mysql import connector

dbconfig = {'host' : '127.0.0.1',
            'user' : 'vsearch',
            'password': 'vsearchpasswd',
            'database': 'vsearchlogDB',
            }

app = Flask(__name__)
# @app.route('/')
# def hello() -> str:
#     return  redirect('/entry')

@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    log_request(request , results)
    return render_template('results.html', 
                    the_phrase=phrase,
                    the_letters= letters,
                    the_title =title,
                    the_results = results,)
    
@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', 
                             the_title='Welcome to search4letters on the web!')

def log_request(req:'flask_request', res:str) -> None:
    conn = connector.connect(**dbconfig)    
    cursor = conn.cursor()    
    _SQL = """ INSERT INTO log
                        (phrase, letters, ip, browser_string, results) 
                        VALUES
                        (%s, %s, %s, %s, %s) """
    
    cursor.execute(_SQL,(req.form['phrase'],
                        req.form['letters'],
                        req.remote_addr,
                        req.user_agent.browser,
                        res,))
    conn.commit()
    cursor.close()
    conn.close()
    

@app.route('/viewlog')
def view_the_log() -> 'html':    
    conn = connector.connect(**dbconfig)    
    cursor = conn.cursor()
    _SQL = """ SELECT * FROM log """
    cursor.execute(_SQL)
    res = cursor.fetchall()
    
        
    
    
if __name__ == '__main__':
    app.run(debug=True)
