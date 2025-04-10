from sqlalchemy.orm import Mapped, mapped_column
from flaskr_medium.database import db
from typing import Optional


# manually uploaded and processed logfile storage tables
class UserInfo(db.Model):
    __tablename__ = "user_info"

    id: Mapped[int] = mapped_column(primary_key=True)
    surname: Mapped[str]
    firstname: Mapped[str]
    age: Mapped[str]
    phone_number: Mapped[str]
    address: Mapped[str]
