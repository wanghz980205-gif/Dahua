# Module CCTP · Contrôle d'accès (brouillon)

Usage : coller dans un CCTP / CCTP-sûreté en **langage de performance**, sans verrouiller une unique marque.  
Les modèles `DHI-…` ci-dessous sont des **équivalents** issus du catalogue Dahua Access Control V1.0 EN (2025-10-14) et de la table 0922.  
Ne pas inventer de numéros de pièce. Commande : modèle interne + `1.0.01.25.*`.

---

## 1. Architecture

Le système de contrôle d'accès sera de type **IP**, administrable depuis un logiciel central, avec conservation locale des droits sur les contrôleurs en cas de perte réseau.

Trois architectures acceptables selon la taille :

| Taille | Pilotage | Capacité indicative | Équivalent catalogue |
|---|---|---|---|
| 1 porte / accueil | Terminal autonome | jusqu'à quelques milliers d'usagers | `DHI-ASI6213J-MW` / `DHI-ASI3214A-W` |
| ≤ 40 portes, sans serveur | Contrôleurs web (série Insider) | 100 000 usagers / 500 000 événements | `DHI-ASC3202B` + lecteurs `ASR…` |
| ≤ 64 portes PME | SmartPSS Lite (Windows, gratuit) | 64 appareils | `DHI-ASC2204C-S` |
| Immeuble / site | DSS Pro | 500 terminaux / 1 000 portes, liaison vidéo et SSI | mêmes contrôleurs + DSS |

Le maître d'œuvre choisira l'architecture ; le titulaire justifiera la capacité (portes, usagers, historiques).

---

## 2. Fonctions minimales (toutes portes)

- Identification : badge, code, biométrie et **combinaisons** (selon la porte).
- Rôles : général, VIP, visiteur, ronde, **code sous contrainte (duress)**.
- 128 plages horaires et 128 calendriers jours fériés.
- Alarmes : porte maintenue, intrusion, duress, arrachement, **anti-passback**, seuil badges illégaux.
- Anti-passback et **interverrouillage multi-portes** sur les locaux sensibles.
- Entrées/sorties TOR : bouton de sortie, contact de porte, gâche / ventouse, report d'alarme.
- Journal d'événements horodaté, exportable.
- Ouverture pompiers / issue de secours selon le SSI du bâtiment (contact NF, déverrouillage à coupure ou selon consigne du CCTP SSI).

---

## 3. Lecteurs et badges

- Liaison lecteur ↔ contrôleur : **RS485** (jusqu'à 100 m, 1000 m si alimentation séparée) **ou** Wiegand 26/34.
- Lecteurs extérieurs : **IP66** après étanchéité silicone, plage −30 °C à +70 °C (série type `ASR2100A` / `ASR2200A`).
- Clavier : série type `ASR2101A`.
- Empreinte + badge : série type `ASR2102A` (3 000 empreintes).
- Double technologie IC/ID : série type `ASR2100A-ME` / `ASR2101A-ME`.

**Point d'attention France :** le catalogue export décrit surtout **MIFARE Classic 13,56 MHz** et Unique 125 kHz. Si le CCTP impose **MIFARE DESFire EV2/EV3** (fréquent en site sensible / APSAD), le titulaire devra **prouver** le lecteur et le badge DESFire réellement commandables ; ne pas assimiler Classic et DESFire.

---

## 4. Terminaux reconnaissance sans contact (si prescrit)

- Reconnaissance &lt; 0,3 s, capacité faces selon lot (1 500 à 100 000).
- Anti-usurpation photo/vidéo.
- Écran tactile, Mifare, RS485 / Wiegand, alarme.
- Indice IP65 sur les modèles extérieurs type `ASI6213J-MW`, `ASI7213X`.
- **RGPD / CNIL :** la biométrie faciale est un traitement à risque. Le CCTP doit limiter la finalité (accès physique), la durée de conservation des templates, l'information des personnes, et interdire le rapprochement avec un fichier de vidéoprotection sans base légale. Le logo « complies with GDPR » du catalogue ne suffit pas.

Ne pas prescrire les modèles **température frontale** (`…-T1` / `…-FT1`) sauf besoin sanitaire explicite.

---

## 5. Contrôleurs multi-portes

Équivalents :

- 2 portes 1 sens : `DHI-ASC2202B-S` / `ASC2202C-S`
- 2 portes 2 sens : `DHI-ASC2202B-D` / `ASC2202C-D`
- 4 portes 1 sens : `DHI-ASC2204B-S` / `ASC2204C-S` — `1.0.01.25.11413-9001`
- 8 portes : `DHI-ASC2208C-S`

Capacité catalogue : 100 000 usagers, 500 000 événements, Ethernet 10/100.

---

## 6. Supervision

- **SmartPSS Lite** : jusqu'à 64 appareils ; CCTV + accès + présence + interphonie ; ouverture à distance ; SDK.
- **DSS Pro** : jusqu'à 1 000 portes ; liaison caméra sur événement d'accès ; report incendie ; clients multiples.

Les images d'accès sont des données personnelles (RGPD). Durée d'enregistrement alignée sur la vidéoprotection du site.

---

## 7. Tourniquets (gares, sièges, industriels)

- Trepied extérieur type `ASGG5xxT` (MCBF ≥ 3 000 000, −25 °C à +70 °C).
- Battant / swing type `ASGB6` / `ASGB8` (MCBF ≥ 5 000 000, 10–20 paires IR, passage 600 mm, PMR jusqu'à 1 000–1 200 mm).
- Modes : 9 modes de passage, anti-queue, anti-intrusion, déverrouillage incendie.

---

## 8. Serrures (lots complémentaires)

Ventouses 280/500 kg type `DHI-ASF280A` / `ASF500A` (matériel `1.2.01.27.*`), gâches, pênes. Alimentation 12/24 V, −30 °C à +60 °C. Issue de secours conforme au règlement de sécurité.

---

## 9. Câblage

- IP : cat. 5e minimum entre contrôleurs, switch et serveur.
- RS485 et TOR en câble adapté, distance lecteurs selon §3.
- PoE possible sur certaines architectures Insider (alimentation gâche à valider : souvent 12 V séparée).

---

*Brouillon à relire avec la liste France/EUR et les certificats CNPP/CE. Ne pas figer la marque dans le CCTP public.*
