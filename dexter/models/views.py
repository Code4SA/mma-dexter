from sqlalchemy import Table, Column, Integer, ForeignKey

from .support import db

# NOTE: sqlalchemy doesn't easily support creating views, so that is done
# in mysql-specific SQL in resources/mysql/views.sql. 
#
# Don't load this module during tests

# helper view across documents
DocumentsView = Table("documents_view", db.metadata, 
        Column("document_id", Integer, ForeignKey("documents.id")),
        autoload=True, autoload_with=db.engine)

# helper view across sources
DocumentSourcesView = Table("document_sources_view", db.metadata, 
        Column("document_source_id", Integer, ForeignKey("document_sources.id")),
        Column("document_id", Integer, ForeignKey("documents.id")),
        autoload=True, autoload_with=db.engine)

# helper across document fairness
DocumentFairnessView = Table("documents_fairness_view", db.metadata,
        Column("document_id", Integer, ForeignKey("documents.id")),
        autoload=True, autoload_with=db.engine)

# helper across document keywords
DocumentKeywordsView = Table("documents_keywords_view", db.metadata,
        Column("document_id", Integer, ForeignKey("documents.id")),
        autoload=True, autoload_with=db.engine)

# helper across document places
DocumentPlacesView = Table("documents_places_view", db.metadata,
        Column("document_id", Integer, ForeignKey("documents.id")),
        autoload=True, autoload_with=db.engine)

# helper across document principles
DocumentPrinciplesView = Table("documents_principles_view", db.metadata,
        Column("document_id", Integer, ForeignKey("documents.id")),
        autoload=True, autoload_with=db.engine)

# helper across documents for children analysis
DocumentChildrenView = Table("documents_children_view", db.metadata,
        Column("document_id", Integer, ForeignKey("documents.id")),
        autoload=True, autoload_with=db.engine)
