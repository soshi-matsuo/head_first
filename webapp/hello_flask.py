from flask import Flask, render_template, request, escape, session, copy_current_request_context
from threading import Thread
from time import sleep

from search4letters import search4letters
from DBcm import UseDatabase, NoDBError, CredentialError, SQLError
from checker import check_logged_in

app = Flask(__name__)

app.config['dbconfig'] = {'host':'127.0.0.1', 
						'user':'wrongUser', 
						'password':'wrongPass', 
						'database':'wrongDB'}

app.secret_key = 'YouWillNeverGuess'

@app.route('/login')
def login() -> str:
    session['logged_in'] = True
    return 'You are now logged in'

@app.route('/logout')
def logout() -> str:
    session.pop('logged_in')
    return 'You are now logged out'
	
@app.route('/search4', methods=['POST'])
def do_search():
	@copy_current_request_context
	def log_request(req: 'flask_request', res:str):
		sleep(15)
		try:
			with UseDatabase(app.config['dbconfig']) as cursor:
				query = '''insert into log
						(phrase, letters, ip, browser_string, results)
						values
						(%s, %s, %s, %s, %s)'''
				cursor.execute(query, (req.form['phrase'],
										req.form['letters'],
										req.remote_addr,
										req.user_agent.browser,
										res))
		except CredentialError as err:
			print('wrong ID/Password: ', str(err))
		except NoDBError as err:
			print('Is your database switched on?: ', str(err))
		except SQLError as err:
			print('Is your query correct?', str(err))
		except Exception as err:
			print('something went wrong', str(err))
		return 'Error'
	
	title = 'Here are your results:'
	phrase = request.form['phrase']
	letters = request.form['letters']
	results = str(search4letters(phrase, letters))
	try:
		t = Thread(target=log_request, args=(request, results))
		t.start()
	except Exception as err:
		print('Logging failed with this error: ', str(err))
	return render_template('results.html',
							the_title=title,
							the_phrase=phrase,
							the_letters=letters,
							the_results=results)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', 
                            the_title='Welcome to search4letters on the web!')

@app.route('/viewlog')
@check_logged_in
def view_log():
	try:
		with UseDatabase(app.config['dbconfig']) as cursor:
			query = '''select phrase, letters, ip, browser_string, results from log'''
			cursor.execute(query)
			logs = cursor.fetchall()
		
		titles = ('Phrase', 'Letters', 'Remote_addr', 'User_agent', 'Results')
		return render_template('viewlog.html',
								the_title='View logs',
								the_row_titles=titles,
								the_data=logs)
	except CredentialError as err:
		print('wrong ID/Password: ', str(err))
	except NoDBError as err:
		print('Is your database switched on?: ', str(err))
	except SQLError as err:
		print('Is your query correct?', str(err))
	except Exception as err:
		print('something went wrong', str(err))
	return 'Error'

if __name__ == '__main__':
    app.run(debug=True)