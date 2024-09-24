from flask import Flask
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from controllers.youtube import youtube_blueprint
from controllers.general import general_blueprint

app = Flask(__name__)
CORS(app)

# Swagger setup
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name': "YouTube Downloader API"})
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


app.register_blueprint(general_blueprint)
# Register YouTube blueprint
app.register_blueprint(youtube_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
