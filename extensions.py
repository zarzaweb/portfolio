from flask import request
from flask_babel import Babel, Domain


def get_locale():
    return request.cookies.get("language", "es")

babel = Babel(
    locale_selector=get_locale
)


projects_domain = Domain(domain="projects")
projects_gettext = projects_domain.lazy_gettext