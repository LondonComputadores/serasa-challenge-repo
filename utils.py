from model import Users

def insert_users():
    user = Users(name='Alexandre', cpf=11122233345)
    print(user)

def find_user():
    user = Users.query.filter_by(name='Alexandre')
    print(user)

if __name__ == "__main__":
    insert_users()
    #find_user()