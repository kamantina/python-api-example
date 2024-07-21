from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flasgger import Swagger

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)

class UppercaseText(Resource):

    def get(self):
        """
        This method responds to the GET request for this endpoint and returns the data in uppercase.
        ---
        tags:
        - Text Processing
        parameters:
            - name: text
              in: query
              type: string
              required: true
              description: The text to be converted to uppercase
        responses:
            200:
                description: A successful GET request
                content:
                    application/json:
                      schema:
                        type: object
                        properties:
                            text:
                                type: string
                                description: The text in uppercase
        """
        text = request.args.get('text')

        return jsonify({"text": text.upper()})


class TextProcessing(Resource):
    def get(self):
        """
        This method responds to the GET request for this endpoint and returns the processed text.
        ---
        tags:
        - Text Processing
        parameters:
            - name: text
              in: query
              type: string
              required: true
              description: The text to be processed
            - name: duplication factor
              in: query
              type: integer
              required: false
              description: The number of times to repeat the text
            - name: capitalization
              in: query
              type: string
              enum: [UPPER, LOWER]
              required: false
              description: The capitalization type for the text
        responses:
            200:
                description: A successful GET request
                content:
                    application/json:
                      schema:
                        type: object
                        properties:
                            text:
                                type: string
                                description: The processed text
        """
        text = request.args.get('text')
        duplication_factor = int(request.args.get('duplication factor', '1'))
        capitalization = request.args.get('capitalization')

        if capitalization == 'UPPER':
            processed_text = text.upper()
        elif capitalization == 'LOWER':
            processed_text = text.lower()
        else:
            processed_text = text

        result = {"text": processed_text * duplication_factor}

        return jsonify(result)


api.add_resource(UppercaseText, "/uppercase")
api.add_resource(TextProcessing, '/process')


if __name__ == "__main__":
    app.run(debug=True)