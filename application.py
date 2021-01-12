from flask import Flask, render_template


def mainNba():
    return render_template('home.html')

header_text = '''
    <html>\n<head> <title>NBA HeadtoHead</title> </head>\n<body>'''

# EB looks for an 'application' callable by default.
application = Flask(__name__)

# add a rule for the index page.
application.add_url_rule('/', 'index', (lambda: header_text +
    mainNba()))

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()