from . import Medium, Gender, Race, SourceFunction, Topic

def seed_db(db):
    """ Add seed entities to the database. """
    for x in Medium.create_defaults():
        db.session.add(x)

    for x in Gender.create_defaults():
        db.session.add(x)

    for x in Race.create_defaults():
        db.session.add(x)

    for x in SourceFunction.create_defaults():
        db.session.add(x)

    for x in Topic.create_defaults():
        db.session.add(x)

    db.session.commit()
