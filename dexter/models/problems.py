class DocumentAnalysisProblem(object):
    """
    A helper class that describes a problem with a document's analysis.
    It has support for filtering SQL queries to find documents with that
    problem, describing the problem, etc.
    """
    _problems = {}

    def check(self, doc):
        raise NotImplementedError()

    def filter_query(self, query):
        raise NotImplementedError()

    @classmethod
    def all(cls):
        if not cls._problems:
            cls._problems = dict((k.code, k()) for k in cls.__subclasses__())
        return sorted(cls._problems.values(), key=lambda k: k.short_desc)

    @classmethod
    def for_document(cls, doc):
        return [p for p in cls.all() if p.check(doc)]

    @classmethod
    def for_select(cls):
        return [[k.code, k.short_desc] for k in cls.all()]

    @classmethod
    def lookup(cls, key):
        return cls._problems[key]


class MissingTopic(DocumentAnalysisProblem):
    code = 'missing-topic'
    short_desc = 'missing a topic'
    long_desc  = 'This document is missing a topic.'

    def check(self, doc):
        return doc.topic is None

    def filter_query(self, query):
        from .document import Document
        return query.filter(Document.topic == None)


class MissingOrigin(DocumentAnalysisProblem):
    code = 'missing-origin'
    short_desc = 'missing an origin'
    long_desc  = 'This document is missing an origin.'

    def check(self, doc):
        return doc.origin is None

    def filter_query(self, query):
        from .document import Document
        return query.filter(Document.origin == None)


class SourceWithoutFunction(DocumentAnalysisProblem):
    code = 'source-without-function'
    short_desc = 'source without a function'
    long_desc  = 'This document has a source without a function.'

    def check(self, doc):
        return any(ds.source_type != 'child' and ds.source_function_id is None for ds in doc.sources)

    def filter_query(self, query):
        from . import DocumentSource
        return query\
                .join(DocumentSource)\
                .filter(DocumentSource.source_type != 'child')\
                .filter(DocumentSource.function == None)


class SourceWithoutAffiliation(DocumentAnalysisProblem):
    code = 'source-without-affiliation'
    short_desc = 'source without an affiliation'
    long_desc  = 'This document has a source without an affiliation.'

    def check(self, doc):
        return any(ds.source_type != 'child' and ds.affiliation_id is None for ds in doc.sources)

    def filter_query(self, query):
        from . import DocumentSource
        return query\
                .join(DocumentSource)\
                .filter(DocumentSource.source_type != 'child')\
                .filter(DocumentSource.affiliation == None)


class ChildSourceWithoutAge(DocumentAnalysisProblem):
    code = 'child-source-without-age'
    short_desc = 'child source without an age'
    long_desc  = 'This document has a child source without an age.'

    def check(self, doc):
        return any(ds.source_type == 'child' and ds.source_age_id is None for ds in doc.sources)

    def filter_query(self, query):
        from . import DocumentSource
        return query\
                .join(DocumentSource)\
                .filter(DocumentSource.source_type == 'child')\
                .filter(DocumentSource.age == None)


class ChildSourceWithoutRole(DocumentAnalysisProblem):
    code = 'child-source-without-role'
    short_desc = 'child source without a role'
    long_desc  = 'This document has a child source without a role.'

    def check(self, doc):
        return any(ds.source_type == 'child' and ds.source_role_id is None for ds in doc.sources)

    def filter_query(self, query):
        from . import DocumentSource
        return query\
                .join(DocumentSource)\
                .filter(DocumentSource.source_type == 'child')\
                .filter(DocumentSource.role == None)
