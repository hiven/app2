from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from main.views import main_bp
from products.views import products_bp

app = Flask(__name__)

app.register_blueprint(main_bp)
app.register_blueprint(products_bp, url_prefix='/product')
