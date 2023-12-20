from flask import Flask, request
from flask import jsonify
import json
from bot import check_new_airtable_record

app = Flask(__name__)


@app.route('/', methods=["GET"])
def getData():
    check_new_airtable_record()
    return jsonify({"status":"success"})


if __name__ == "__main__":
    app.run(debug=True)
