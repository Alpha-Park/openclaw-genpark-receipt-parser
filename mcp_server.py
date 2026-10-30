import sys
import json
from client import ReceiptParserEngine

def handle_request(req):
    method = req.get("method")
    if method == "tools/list":
        return {
            "tools": [{
                "name": "parse_receipt",
                "description": "Parse raw unstructured receipt text into validated line items and subtotals",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "raw_text": {"type": "string"}
                    },
                    "required": ["raw_text"]
                }
            }]
        }
    elif method == "tools/call":
        args = req.get("params", {}).get("arguments", {})
        out = ReceiptParserEngine.parse_receipt(args.get("raw_text", ""))
        return {"content": [{"type": "text", "text": json.dumps(out, indent=2)}]}
    return {"error": "Unsupported method"}

if __name__ == "__main__":
    for line in sys.stdin:
        if not line.strip(): continue
        try:
            req = json.loads(line)
            res = handle_request(req)
            print(json.dumps({"id": req.get("id"), "result": res}))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"error": str(e)}))
            sys.stdout.flush()
