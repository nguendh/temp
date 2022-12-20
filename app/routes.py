from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

from app import api
from app.api.api_user import GetUser, AddUser, UpdateUser, DeleteUser
from app.api.api_item import GetItem, AddItem, UpdateItem, DeleteItem
from app.api.api_order_model import GetOrderModel, AddOrderModel, UpdateOrderModel, DeleteOrderModel
from app.api.api_items_in_order import GetItemsInOrder, AddItemsInOrder, UpdateItemsInOrder, DeleteItemsInOrder


@app.route('/')
@app.route('/index')
def hello_world():  # put application's code here
    return render_template('index.html', text='Hello World!')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)


# api route for CRUD user
api.add_resource(GetUser, '/get_user')
api.add_resource(AddUser, '/add_user')
api.add_resource(UpdateUser, '/update_user/<int:id>')
api.add_resource(DeleteUser, '/delete_user/<int:id>')

# api route for CRUD item
api.add_resource(GetItem, '/get_item')
api.add_resource(AddItem, '/add_item')
api.add_resource(UpdateItem, '/update_item/<int:id>')
api.add_resource(DeleteItem, '/delete_item/<int:id>')

# api route for CRUD items_in_order
api.add_resource(GetItemsInOrder, '/get_items_in_order')
api.add_resource(AddItemsInOrder, '/add_items_in_order')
api.add_resource(UpdateItemsInOrder, '/update_items_in_order/<int:id>')
api.add_resource(DeleteItemsInOrder, '/delete_items_in_order/<int:id>')

# api route for CRUD order_model
api.add_resource(GetOrderModel, '/get_order_model')
api.add_resource(AddOrderModel, '/add_order_model')
api.add_resource(UpdateOrderModel, '/update_order_model/<int:id>')
api.add_resource(DeleteOrderModel, '/delete_order_model/<int:id>')

if __name__ == '__main__':
    app.run()
