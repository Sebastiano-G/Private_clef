import pysparql_anything as cli

engine = cli.SparqlAnything()
engine.run(
    q='query.rq',
    l='query_str_decoded'
)