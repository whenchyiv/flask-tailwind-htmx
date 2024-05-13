# WCH Flask Boilerplate

Quick and dirty boilerplate for a Flask app with Tailwind/HTMX.

## Setup
1. Create a virtualenv using python 3.11+ (e.g. `virtualenv .venv -p python3.11`)
2. Install requirements: `source .venv/bin/activate && pip install -r requirements.txt`
3. Create an `env.py` file in the app's root directory and add the var `SECRET_KEY: str = 'yourkeyhere'`
4. `flask run --debug`

## Deployment Notes
- Set an env var PRODUCTION=1 to load the production config, rather than the default development config.
- Includes a basic Procfile and runtime.txt for Railway/Heroku deployment.
- Suggest using whitenoise for static files in prod: https://whitenoise.readthedocs.io/en/stable/flask.html

## Other Info
### templates/base.html
Base jinja2 template for inheritance. Includes `static/css/dist.css` and `static/js/htmx.min.js` by default.

Vars:
- `title: str` the page title
- `description: str` the meta description

Blocks:
- `head` head tag content
- `body` body tag content
- `scripts` bottom of the body tag for javascript

### Miscellaneous Notes
- `./twcompile.sh` is a shortcut script for Tailwind compilation (defaults input from `src/tailwindcss/input.css` and minified output to `static/css/dist.css`).
- The `env.py` file in the app root directory is required for secrets. This is loaded by `config.py` during app creation, and is used by the `DevelopmentConfig` class.
- App is set up with a basic blueprint (`front_page/` for front page views).
- If you need access to the app object, avoid circular imports with `from flask import current_app`.
- Yes I've included jquery 3.7.1 in `static/js`. No you cannot stop me.
