from .views import MoviesAPI, MovieAPI

def url_configuration(api):
    api.add_resource(MoviesAPI, '/movies')
    api.add_resource(MovieAPI, '/movies/<id>')
