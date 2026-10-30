from flask import Blueprint, render_template, current_app, request, redirect, url_for, make_response


main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def inicio():
    return render_template("index.html")

@main_bp.route("/sobre-mi")
def sobre_mi():
    return render_template("sobre_mi.html")

@main_bp.route("/contacto")
def contacto():
    return render_template("contacto.html")

@main_bp.route("/robots.txt")
def robots():
    return current_app.send_static_file("robots.txt")

@main_bp.route("/idioma/<lang>")
def idioma(lang):
    if lang not in ("es", "en"):
        return redirect(request.referrer or url_for("main.inicio"))

    response = make_response(
        redirect(request.referrer or url_for("main.inicio"))
    )

    response.set_cookie(
        "language",
        lang,
        max_age=31536000,
        httponly=True,
        samesite="Lax"
    )

    return response