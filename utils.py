from model import Users, Orders, Sign_In

def insert_users(*args):
    user = Users(name='Alexandre')
    print(user)
    user.save()

def find_user_by_name():
    user = Users.query.filter_by(name='Alexandre').first()
    print(user.name)

def update_user():
    user = Users.query.filter_by(name='Alexandre').first()
    user.name = 'Angelina'
    user.save()

def delete_user(*args):
    user = Users.query.filter_by(name='Alexandre').first()
    user.delete()

def find_all_users():
    user = Users.query.all()
    print(user)


def insert_orders(*args):
    order = Orders()
    print(order)
    order.save()

def find_order_by_item_description():
    order = Orders.query.filter_by(item_description='Script').first()
    print(order.item_description)

def update_order():
    order = Orders.query.filter_by(item_description='Script').first()
    order.item_description = 'Software'
    order.save()

def delete_order(*args):
    order = Orders.query.filter_by(item_description='Software').first()
    order.delete()

def find_all_orders():
    order = Orders.query.all()
    print(order)

def insert_user_sign_in(login, password):
    sign_in = Sign_In(login=login, password=password)
    sign_in.save()

if __name__ == "__main__":
    #insert_users('Almir')
    #find_user_by_name()
    #update_user()
    #delete_user('Alexandre')
    #find_all_users()
    #insert_user_sign_in('Alex', '1234')
    #insert_orders('Hardware')
    #find_order_by_item_description()
    find_all_orders()
    