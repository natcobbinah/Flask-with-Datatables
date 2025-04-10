from flaskr_medium.database import db
from sqlalchemy import insert
from flaskr_medium.models import UserInfo
import random


def prepopulate_userinfo_table():
    stmt_userinfos = []

    for i in range(500_000):

        user_random_value = random.random()
        user_random_age = random.randint(1, 150)
        user_phone_number = random.uniform(2.5, 10)

        record_to_insert = insert(UserInfo).values(
            id=i,
            surname="user_s_" + str(user_random_value)[2:],
            firstname="user_f_" + str(user_random_value)[2:],
            age=str(user_random_age),
            phone_number=str(user_phone_number)[2:],
            address="user_addr_" + str(user_random_value)[2:],
        )
        stmt_userinfos.append(record_to_insert)

    for userinfo in stmt_userinfos:
        db.session.execute(userinfo)
        db.session.commit()
