"""Receipt OCR Text Parser Engine.
100% Python Standard Library.
"""

import re

class ReceiptParserEngine:
    """Parses raw scanned receipt strings into structured financial line items."""

    @staticmethod
    def parse_receipt(raw_text: str) -> dict:
        lines = [line.strip() for line in raw_text.splitlines() if line.strip()]
        line_items = []
        total_amount = 0.0
        tax_amount = 0.0
        merchant = lines[0] if lines else "Unknown Merchant"

        for line in lines[1:]:
            # Look for price patterns like $12.99 or 12.99
            match = re.search(r"(\$?\d+\.\d{2})", line)
            if match:
                price_str = match.group(1).replace("$", "")
                try:
                    price = float(price_str)
                    desc = line.replace(match.group(1), "").strip()
                    if "TOTAL" in line.upper():
                        total_amount = price
                    elif "TAX" in line.upper():
                        tax_amount = price
                    else:
                        line_items.append({"item": desc or "Item", "amount": price})
                except ValueError:
                    pass

        calculated_subtotal = sum(i["amount"] for i in line_items)
        if total_amount == 0.0:
            total_amount = calculated_subtotal + tax_amount

        return {
            "merchant": merchant,
            "line_items_count": len(line_items),
            "line_items": line_items,
            "calculated_subtotal": round(calculated_subtotal, 2),
            "tax_amount": round(tax_amount, 2),
            "total_amount": round(total_amount, 2)
        }
