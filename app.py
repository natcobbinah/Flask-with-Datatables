from flask import Flask, render_template
from .blueprint_routes import user_info_blueprint
from .dummy_data import prepopulate_userinfo_table
from flaskr_medium.database import db
from sqlalchemy import text

# Models are defined in other modules,  thus must be imported
# before calling create_all, otherwise SQLAlchemy will not know about them.
# https://flask-sqlalchemy.readthedocs.io/en/stable/quickstart/
from flaskr_medium.models import UserInfo


app = Flask(__name__)
app.config.from_object("flaskr_medium.settings")

# database
db.init_app(app)

# autopopulate database table
with app.app_context():
    """
    SQLite does not have an explicit TRUNCATE TABLE command like other databases. Instead, it has added a TRUNCATE optimizer
    to the DELETE statement. To truncate a table in SQLite, you just need to execute a DELETE statement without a WHERE clause.
    [source: https://www.techonthenet.com/sqlite/truncate.php]
    """
    db.create_all()

    # truncate tables on server-restart instead of dropping and recreating it using db.drop_all()
    truncate_tables = [
        text("DELETE FROM user_info"),
    ]
    for table in truncate_tables:
        db.session.execute(table)
        db.session.commit()

    prepopulate_userinfo_table()


# register blueprint routes
app.register_blueprint(user_info_blueprint)

if __name__ == "__main__":
    app.run()
