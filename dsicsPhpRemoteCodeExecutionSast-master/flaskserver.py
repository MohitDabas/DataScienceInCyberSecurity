from flask import Flask, jsonify, request, json
import os

app = Flask(__name__)
@app.route('/open_viscode', methods=['GET'])
def open_viscode():
    PathNLineNum = request.args.get('PathNLineNum')
    os.system("code -g "+PathNLineNum)
    return jsonify(PathNLineNum)


if __name__ == '__main__':
    app.run(debug=True)
