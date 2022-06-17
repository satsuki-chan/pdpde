"""
Main module for the API server
"""
from flask import render_template
import config

# Application instance
conn_app = config.conn_app
# swagger.yml file to configure endpoints
conn_app.add_api("swagger.yml")

# Default URL route for root, "/"
@conn_app.route("/")
def home():
    """
    This function just responds to the browser URL
    localhost:5000/

    :return:        the rendered template "base.html"
    """
    return render_template("base.html")


if __name__ == "__main__":
    #conn_app.run(threaded=True, port=5000)   ### On Production: debug=False
    conn_app.run(threaded=True, port=5000, debug=True)
