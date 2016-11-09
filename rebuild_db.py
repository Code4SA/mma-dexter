from dexter.models import db
from dexter.models.seeds import seed_db
# db.drop_all()
# db.create_all()
seed_db(db)