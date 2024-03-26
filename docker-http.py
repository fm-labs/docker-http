import os
import sys

sys.path.append("./src")

from dockerhttp.server.app import app

if __name__ == '__main__':
    port_setting = os.getenv("PORT", "5050")
    port = int(port_setting)

    host = os.getenv("HOST", "0.0.0.0")
    print(f"Starting webserver on port {port}")
    app.run(debug=True, port=port, host=host)
