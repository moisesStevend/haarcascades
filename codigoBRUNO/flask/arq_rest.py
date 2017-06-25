from flask import Flask, request
from flask_restful import Resource, Api
import requests

app = Flask(__name__)
api = Api(app)


conteo = {}
tiempo = {}



#conteo[u'duracion']='0'
#tiempo[u'entra']='0'

class Conteo_App(Resource):
    def get(self, conteo_id):
        #print conteo_id, type(conteo_id)
        #if not conteo[conteo_id]:
		#	return "null"#{conteo_id: conteo[conteo_id]}
        #else:
		return conteo[conteo_id]

    def put(self, conteo_id):
        conteo[conteo_id] = request.form['data']
        return conteo[conteo_id]#{conteo_id: conteo[conteo_id]}
        
class Tiempo_App(Resource):
    def get(self, tiempo_id):
        #print tiempo_id
        #if not tiempo[tiempo_id]:
		#	return 'null'
        #else:
		return tiempo[tiempo_id]#{tiempo_id: tiempo[tiempo_id]}

    def put(self, tiempo_id):
        tiempo[tiempo_id] = request.form['data']
        return tiempo[tiempo_id] #{tiempo_id: tiempo[tiempo_id]}
        
api.add_resource(Conteo_App, '/conteo/<string:conteo_id>')
api.add_resource(Tiempo_App, '/tiempo/<string:tiempo_id>')

if __name__ == '__main__':
    #requests.put('http://192.168.2.26:5000/conteo/entra', data = {'data':"4"})
    #srequests.put('http://192.168.2.26:5000/tiempo/duracion', data = {'data':"-1"})
    app.run(host='192.168.2.26', debug=True)
    


#curl http://192.168.2.26:5000/tiempo/duracion -d "data= 30" -X PUT
#curl http://192.168.2.26:5000/conteo/entra -d "data= -1" -X PUT
