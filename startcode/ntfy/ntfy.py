# Maak een ntfy-notificatie
chatnaam = "A7W1Jr1ZTGrGQTZ4"


import requests
requests.post(f"https://ntfy.sh/{chatnaam}",data="Remote access to phils-laptop detected. Act right away.",
    headers={
        "Title": "banaan is lekker",
        "Priority": "high",
        "Tags": "warning,skull"
    })