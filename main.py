from flask import Flask
from view_functions.views import posts_bp

app = Flask(__name__)
app.register_blueprint(posts_bp)

if __name__ == '__main__':
    app.run(debug=True)
