# NOM: RASOANAIVO Harena Fitiavana
# L3IDEV
 
# Projet Architecture Orientée Service (SOA) - Gestion Hôtel

[cite_start]Ce projet implémente le diagramme BPMN d'un processus de réservation Hôtel-Restaurant[cite: 1].

## Services implémentés
1. [cite_start]**Service Réservation (Port 8000)** : Gère le choix des chambres, la vérification de disponibilité par la réceptionniste et l'émission de facture[cite: 10, 50].
2. [cite_start]**Service Restaurant (Port 8001)** : Gère la publication des menus et la prise de commande liée à la facture de la chambre.

## Installation
1. Installez les dépendances : `pip install -r requirements.txt`
2. Lancez le service Réservation : `cd reservation_service && uvicorn main:app --port 8000`
3. Lancez le service Restaurant : `cd restaurant_service && uvicorn main:app --port 8001`