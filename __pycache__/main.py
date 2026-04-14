from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="🏢 Système de Réservation Hôtel",
    description="Gestion des nuitées, vérification de disponibilité et facturation."
)

# Base de données simulée (In-Memory)
chambres_db = {
    "101": {"categorie": "Standard", "tarif": 50, "disponible": True},
    "102": {"categorie": "Standard", "tarif": 50, "disponible": True},
    "201": {"categorie": "Luxe", "tarif": 120, "disponible": True},
}

class ModeleReservation(BaseModel):
    nom_client: str
    chambre_id: str

@app.get("/tarifs", summary="1. Consulter les tarifs (Action Client)")
def consulter_tarifs():
    """Le client consulte les tarifs et choisit sa catégorie."""
    print("LOG: Un client consulte la liste des tarifs.")
    return {"chambres_disponibles": chambres_db}

@app.get("/disponibilite/{chambre_id}", summary="2. Vérifier disponibilité (Action Réception)")
def verifier_dispo(chambre_id: str):
    """La réceptionniste vérifie si la chambre est libre avant d'accepter."""
    if chambre_id not in chambres_db:
        raise HTTPException(status_code=404, detail="Chambre inexistante")
    
    etat = "Libre" if chambres_db[chambre_id]["disponible"] else "Occupée"
    print(f"LOG: Vérification de la chambre {chambre_id} : {etat}")
    return {"chambre": chambre_id, "statut": etat}

@app.post("/reserver", summary="3. Encaisser et Facturer (Action Réception)")
def enregistrer_reservation(res: ModeleReservation):
    """Émet la facture, encaisse le paiement (ID vérifiée) et notifie le comptable."""
    chambre = chambres_db.get(res.chambre_id)
    
    if not chambre or not chambre["disponible"]:
        print(f"LOG: Réservation refusée pour la chambre {res.chambre_id}")
        return {"resultat": "REFUSÉ", "motif": "Chambre non disponible"}

    # Simulation du processus métier
    chambre["disponible"] = False
    print(f"LOG: Facture émise pour {res.nom_client}. Paiement encaissé.")
    
    return {
        "resultat": "RÉSERVATION ACCEPTÉE",
        "facture": {
            "client": res.nom_client,
            "montant": chambre["tarif"],
            "statut": "Payé (Pièce d'identité enregistrée)",
            "action_comptable": "Copie transmise au comptable pour le tableau de bord."
        }
    }