import flask
import flask_restful

import resources.example


app = flask.Flask('CloudBash')
api = flask_restful.Api(app, prefix = '/sh')

api.add_resource(resources.example.Example, '/example')
# endpoint that accepts GET requests with a bash command as a parameter 
# endpoint to retrieve information about the operating system 
# endpoint to retrieve the last 100 commands by user

@app.after_request
def after(response):
    print(f'-> {response}')
    return response

if __name__ == '__main__':
    #init_db
    app.run(use_reloader = True, debug = True, host = '0.0.0.0', port = 80)
