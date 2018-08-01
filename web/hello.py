def app(environ, start_response):
    data = environ['QUERY_STRING'].replace('&', '\r\n')
    status = "200 OK"
    start_response(status, [("Content-Type", "text/plain"), ("Content-Length", str(len(data)))])
    return iter([data])
