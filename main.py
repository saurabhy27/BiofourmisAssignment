from flask import Flask, request, jsonify
from services import store_data, process_data

app = Flask(__name__)


@app.route("/vitals_input", methods=["GET", "POST"])
def vitals_input():
    resp = store_data.store_in_csv(request.get_json())
    return jsonify({"resp": resp})


@app.route("/vitals_output/<int:agg_min>", methods=["GET"])
def vitals_output(agg_min):
    resp = process_data.processor(agg_min)
    return jsonify({"resp": resp})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=False)
