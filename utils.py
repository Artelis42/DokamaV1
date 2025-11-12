# utils.py
from datetime import datetime

def format_date_fr(datestr: str) -> str:
    """Transforme une date YYYY-MM-DD en format JJ/MM."""
    try:
        d = datetime.strptime(datestr, "%Y-%m-%d").date()
        return d.strftime("%d/%m")
    except Exception:
        return datestr
