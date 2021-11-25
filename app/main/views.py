from flask import render_template, request, redirect, url_for, flash

# import the main blue print instance
from app.main import main


@main.route('/')
def index():
    return render_template('index.html')









from project import db
from project.models import Items, User
from .forms import ItemsForm, EditItemsForm


# CONFIG
items_blueprint = Blueprint('items', __name__, template_folder='templates')


# ROUTES
@items_blueprint.route('/all_items', methods=['GET', 'POST'])

def all_items():
    """Render homepage"""
    all_user_items = Items.query.filter_by(user_id=current_user.id)
    return render_template('all_items.html', items=all_user_items)


@items_blueprint.route('/add_item', methods=['GET', 'POST'])
def add_item():
    form = ItemsForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            try:
                new_item = Items(form.name.data, form.notes.data,
                                 current_user.id)
                db.session.add(new_item)
                db.session.commit()
                message = Markup(
                    "<strong>Well done!</strong> Item added successfully!")
                flash(message, 'success')
                return redirect(url_for('home'))
            except:
                db.session.rollback()
                message = Markup(
                    "<strong>Oh snap!</strong>! Unable to add item.")
                flash(message, 'danger')
    return render_template('add_item.html', form=form)


