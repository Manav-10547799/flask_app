
from wtforms import Form, StringField, SelectField
class CategorySearchForm(Form):
    choices = [('Men', 'Men'),
               ('Women', 'Women'),
               ('TV', 'TV')]
    select = SelectField('Search for categories:', choices=choices)
    search = StringField('')