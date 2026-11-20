# BiblioIIT — Gestion de la bibliothèque

Application console en Python pour gérer les emprunts de la bibliothèque de l'IIT.
Projet d'équipe, Séance 4.

## Architecture MVC

```
BiblioIIT/
├── main.py                     ← point d'entrée : relie M, V et C
├── biblioiit/
│   ├── modele/                 ← M : données + règles + base
│   │   ├── modeles.py          (B) Livre, Adherent, Emprunt
│   │   ├── regles.py           (A) durée d'emprunt, retards, formats
│   │   └── depot_sqlite.py     (C) lecture/écriture SQLite
│   ├── controleur/             ← C : la logique des actions
│   │   └── service.py          (D) rechercher, emprunter, rendre, retards
│   └── vue/                    ← V : ce que voit l'utilisateur
│       ├── application.py      (E) interface graphique Textual (onglets, tableaux)
│       ├── fenetres.py         (E) fenêtre « Choisir un adhérent »
│       ├── style.tcss          (E) couleurs et mise en page de l'interface
│       └── console.py          (E) menu console simple (input / print)
├── tests/                      ← un fichier de tests par module
├── donnees/                    ← biblio.db est créé ici automatiquement
└── .github/workflows/ci.yml    ← pipeline : lance pytest à chaque push/PR
```

Sens des appels : **Vue → Contrôleur → Modèle**. Le modèle ne connaît ni la vue
ni le contrôleur, et seule la vue fait des `print()` / `input()`.

## Répartition de l'équipe

| Membre | Fichier | Branche | Tests |
|---|---|---|---|
| A | `biblioiit/modele/regles.py` | `feature/regles` | `tests/test_regles.py` |
| B | `biblioiit/modele/modeles.py` | `feature/modeles` | `tests/test_modeles.py` |
| C | `biblioiit/modele/depot_sqlite.py` | `feature/base` | `tests/test_depot_sqlite.py` |
| D | `biblioiit/controleur/service.py` | `feature/service` | `tests/test_service.py` |
| E | `biblioiit/vue/console.py` | `feature/menu` | `tests/test_console.py` |

## Installation (Windows / PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

> Si PowerShell refuse d'activer le venv :
> `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`

## Lancer l'application

```powershell
python main.py            # interface graphique (onglets, souris, couleurs)
python main.py --simple   # menu console classique
```

Dans VS Code : **F5** (choisir « interface graphique »), ou menu
*Terminal › Exécuter la tâche… › BiblioIIT : lancer l'application*.

Adhérents de démonstration : `E2026-001` à `E2026-005`. Livres : `L001` à `L014`.

### L'interface graphique (inspirée d'Open Library)

| Onglet | Touche | Contenu |
|---|---|---|
| 🏠 Accueil | F1 | Tableau de bord : livres, disponibles, empruntés, retards, réservations |
| 📚 Catalogue | F2 | Recherche en direct, fiche du livre, boutons Emprunter / Réserver / Rendre |
| 👤 Mon compte | F3 | Emprunts d'un adhérent avec les jours restants, ses réservations |
| ⏰ Retards | F4 | Livres non rendus à temps |
| ⚙ Gestion | F5 | Ajouter / supprimer un livre, inscrire un adhérent, liste des adhérents |

Ctrl+T change le thème de couleurs et Ctrl+Q quitte l'application.

## Lancer les tests

```powershell
pytest -v
```

## Règles métier

- Durée d'un emprunt : **14 jours**
- Maximum **3 emprunts** en cours par adhérent
- Un livre déjà emprunté ne peut pas être emprunté à nouveau
- Un livre emprunté peut être **réservé** (file d'attente) ; à son retour,
  seul le premier de la file peut l'emprunter
- Un adhérent peut annuler sa réservation (onglet Mon compte)
- Un nouveau livre reçoit le code suivant (`L015`…) ; un nouvel adhérent
  le matricule suivant de l'année (`E2026-006`…)
- Un livre emprunté ou réservé ne peut pas être supprimé
- Formats : livre `L001`, matricule `E2026-001`
