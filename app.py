from flask import Flask

from routes import main_bp, projects_bp

from extensions import babel, get_locale


app = Flask(__name__)

babel.init_app(app, locale_selector=get_locale)

app.register_blueprint(main_bp)
app.register_blueprint(projects_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)