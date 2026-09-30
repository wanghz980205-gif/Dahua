# Module CCTP · Vidéosurveillance Wi-Fi / 4G / batterie (brouillon)

Ce n'est **pas** le module des caméras IP filaires NF EN 62676 pour gare, métro ou CSU.  
Usage : petits sites, habitat, chantier temporaire, retail. Modèles = équivalents 0922, pas un verrouillage de marque.

---

## 1. Quand l'écrire

- Site sans fourreaux, bâtiment existant, location courte, commerce.  
- Pas en substitution d'un réseau PoE dimensionné (Egis / Ingérop / Systra).

Trois familles catalogue Dahua Wireless 2026-06 : **indoor**, **outdoor Wi-Fi**, **4G**.

---

## 2. Exigences minimales (si le CCTP accepte le sans-fil)

- Enregistrement local (carte SD dont la compatibilité est justifiée) **et/ou** NVR / cloud selon le lot.  
- Chiffrement du flux et du stockage ; mot de passe unique ; pas de compte usine.  
- Alimentation : 12 V / PoE / batterie / panneau — le titulaire joint le calcul d'autonomie (le GKS a une table « Low Power Consumption Camera Endurance Time »).  
- 4G : SIM M2M, bande EU, volume data, reprise sur coupure. Le suffixe interne `NL668` / `EAU` désigne le module + région, pas un autre appareil.  
- Hors gel / IP selon pose (extérieur IP66 analogue aux IPC filaires de même usage).  
- RGPD : mêmes règles que la vidéoprotection filaire (finalité, durée, information, pas de reconnaissance faciale sans base).

---

## 3. Équivalents 0922 (Europe, à filtrer par liste France)

| Usage | Modèle externe | Pièce |
|---|---|---|
| Intérieur Hero | `DH-H3JE` | `1.0.01.04.48317-9901` |
| Cube intérieur dissuasion | `DH-F5D-PV` | `1.0.01.04.45447-9001` |
| Dôme Wi-Fi + dissuasion | `DH-IPC-HDW1539DA-SW-PV` | `1.0.01.04.45395-9001` |
| Tube Wi-Fi | `DH-IPC-HFW1339DTK1-SW-PV` | `1.0.01.04.45380-9001` |
| PTZ batterie | `DH-P3AE-PV` | `1.0.01.07.15562-9002` |
| Tube 4G | `DH-IPC-HFW2441DG-4G-SP-B-MAX` | `1.0.01.04.45462-9001` |
| Batterie 4G | `DH-BP4A-4G` | `1.0.01.04.46128` |

`BP6X` apparaît dans le pack GKS mais **pas** dans 0922 : ne pas inventer de numéro de pièce.

Suffixes : `SW` = Wi-Fi ; `4G` = cellulaire ; `PV` = dissuasion sonore/lumineuse ; `IL` = double éclairage ; `EUR` = variante de commande Europe.

---

## 4. Ce qu'il ne faut pas écrire

- Ne pas présenter une caméra batterie comme système principal d'une gare.  
- Ne pas promettre une autonomie sans la feuille de calcul GKS.  
- Ne pas confondre `SW` (Wi-Fi) et `SAW` (variante Wi-Fi, souvent IL) : ce sont deux SKU.

*Brouillon. Recoller le lien GKS non expiré pour caler le texte sur le catalogue 2026-06.*
