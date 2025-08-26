import requests
import sys

# Small alias map for common local names -> ISO codes
ALIASES = {
    'KSH': 'KES',
    'SHILLING': 'KES',
}

# Cache for supported currency symbols
_SYMBOLS_CACHE = None


def get_supported_symbols():
    """Return a set of supported 3-letter currency codes from exchangerate.host.

    Caches the result for this process to avoid repeated network calls.
    """
    global _SYMBOLS_CACHE
    if _SYMBOLS_CACHE is not None:
        return _SYMBOLS_CACHE
    try:
        r = requests.get('https://api.exchangerate.host/symbols', timeout=8)
        r.raise_for_status()
        data = r.json()
        symbols = data.get('symbols') or {}
        _SYMBOLS_CACHE = set(k.upper() for k in symbols.keys())
        return _SYMBOLS_CACHE
    except Exception:
        # If the symbols endpoint is unavailable, return a conservative empty set
        _SYMBOLS_CACHE = set()
        return _SYMBOLS_CACHE


def convert_currency(from_currency: str, to_currency: str, amount: float):
    # Backwards-compatible wrapper that prints the result and returns the value
    converted, err = fetch_conversion(from_currency, to_currency, amount)
    if converted is not None:
        print(f"{amount} {from_currency.upper()} = {converted:.2f} {to_currency.upper()}")
        return converted
    else:
        print(err)
        return None


def fetch_conversion(from_currency: str, to_currency: str, amount: float):
    """Programmatic conversion helper.

    Returns (converted_amount: float, None) on success.
    Returns (None, error_message: str) on failure.
    """
    # Apply aliases (local names -> ISO codes)
    from_currency = ALIASES.get(from_currency.upper(), from_currency.upper())
    to_currency = ALIASES.get(to_currency.upper(), to_currency.upper())

    # Validate currency codes against supported symbols
    symbols = get_supported_symbols()
    if symbols:
        if from_currency not in symbols:
            return None, f"Unknown or unsupported base currency: {from_currency}"
        if to_currency not in symbols:
            return None, f"Unknown or unsupported target currency: {to_currency}"

    url = "https://api.exchangerate.host/convert"
    params = {
        "from": from_currency,
        "to": to_currency,
        "amount": amount
    }
    try:
        response = requests.get(url, params=params, timeout=10)
    except requests.RequestException as e:
        return None, f"Network error while contacting conversion API: {e}"

    # Try to parse JSON safely
    try:
        data = response.json()
    except ValueError:
        return None, "Received non-JSON response from conversion API"

    if response.status_code != 200:
        return None, f"API returned status {response.status_code}: {data}"

    # Primary provider returns 'result'
    if 'result' in data and data['result'] is not None:
        return data['result'], None

    # Primary API didn't return a result - prepare info for debugging
    api_error = data.get('error') or data.get('info')
    debug_msg = "Primary API did not include 'result'."
    if api_error:
        debug_msg += f" Primary API info: {api_error}."

    # Try fallback provider open.er-api.com which exposes latest rates
    try:
        fb_url = f"https://open.er-api.com/v6/latest/{from_currency}"
        fb_resp = requests.get(fb_url, timeout=10)
        fb_resp.raise_for_status()
        fb = fb_resp.json()
        rates = fb.get('rates')
        if not rates or to_currency not in rates:
            return None, debug_msg + " Fallback provider doesn't have the requested currency pair."
        converted = amount * rates[to_currency]
        return converted, None
    except Exception as e:
        return None, debug_msg + f" Fallback failed: {e}"


if __name__ == "__main__":
    # Support optional command-line args to allow non-interactive testing:
    #   python currency_converter.py <FROM> <TO> <AMOUNT>
    if len(sys.argv) >= 4:
        from_currency = sys.argv[1].strip().upper()
        to_currency = sys.argv[2].strip().upper()
        try:
            amount = float(sys.argv[3])
        except ValueError:
            print("Invalid amount provided on the command line.")
            sys.exit(1)
    else:
        from_currency = input("Enter the base currency: ").strip().upper()
        to_currency = input("Enter the target currency: ").strip().upper()
        try:
            amount = float(input("Enter the amount to convert: "))
        except ValueError:
            print("Invalid amount")
            sys.exit(1)

    # Apply simple aliases (avoid unbound warnings by doing mapping here)
    from_currency = ALIASES.get(from_currency, from_currency)
    to_currency = ALIASES.get(to_currency, to_currency)

    convert_currency(from_currency, to_currency, amount)