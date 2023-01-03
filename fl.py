from app import create_app
from flask_migrate import Migrate
from flasgger import Swagger


app = create_app()

from app import db
swagger = Swagger(app)
migrate = Migrate(app, db)

from app.models import Racing
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Racing=Racing)
