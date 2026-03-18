---
name: genpark-receipt-parser
description: Use this skill when the user wants to automatically extract purchase details, item names, and prices from GenPark email receipts or order confirmation text.
metadata: {"openclaw": {"emoji": "🧾", "requires": {}}}
---

# GenPark Receipt Parser

You help the user automatically extract and organize their purchase history from GenPark receipts. You parse raw text or email content and return neat, structured data tracking their spending over time.

## Step 1: Receive the Receipt Text
Ask the user to paste their GenPark order receipt text or email contents. 

## Step 2: Parse and Extract Data
Analyze the text to identify the following details:
- **Order ID**: The unique GenPark tracking or order number.
- **Date of Purchase**: When the order was placed.
- **Items**: A list of the products bought.
- **Individual Prices**: The cost of each product.
- **Total Amount Paid**: Including taxes and shipping.

## Step 3: Format the Output
Return the parsed information in a clean, legible table format.

**Example Output:**
> 🧾 **GenPark Receipt Extracted Successfully**
> **Order #:** GP-987654321
> **Date:** October 12, 2023
> 
> | Item | Price |
> |---|---|
> | Wireless Ergonomic Keyboard | $89.99 |
> | Screen Cleaning Kit | $14.50 |
> | **Tax & Shipping** | $8.00 |
> | **Total** | **$112.49** |

## Step 4: Tracking Memory (Optional)
Ask the user if they'd like to save this order to their running memory log. If they say yes, save a serialized view to their OpenClaw memory:

```yaml
genpark_purchases:
  - order_id: "GP-987654321"
    date: "2023-10-12"
    total: 112.49
    items:
      - "Wireless Ergonomic Keyboard"
      - "Screen Cleaning Kit"
```
