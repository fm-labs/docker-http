import os
import sys

sys.path.append("./src")

from dockerhttp.server.app import app

if __name__ == '__main__':
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "5050"))

    print(f"Starting webserver on port {port}")
    app.run(debug=True, port=port, host=host)
