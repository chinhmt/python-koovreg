from flask import (
  Blueprint,
)

module = Blueprint('general', __name__)


@module.app_errorhandler(404)
def page_not_found(error):
  return "404 Not Found", 404


@module.app_errorhandler(500)
def internal_error(err):
  return "500 Internal Server Error", 500
