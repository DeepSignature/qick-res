from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('instance.config')  # Load config from instance/config.py

    # Register blueprints
    from .controllers.qr_code_controller import qr_code_blueprint
    app.register_blueprint(qr_code_blueprint)

    return app
