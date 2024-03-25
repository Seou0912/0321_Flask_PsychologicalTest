from flask import Flask, jsonify, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime, timedelta
import pytz
import plotly.express as px
import pandas as pd
from flask_cors import CORS
from psypro.routes import app as main_app

# 데이터베이스 설정
app = Flask(__name__)
app.register_blueprint(main_app)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///instance/psydatabase.db"
db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db)

# 여기에 모델 정의 (Participant, Answer)


# @app.route("/", methods=["GET"])
# def home():
#     # 참여자 정보 입력 페이지를 렌더링합니다.
#     return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
