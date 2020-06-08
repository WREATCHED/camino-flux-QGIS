# PLUGIN QGIS Camino

---           

## Technologies
- [Python 3.x]

---           

## Environnement
 - Version de QGIS 3.12.0-București ( fonctionne en 3.x )
 - Qt 5.11.2 
 - OS Version Windows 10 (10.0)

---

## Installation
### Automatiquement
L’application se trouve sur la ressource du département MSP/DS/GSG (http://piece-jointe-carto.developpement-durable.gouv.fr/NAT002/QGIS/plugins/plugins.xml)
et est donc accessible via le menu Extension : Installer / Gérer les extensions.
Camino pourra être installé, mis à jour via ce dispositif.

### Manuellement
Soit décompresser le fichier zippé (camino3.zip – mdp « qgis_dl ») qui comprend l’ensemble de l’application et de la recopier :
 - Pour les packages DS/GSG sous : "C:\ProgramFiles\QGIS\profil\python\camino3"
 - Pour la version communautaire sous "MonProfilAMoi\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\camino3"

---

## Documentation
La documentation [est disponible ici](https://github.com/MTES-MCT/camino-flux-QGIS/blob/master/doc/camino_doc.pdf).

---

## Structure des fichiers

.                        # `Racine où se trouve les sources .py`
│
├── doc                  # `documentation et flyer`
├── i18n                 # `fichiers des langues
└── icons                # `icones de l'application, menu, barre d'outils, IHM`
    └── metier           # `icones de la boite de dialogue de filtre`
└── requete              # `dossier par défaut de sauvegarde et de chargement des requetes (filtres)`

---

## Crédits

### Production

- [La Fabrique Numérique, Ministère de la transition écologique et solidaire](https://www.ecologique-solidaire.gouv.fr/inauguration-fabrique-numerique-lincubateur-des-ministeres-charges-lecologie-et-des-territoires)

### Équipe

- Didier LECLERC, CMSIG développeur MTES/MCTRCT SG/SNUM/UNI/DRC
- Nicolas PETITOT, Appui métier

---

## Licence

Camino API, le cadastre minier numérique ouvert

[AGPL 3 ou plus récent](https://spdx.org/licenses/AGPL-3.0-or-later.html)
