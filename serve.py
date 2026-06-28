mimetypes_mapping = {
    '.js': 'application/javascript',
    '.css': 'text/css',
    '.html': 'text/html; charset=utf-8',
    '.json': 'application/json',
    '.svg': 'image/svg+xml',
}

def handler(*args, **kwargs):
    import http.server
    h = http.server.SimpleHTTPRequestHandler(*args, directory='.', **kwargs)
    orig = h.guess_type

    def guess(p):
        import os
        ext = os.path.splitext(p)[1].lower()
        return mimetypes_mapping.get(ext) or orig(p)
    h.guess_type = guess
    return h

import http.server
import socketserver
with socketserver.TCPServer(("", 8080), handler) as httpd:
    print("Serving at port 8080")
    import sys
    sys.stdout.flush()
    httpd.serve_forever()
