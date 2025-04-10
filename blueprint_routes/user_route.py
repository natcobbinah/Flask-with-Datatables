from flask import Blueprint, render_template, request, jsonify, url_for, redirect
import json
from flaskr_medium.database import db
from flaskr_medium.models import UserInfo
from sqlalchemy import select, or_


user_info_blueprint = Blueprint("user_info", __name__)

INDEX_HTML = "index.html"
NO_DATA_AVAIALABLE = "not_available"


@user_info_blueprint.route("/")
def homepage() -> str:
    return render_template(INDEX_HTML)


@user_info_blueprint.route("/", methods=["POST"])
def user_records() -> json:
    draw = int(request.form.get("draw", 1))
    row = int(request.form.get("start", 0))  # offset

    # number of records perpage
    rowperpage = int(request.form.get("length", 10))
    search_value = request.form.get("search[value]", "").lower()

    # Total number of records without filtering
    user_record_count = db.session.query(UserInfo).count()
    usersata_stmt = select(UserInfo).offset(row).limit(rowperpage)
    usersdata_result = db.session.execute(usersata_stmt).scalars().all()

    # Total number of records with filtering
    if search_value != "":
        return queried_search_data(
            search_value=search_value,
            row=row,
            rowperpage=rowperpage,
            draw=draw,
            user_record_count=user_record_count,
            usersdata_result=usersdata_result,
        )

    # Convert the result to a list of dictionaries
    processed_usersata = [
        {
            "id": user.id,
            "surname": user.surname,
            "firstname": user.firstname,
            "age": user.age,
            "phone_number": user.phone_number,
            "address": user.address,
        }
        for user in usersdata_result
    ]

    if len(processed_usersata) > 0:
        return jsonify(
            {
                "draw": draw,
                "data": processed_usersata,
                "recordsTotal": user_record_count,
                "recordsFiltered": user_record_count,
            }
        )

    return jsonify(
        {
            "id": NO_DATA_AVAIALABLE,
            "surname": NO_DATA_AVAIALABLE,
            "firstname": NO_DATA_AVAIALABLE,
            "age": NO_DATA_AVAIALABLE,
            "phone_number": NO_DATA_AVAIALABLE,
            "address": NO_DATA_AVAIALABLE,
        }
    )


# non-route-methods
def queried_search_data(
    *,
    search_value: str,
    row: int,
    rowperpage: int,
    draw: int,
    user_record_count: int,
    usersdata_result: list,
):
    """
    queried_search_data method
        Returns json records of table retrieved from database to be rendered on
        frontend datatable

    search_value:
        Search term typed in search field in frontend-datatable
    row:
        Offset value to start fetching table records from: defaults to 0
    rowperpage:
        Number of records per page returned to frontend-datatables: defaults to 10
    draw:
        Event is fired whenever the table is redrawn on the frontend-page
    user_record_count:
        Total number of records without filtering
    userdata_result:
        List of table records to be returned
    """

    db_query_search_result = (
        db.session.query(UserInfo)
        .filter(
            or_(
                UserInfo.id == search_value,
                UserInfo.firstname.contains(search_value),
                UserInfo.surname.contains(search_value),
                UserInfo.address.contains(search_value),
            )
        )
        .offset(row)
        .limit(rowperpage)
        .all()
    )

    # Convert the result to a list of dictionaries
    processed_logdata = [
        {
            "id": user.id,
            "surname": user.surname,
            "firstname": user.firstname,
            "age": user.firstname,
            "phone_number": user.phone_number,
            "address": user.address,
        }
        for user in db_query_search_result
    ]

    # Convert the result to a list of dictionaries
    if len(processed_logdata) > 0:
        return jsonify(
            {
                "draw": draw,
                "data": processed_logdata,
                "recordsTotal": user_record_count,
                "recordsFiltered": len(usersdata_result),
            }
        )
