from flask import Flask, render_template, flash, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from form import AddPetForm, EditPetForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres:///adopt"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

connect_db(app)


@app.route("/")
def display_homepage():
    """Display homepage"""

    pets = Pet.query.all()
    return render_template("index.html", pets=pets)


@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Add a pet"""

    form = AddPetForm()

    if form.validate_on_submit():
        form_data = {
            'name': form.name.data,
            'species': form.species.data,
            'photo_url': form.photo_url.data,
            'age': form.age.data,
            'notes': form.notes.data,
            'available': form.available.data
        }
        pet = Pet(**form_data)
        db.session.add(pet)
        db.session.commit()
        return redirect("/")

    else:
        return render_template("form-add-pet.html", form=form)


@app.route("/<int:pid>", methods=["GET", "POST"])
def edit_pet(pid):
    """Edit a pet"""

    pet = Pet.query.get_or_404(pid)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()
        return redirect("/")

    else:
        return render_template("show-pet.html", form=form, pet=pet)
