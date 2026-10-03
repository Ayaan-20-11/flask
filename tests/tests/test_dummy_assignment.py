import pytest
from flask import Flask, jsonify

def test_json_dump_assignment():
    app = Flask(__name__)
    with app.app_context():
        res = jsonify({"assignment": "done"})
        assert res.status_code == 200
        assert b'"assignment":"done"' in res.data
