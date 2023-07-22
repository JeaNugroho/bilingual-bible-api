from flask import Flask, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS

import services.esv_service as EsvService
import services.tb_service as TbService
import config

app = Flask(__name__)
app.config.from_object(config)
CORS(app, resources={r"/*": {"origins": "http://localhost:8080"}})

api = Api(app)

class Passages(Resource):

    def get(self, book, chapter):
        # body = request.get_json()
        # searchDir = body.get('searchDirection')

        
        esv_params = f'{book} {chapter}'
        
        esv_response = EsvService.fetch_esv(esv_params, app.config['ESV_API_TOKEN'])
        esv_chopped = EsvService.chop_string(esv_response['passages'][0], esv_params)
        has_title_in_beginning = False
        if esv_chopped[0][0] != '[':
            has_title_in_beginning = True

        book_idx = EsvService.get_esv_books().index(book)
        tb_chopped = TbService.fetch_tb(book_idx, chapter, has_title_in_beginning)

        data = {
            'data': {
                'esv': esv_chopped,
                'tb': tb_chopped
            }
        }
        
        return jsonify(data)
        

api.add_resource(Passages, '/book/<string:book>/chapter/<int:chapter>', endpoint='item')


if __name__ == '__main__':
    app.run(debug=True)