
from flask import Flask, render_template, request,session,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
from flask_mail import Mail
import math

with open("config.json", 'r') as fp:
    pars = json.load(fp)['pars']

local_server = True
app = Flask(__name__)
app.config.update(
MAIL_SERVER='smtp.gmail.com',
MAIL_PORT='465',
MAIL_USE_SSL=True,
MAIL_USERNAME=pars["g_user"],
MAIL_PASSWORD=pars["g_pas"]
)

mail = Mail(app)
if local_server:
    app.config['SQLALCHEMY_DATABASE_URI'] = pars["local_uri"]
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = pars["local_uri"]

db = SQLAlchemy(app)

class contact(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(120))
    mss = db.Column(db.String(120), nullable=False)


@app.route("/contacts", methods=["GET", "POST"])
def contacts():
    if request.method == "POST":
        Name = request.form.get('name')
        Email = request.form.get('email')
        sms = request.form.get('sms')
        entry = contact(name=Name, email=Email, mss=sms, date=datetime.now())
        db.session.add(entry)
        db.session.commit()
        mail.send_message("New msg from blog",
                          sender=Email, recipients=[pars["g_user"]],
                          body=sms+"\n"+Email
                          )
    return render_template('contacts.html', pars=pars)




########HOME#############
@app.route("/")
def home():
    posts=Post.query.filter_by().all()[0:pars["no_p"]]
    docs=Doc.query.filter_by().all()[0:pars["no_p"]]
    movies = Movie.query.filter_by().all()[0:pars["no_p"]]
    codes = Code.query.filter_by().all()[0:pars["no_p"]]
    ytofs = Ytof.query.filter_by().all()[0:pars["no_p"]]
    ogames = Ogame.query.filter_by().all()[0:pars["no_p"]]
    gameds = Gamed.query.filter_by().all()[0:pars["no_p"]]
    soft = Software.query.filter_by().all()[0:pars["no_p"]]
    coll = College.query.filter_by().all()[0:pars["no_p"]]
    hosts = Host.query.filter_by().all()[0:pars["no_p"]]
    return render_template('index.html', pars=pars,posts=posts, docs=docs,movies =movies,codes=codes,ytofs=ytofs,ogames=ogames,gameds=gameds,soft=soft,coll=coll,hosts=hosts)


@app.route("/aboutweb")
def about():
    return render_template('aboutweb.html', pars=pars)


####anime######
class Post(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    img = db.Column(db.String(20), nullable=False)
    content = db.Column(db.String(1200), nullable=False)
    logo= db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(25), nullable=False)
    link = db.Column(db.String(50), nullable=False)

###document###
class Doc(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    img = db.Column(db.String(20), nullable=False)
    content = db.Column(db.String(1200), nullable=False)
    logo= db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(25), nullable=False)
    link = db.Column(db.String(50), nullable=False)


#######Movies######
class Movie(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    img = db.Column(db.String(20), nullable=False)
    content = db.Column(db.String(1200), nullable=False)
    logo= db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(25), nullable=False)
    link = db.Column(db.String(50), nullable=False)

######coding##########
class Code(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    img = db.Column(db.String(20), nullable=False)
    content = db.Column(db.String(1200), nullable=False)
    logo= db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(25), nullable=False)
    link = db.Column(db.String(50), nullable=False)

######yoututbe offline#####
class Ytof(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    img = db.Column(db.String(20), nullable=False)
    content = db.Column(db.String(1200), nullable=False)
    logo= db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(25), nullable=False)
    link = db.Column(db.String(50), nullable=False)

######online game######

class Ogame(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    img = db.Column(db.String(20), nullable=False)
    content = db.Column(db.String(1200), nullable=False)
    logo= db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(25), nullable=False)
    link = db.Column(db.String(50), nullable=False)

#######gaming download######

class Gamed(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    img = db.Column(db.String(20), nullable=False)
    content = db.Column(db.String(1200), nullable=False)
    logo= db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(25), nullable=False)
    link = db.Column(db.String(50), nullable=False)

#####software downlaod#######

class Software(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    img = db.Column(db.String(20), nullable=False)
    content = db.Column(db.String(1200), nullable=False)
    logo= db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(25), nullable=False)
    link = db.Column(db.String(50), nullable=False)


######college search#######


class College(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    img = db.Column(db.String(20), nullable=False)
    content = db.Column(db.String(1200), nullable=False)
    logo= db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(25), nullable=False)
    link = db.Column(db.String(50), nullable=False)

#####webhosting########
class Host(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    img = db.Column(db.String(20), nullable=False)
    content = db.Column(db.String(1200), nullable=False)
    logo= db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(25), nullable=False)
    link = db.Column(db.String(50), nullable=False)



app.run(debug=True)



