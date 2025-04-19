def format_discord_alert(item):
    return {
        "content": "@everyone",  # à personnaliser
        "embeds": [{
            "title": item["title"],
            "description": f'{item["price"]} €',
            "url": item["link"],
            "image": {"url": item["image"]}
        }]
    }
