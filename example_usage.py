from client import ReceiptParserEngine

if __name__ == "__main__":
    raw = """SuperMarket Plaza
Fresh Organic Apples $4.99
Almond Milk 1L $3.50
Artisan Sourdough $5.20
Tax $1.10
Total $14.79"""
    print("Parsed Receipt:", ReceiptParserEngine.parse_receipt(raw))
