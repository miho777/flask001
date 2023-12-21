#!/usr/bin/env python3
# Import modules required for app
from flask import Flask

##### Create a Flask instance
app = Flask(__name__)
count = 0
##### Define routes #####
@app.route('/')
def home(): 
    global count
    count = count + 1
    RET_TEXT = 'Hello World! count= ' + str(count)
    # return RET_TEXT
    return f'<html><head><style>body {{font-size: 32px;}}</style></head><body><p>{RET_TEXT}</p></body></html>'

##### Run the Flask instance, browse to http://<< Host IP or URL >>:8080 
if __name__ == "__main__":
	app.run(host='0.0.0.0', port='8080')