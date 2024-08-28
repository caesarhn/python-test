from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route("/segitiga")
@cross_origin()
def segitiga():
    data = request.args.get("data")
    print(data)
    arr = list(str(input))
    result = []
    i = 0
    while i < len(arr):
        result.append(int(arr[i]) * (10 ** i))
    
    return result

@app.route("/ganjil")
@cross_origin()
def Ganjil():
    data = int(request.args.get("data"))
    print(data)
    i = 0
    res = []
    while i < data:
        if i % 2 != 0:
            res.append(i)
        i += 1
    return jsonify(res)

@app.route("/prima")
@cross_origin()
def Prima():
    data = int(request.args.get("data"))
    print(data)
    i = 3
    res = []
    count = data
    while i < data:
        isPrime = True
        for x in range(2, i):
            if count % x == 0:
                isPrime = False
                print(count, " : ", x, " = ", count % x)
        if isPrime:
            res.append(i)
        i += 1
    return jsonify(res)

if __name__ == "__main__":
    app.run()