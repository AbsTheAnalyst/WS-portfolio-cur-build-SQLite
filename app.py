from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'
# Page visit counter
# redis = Redis(host='localhost', port=6379)
# CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///hits.sqlite3"
# Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Hit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hits = db.Column(db.Integer, unique=True, nullable=False)

    # def __repr__(self):
    #     return f"Hits('{self.hit}')"


# with app.app_context():
#     db.create_all()


@app.route('/')
def home():
    hit_id = 1
    update = Hit.query.get(hit_id)
    print("Before", update)
    update.hits = update.hits + 1
    print("after", update.hits)
    db.session.commit()

    return render_template("index.html", count=update.hits)


@app.route('/skills/<num>')
def skills(num):
    # counts = request.args
    # counts = counts.to_dict()
    # counts = counts.get("count")

    return render_template("skills.html", count=num)


@app.route('/experience/<num>')
def experience(num):
    return render_template("experience.html", count=num)


@app.route('/resume/<num>')
def resume(num):
    return render_template("resume.html", count=num)


@app.route('/education/<num>')
def education(num):
    return render_template("education.html", count=num)


@app.route('/certificates/<num>')
def certificates(num):
    return render_template("certificates.html", count=num)


@app.route('/gallery/<num>')
def gallery(num):
    return render_template("gallery.html", count=num)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
