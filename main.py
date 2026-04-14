from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title=" Service Restaurant",
    description="Gestion de la carte (Web/Facebook) et prise de commande."
)

# Menus à publier
menus_db = [
    {"id": 1, "nom": "Petit Déjeuner Complet", "prix": 15},
    {"id": 2, "nom": "Menu Gastronomique", "prix": 45},
    {"id": 3, "nom": "Formule Midi", "prix": 25},
]

class ModeleCommande(BaseModel):
    chambre_id: str
    menu_id: int

@app.get("/menus", summary="1. Afficher les menus (Action Restaurant)")
def afficher_menus():
    """Publie les menus sur le site web et la page Facebook."""
    print("LOG: Publication des menus mise à jour.")
    return {"carte_du_jour": menus_db}

@app.post("/commander", summary="2. Prendre commande (Action Restaurant)")
def prendre_commande(cmd: ModeleCommande):
    """Enregistre la commande et transfère la note à la chambre."""
    menu = next((m for m in menus_db if m["id"] == cmd.menu_id), None)
    
    if not menu:
        return {"erreur": "Plat non trouvé dans la carte."}

    print(f"LOG: Commande de '{menu['nom']}' pour la chambre {cmd.chambre_id}")
    
    return {
        "statut": "Commande en cuisine",
        "facturation": {
            "article": menu["nom"],
            "montant": menu["prix"],
            "action": f"Note ajoutée à la facture globale de la chambre {cmd.chambre_id}",
            "note_interne": "Montant dû au restaurant, encaissé par l'hôtel au départ."
        }
    }
