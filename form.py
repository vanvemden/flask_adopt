from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional


class AddPetForm(FlaskForm):
    """ Add pet form """

    name = StringField("Pet name", validators=[InputRequired()])
    species = StringField("Species of pet", validators=[InputRequired()])
    photo_url = StringField("Picture of pet", validators=[Optional()])
    age = SelectField("age", choices=[("baby", "Baby"), ("young", "Young"),
                                      ("adult", "Adult"), ("senior", "Senior")], validators=[InputRequired()])
    notes = TextAreaField("Notes",
                          validators=[Optional()])
    available = BooleanField('Active', default=True,
                             validators=[Optional()])


class EditPetForm(FlaskForm):
    """ Edit pet form """

    photo_url = StringField("Picture of pet", validators=[Optional()])
    notes = TextAreaField("Anything worth mentioning?",
                          validators=[Optional()])
    available = BooleanField('Active', default=True,
                             validators=[Optional()])
