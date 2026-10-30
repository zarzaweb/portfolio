from flask import Blueprint, render_template

from data.projects import PROJECTS


projects_bp = Blueprint("projects", __name__, url_prefix="/proyectos")


@projects_bp.route("/")
def proyectos():
    return render_template("proyectos.html")


@projects_bp.route("/<slug>")
def proyecto(slug):
    project = PROJECTS.get(slug)

    if project is None:
        return "Proyecto no encontrado", 404

    return render_template(
        "proyecto.html",
        project=project
    )