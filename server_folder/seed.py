from model import connect_to_db, db, User



def create_user():
    print('Users')
    User.query.delete()

    user1 = User(email='user@example.com', password='123', first_name='John', last_name='Smith', budget=0.00, bill_color='#955525')

    db.session.add(user1)


if __name__ == '__main__':
    from flask import Flask
    app = Flask(__name__)
    connect_to_db(app)

    db.create_all()

    create_user()

    db.session.commit()