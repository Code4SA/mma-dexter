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
