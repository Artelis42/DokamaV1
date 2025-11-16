import requests
from datetime import datetime, timedelta

API_BASE = "https://api.dofusdu.de/dofus3/v1/fr/almanax"

def fetch_almanax(day_offset: int = 0):
    """
    Récupère l'entrée de l'Almanax pour la date du jour + offset.
    Retourne un dict avec : date, ressource, quantité, bonus.
    """
    target_date = datetime.now().date() + timedelta(days=day_offset)
    date_str = target_date.strftime("%Y-%m-%d")
    url = f"{API_BASE}/{date_str}"

    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        data = resp.json()

        tribute = data.get("tribute", {})
        item = tribute.get("item", {})
        quantity = tribute.get("quantity", "–")
        bonus = data.get("bonus", {}).get("name", "–")

        return {
            "date": date_str,
            "resource": item.get("name", "–"),
            "quantity": quantity,
            "bonus": bonus
        }

    except requests.exceptions.RequestException as e:
        print(f"⚠️ Erreur réseau/API Almanax ({date_str}): {e}")
    except ValueError as e:
        print(f"⚠️ Erreur JSON ({date_str}): {e}")
    except Exception as e:
        print(f"⚠️ Erreur inattendue ({date_str}): {e}")

    return None
