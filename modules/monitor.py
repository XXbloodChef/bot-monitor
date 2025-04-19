from modules.scrapers_dispatcher import run_all_scrapers
from modules.storage import load_seen_items, save_seen_items

def monitor_loop():
    seen = load_seen_items()
    new_items = run_all_scrapers()
    for item in new_items:
        if item['link'] not in seen:
            # Alerte ici à intégrer avec alerts.send_alert()
            print(f"Nouvel item détecté : {item['title']}")
            seen.add(item['link'])
    save_seen_items(seen)
