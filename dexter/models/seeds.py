from . import Medium

def seed_db(db):
    """ Add seed entities to the database. """
    for x in Medium.create_defaults():
        db.session.add(x)

    db.session.commit()
