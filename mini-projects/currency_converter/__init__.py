"""currency_converter package exports the main helpers for conversion.

This makes `from currency_converter import fetch_conversion` work when the
package is importable.
"""
from .currency_converter import fetch_conversion, convert_currency, ALIASES, get_supported_symbols

__all__ = ["fetch_conversion", "convert_currency", "ALIASES", "get_supported_symbols"]
