from model import Users, Sign_In

def insert_users(*args, **kwargs):
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

def insert_user_sign_in(login, password):
    sign_in = Sign_In(login=login, password=password)
    sign_in.save()

def find_all_users():
    user = Users.query.all()
    print(user)

if __name__ == "__main__":
    #insert_users(('Almir', 'Paes'))
    #find_user_by_name()
    #update_user()
    #delete_user('Alexandre')
    find_all_users()
    #insert_user_sign_in('Alex', '1234')
    