import sys
sys.path.append("./src")

from dockerhttp.server.app import app

if __name__ == '__main__':
    port = 5000
    host = "0.0.0.0"
    print(f"Starting webserver on port {port}")
    app.run(debug=True, port=port, host=host)
