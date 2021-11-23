from flask import Flask
from flask_restful import Api, Resource
from services.utils import read_file

app = Flask(__name__)
api = Api(app)

class Movies(Resource):
    def get(self):
        return read_file('./Lab7/data/movies.csv', "movie")

class Links(Resource):
    def get(self):
        return read_file('./Lab7/data/links.csv', "link")

class Tags(Resource):
    def get(self):
        return read_file('./Lab7/data/tags.csv', "tag")

class Ratings(Resource):
    def get(self):
        return read_file('./Lab7/data/ratings.csv', "rating")

api.add_resource(Movies, '/movies')
api.add_resource(Links, '/links')
api.add_resource(Tags, '/tags')
api.add_resource(Ratings, '/ratings')

if __name__ == '__main__':
    app.run(debug=True)
