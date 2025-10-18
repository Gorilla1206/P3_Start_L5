from product_utils import *
import schedule
import time

chatnaam = "A7W1Jr1ZTGrGQTZ4"


def verstuur_notificatie(product):
    bericht = f"Nieuw product: {product.titel} en prijs {product.prijs}"
    #requests.post(f"https://ntfy.sh/{chatnaam}",
                  #data=bericht.encode(encoding="utf-8"))
    print(bericht)
def check_nieuwe_berichten():
    producten = haal_producten_op_simulatie()

    oude_producten = laad_oude_producten()

    print(f"vorige keer waren er {len(producten)} producten ")

    print(f"deze keer zijn er len(producten) producten")

    for product in producten:
        if product not in oude_producten:
             verstuur_notificatie(product)

schedule.every(10).minutes.do(check_nieuwe_berichten)
while(True):
    schedule.run_pending()
    time.sleep(1)




