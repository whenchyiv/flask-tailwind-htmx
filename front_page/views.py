from flask import Blueprint, render_template, abort, current_app
from jinja2 import TemplateNotFound


front_page = Blueprint(
    'front_page',
    __name__,
    template_folder='templates'
)


@front_page.get('/', defaults={'page': 'index'})
@front_page.get('/<page>')
def show(page: str) -> str:
    try:
        return render_template(
            f'front_page/{page}.html'
        )
    except TemplateNotFound:
        abort(404)
