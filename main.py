"""Point d'entrée : assemble Modèle, Contrôleur et Vue, puis lance l'application.

    python main.py            → interface graphique (onglets, tableaux, souris)
    python main.py --simple   → menu console classique (comme sur la diapositive)
"""

import sys
from pathlib import Path

from biblioiit.controleur.service import ServiceBibliotheque
from biblioiit.modele.depot_sqlite import DepotSQLite

CHEMIN_BASE = Path(__file__).parent / "donnees" / "biblio.db"


def main() -> None:
    CHEMIN_BASE.parent.mkdir(exist_ok=True)
    depot = DepotSQLite(str(CHEMIN_BASE))   # Modèle
    depot.remplir_si_vide()
    service = ServiceBibliotheque(depot)    # Contrôleur
    try:
        if "--simple" in sys.argv:          # Vue n°1 : console simple
            from biblioiit.vue.console import Console
            Console(service).lancer()
        else:                               # Vue n°2 : interface graphique
            from biblioiit.vue.application import BiblioApp
            BiblioApp(service).run()
    finally:
        depot.fermer()


if __name__ == "__main__":
    main()
