"""Les règles métier de la bibliothèque (fonctions pures, faciles à tester).

Responsable : membre A — branche feature/regles
"""

import re
from datetime import date, timedelta

DUREE_EMPRUNT_JOURS = 14
MAX_EMPRUNTS_PAR_ADHERENT = 3

_FORMAT_MATRICULE = re.compile(r"^E\d{4}-\d{3}$")  # ex. E2026-001
_FORMAT_CODE_LIVRE = re.compile(r"^L\d{3}$")       # ex. L002


class RegleMetierErreur(Exception):
    """Levée quand une action viole une règle de la bibliothèque."""


def matricule_valide(matricule: str) -> bool:
    return bool(_FORMAT_MATRICULE.match(matricule))


def code_livre_valide(code: str) -> bool:
    return bool(_FORMAT_CODE_LIVRE.match(code))


def calculer_date_retour(date_emprunt: date) -> date:
    """Date limite de retour : date d'emprunt + DUREE_EMPRUNT_JOURS."""
    return date_emprunt + timedelta(days=DUREE_EMPRUNT_JOURS)


def jours_de_retard(date_retour_prevue: date, aujourd_hui: date) -> int:
    """Nombre de jours de retard (0 si le livre n'est pas en retard)."""
    return max(0, (aujourd_hui - date_retour_prevue).days)


def est_en_retard(date_retour_prevue: date, aujourd_hui: date) -> bool:
    return jours_de_retard(date_retour_prevue, aujourd_hui) > 0


def jours_restants(date_retour_prevue: date, aujourd_hui: date) -> int:
    """Jours avant la date de retour (négatif si le retour est dépassé)."""
    return (date_retour_prevue - aujourd_hui).days


ANNEE_MIN_PUBLICATION = 1450  # invention de l'imprimerie

GENRES = ["Roman", "Contes", "Nouvelles", "Poésie", "Théâtre", "Essai",
          "Informatique", "Sciences", "Histoire", "Autre"]


def annee_publication_valide(annee: int, aujourd_hui: date) -> bool:
    return ANNEE_MIN_PUBLICATION <= annee <= aujourd_hui.year


def peut_emprunter(nb_emprunts_en_cours: int) -> bool:
    """Un adhérent ne peut pas dépasser MAX_EMPRUNTS_PAR_ADHERENT."""
    return nb_emprunts_en_cours < MAX_EMPRUNTS_PAR_ADHERENT
