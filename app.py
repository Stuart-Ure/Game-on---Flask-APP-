from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://stuarture@localhost:5432/sport_event_tracker"
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from seed import seed
app.cli.add_command(seed)

from controllers.visit_controller import visits_blueprint
from controllers.sport_event_controller import sport_event_blueprint
from controllers.user_controller import users_blueprint

app.register_blueprint(visits_blueprint)
app.register_blueprint(sport_event_blueprint)
app.register_blueprint(users_blueprint)

@app.route('/')
def home():
    return render_template('index.jinja')

if __name__ == '__main__':
    app.run(debug=True)

