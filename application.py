from flask import Flask, render_template


def mainNba():
    return render_template('home.html')

header_text = '''
    <html>\n<head> <title>NBA HeadtoHead</title> </head>\n<body>'''

application = Flask(__name__)

application.add_url_rule('/', 'index', (lambda: header_text +
    mainNba()))

if __name__ == "__main__":
    application.debug = True
    application.run()
