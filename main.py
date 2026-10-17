"""
Ajeet Singh - Portfolio Website Local Preview Server
Run this script to launch a local development server and preview the portfolio in your browser.
"""

import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8000
DIRECTORY = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'site')

class PortfolioHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def run():
    os.chdir(DIRECTORY)
    # Allow port reuse immediately
    socketserver.TCPServer.allow_reuse_address = True
    
    with socketserver.TCPServer(("", PORT), PortfolioHandler) as httpd:
        url = f"http://localhost:{PORT}/knowra.html"
        print(f"==================================================")
        print(f"🚀 Portfolio Server running at http://localhost:{PORT}")
        print(f"📂 Serving directory: {DIRECTORY}")
        print(f"🌐 Opening {url} in your browser...")
        print(f"⏹️  Press Ctrl+C to stop the server.")
        print(f"==================================================")
        
        webbrowser.open(url)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server...")
            httpd.server_close()
            sys.exit(0)

if __name__ == '__main__':
    run()
