# app.py

from flask import Flask, request, render_template, redirect, flash, url_for
from models import Pet, db, connect_db
from forms import AddPetForm

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///pet_shelter_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = "chickenzarecool21837"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

connect_db(app)

app.app_context().push()

@app.route('/')
def lest_pets():
    '''Show a list of pets'''
    pets=Pet.query.all()
    return render_template('list_pets.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet_form():
    '''A form to add a pet'''
    form=AddPetForm()

    if form.validate_on_submit():
        name=form.name.data
        species=form.species.data
        age=form.age.data
        photo_url=form.photo_url.data
        notes=form.notes.data

        pet=Pet(name=name, species=species, age=age, photo_url=photo_url, notes=notes)
        db.session.add(pet)
        db.session.commit()

        flash(f'{species} {name} {age} years old is added')
        return redirect('/')
    else:
        return render_template('add_pet_form.html', form=form)
    
@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def show_and_edit_pet_info(pet_id):
    '''A page that shows the pet info and an edit form'''
    pet=Pet.query.get_or_404(pet_id)
    form=AddPetForm(obj=pet)

    if form.validate_on_submit():
        pet.name=form.name.data
        pet.species=form.species.data
        pet.age=form.age.data
        pet.photo_url=form.photo_url.data
        pet.notes=form.notes.data

        db.session.commit()
        flash(f'{pet.species} {pet.name} {pet.age} years old is edited')

        return redirect('/<int:pet_id>')
    
    else:
        return render_template('pet_info.html', pet=pet)


    
