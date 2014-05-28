from . import *

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

    for x in DocumentType.create_defaults():
        db.session.add(x)

    for x in AuthorType.create_defaults():
        db.session.add(x)

    for x in Issue.create_defaults():
        db.session.add(x)

    for x in Fairness.create_defaults():
        db.session.add(x)

    for x in Affiliation.create_defaults():
        db.session.add(x)

    for x in AnalysisNature.create_defaults():
        db.session.add(x)

    for x in SourceRole.create_defaults():
        db.session.add(x)

    db.session.commit()

    for x in Principle.create_defaults():
        db.session.add(x)

    db.session.commit()
