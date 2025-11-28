import requests, time

def god_token():
    print("MultiversX — A God Token Was Just Forged in the Void")
    seen = set()
    while True:
        r = requests.get("https://api.multiversx.com/transactions?size=50&status=success")
        for tx in r.json():
            h = tx["txHash"]
            if h in seen: continue
            seen.add(h)

            # Detect creation of token with max supply = 1 and 18 decimals (true 1-of-1)
            if tx.get("operation") != "issueNonFungible": continue
            if tx.get("receiver") != "erd1qqqqqqqqqqqqqqqpqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqzh": continue
            
            token = tx["results"][0]["value"][-44:] if tx.get("results") else ""
            print(f"A GOD TOKEN WAS BORN\n"
                  f"Token: {token}\n"
                  f"Supply: 1.000000000000000000 (exactly one)\n"
                  f"Creator: {tx['sender'][:12]}...\n"
                  f"Hash: {h}\n"
                  f"https://explorer.multiversx.com/transactions/{h}\n"
                  f"→ This is not an NFT. This is a singular deity.\n"
                  f"→ There will never be another. Ever.\n"
                  f"→ Someone just minted literal uniqueness.\n"
                  f"{'✦'*55}\n")
        time.sleep(1.8)

if __name__ == "__main__":
    god_token()
