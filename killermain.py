from fkd1 import ck1
from fkd2 import ck2
from pkd1 import pk1
from pkd2 import pk2
from flask import Flask, request, jsonify
import asyncio
import urllib.parse
from functools import wraps
import time

app = Flask(__name__)

def async_route(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            result = loop.run_until_complete(f(*args, **kwargs))
            return result
        finally:
            loop.close()
    return wrapper

@app.route("/gate=<gate_name>/cc=<cc>")
@async_route
async def process_card(gate_name: str, cc: str):
    """Endpoint to process cards through different gates"""
    
    # Validate CC format
    if not all(x in cc for x in ["|", "|", "|"]):
        return jsonify({"error": "Invalid CC format. Use NUMBER|MM|YY|CVV"}), 400
    
    # Route to appropriate processor
    processors = {
        "fkd1": ck1,
        "fkd2": ck2,
        "pkd1": pk1,
        "pkd2": pk2
    }
    if gate_name not in processors:
        return jsonify({"error": "Gateway not found"}), 404
    
    try:
        start = time.time()
        result = await processors[gate_name](cc)
        tt = f'{time.time()-start:.2f}'
        result = {"result":result,"time":tt}
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
