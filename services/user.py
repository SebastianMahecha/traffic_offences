
import httpmodels.user as user_httpmodels
import models.user as user_models
from sqlmodel import select
import config.db as db


def get_users(session):

    response = user_httpmodels.UserListResponse(
        "success",
        "",
        session.exec(select(user_models.User)).all()
    )
    return response
