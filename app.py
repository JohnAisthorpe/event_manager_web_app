from flask import Flask, render_template
from controllers.participation_controller import participation_blueprint
from controllers.event_controller import event_blueprint
from controllers.athlete_controller import athlete_blueprint

app = Flask(__name__)

app.register_blueprint(participation_blueprint)
app.register_blueprint(event_blueprint)
app.register_blueprint(athlete_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
