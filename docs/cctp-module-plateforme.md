# Module CCTP · Plateforme de supervision (brouillon)

Usage : coller dans un CCTP / CCTP-sûreté en **langage de performance**.  
Les modèles `DHI-DSS…` / `DSS8…` sont des **équivalents** 0922, pas un verrouillage de marque.  
Ne pas inventer de numéros de pièce. Commande : modèle interne + `1.0.01.13.*` (matériel) et `2.9.02.07.*` (licences DSS8).

Les tableaux GKS « DSS Selection V8.8 » restent chiffrés IRM.  
Les **capacités** ci-dessous viennent de la liste de comparaison DSS **V8.5.0** (pack Basic Information).  
`DSS8PRVB` inclut **16 canaux vidéo** ; `DSS8PRDB` inclut **16 portes** (License Quick Guide V8.6).

---

## 1. Architecture

Le site disposera d'une **plateforme IP unique** pour la vidéoprotection, le contrôle d'accès et, le cas échéant, l'anti-intrusion et l'interphonie. Les droits restent applicables sur les contrôleurs / NVR en cas de perte du serveur.

Quatre niveaux catalogue (ne pas mélanger logiciel Windows et appliance Linux) :

| Taille | Pilotage | Ordres de grandeur V8.5 | Équivalent |
|---|---|---|---|
| Petit site | Express logiciel (Windows) | 64 ou 256 canaux selon gratuit / licencié | licences `DSS8EX…` |
| Immeuble | Appliance Linux `DSS7016D/DR-S2` / `DSS7116D/DR` | 500 appareils / 1 000 canaux (un serveur) ; 600 appareils / 1 500 portes | `1.0.01.13.*` + `DSS8PRVB` + N×`DSS8PRV` |
| Site / campus | DSS Professional (Windows) | 1 000 / 2 000 en standalone ; 10 000 / 20 000 en multi-serveurs ; 1 500 appareils / 3 000 portes | mêmes licences Pro |
| Plusieurs sites | Professional + cascade / multi-sites + option hot-standby | `DSS8PRMS` ; `DSSHOTSTANDBY` `2.3.01.01.10131` | |

`DHI-DSS4004-S2` n'est **pas** dans les colonnes de cette comparaison : ne pas lui attribuer les chiffres 7116/7016.

Le maître d'œuvre fixe le nombre de **canaux vidéo**, de **portes**, de **centrales d'alarme** et de **postes client**. Le titulaire produit la matrice de licences (base ≠ canal).

**IVSS** (`DHI-IVSS5108-1I`, `DHI-IVSS7108-1I-V2`, `DHI-IVSS7116…`, famille `1.0.01.23`) est un enregistreur analytique de bord, **pas** le serveur de supervision.

---

## 2. Fonctions minimales

- Enregistrement et restitution des flux vidéo selon le lot vidéoprotection (NF EN 62676).  
- Liaison **événement d'accès ↔ caméra** (ouverture, forçage, duress).  
- Report **anti-intrusion** et, si prescrit, **SSI / incendie**.  
- Clients multiples (PC / mobile), journaux horodatés, profils opérateurs.  
- Horodatage NTP ; sauvegarde de configuration ; restauration documentée.

**SIA ADM-CID / DCS** (réception) : prévu uniquement sur **DSS Professional Windows**, pas sur l'appliance Linux ni Express.  
Poussée d'événements vers un centre : licence `DSS8PRSIA` (`2.9.02.07.10157`).

Modules 0922 à n'exiger que s'ils sont au CCTP : stationnement `DSS8PRPML`, visiteurs `DSS8PRVML`, analyse vidéo `DSS8PRVAML`.

---

## 3. Licences (DSS 8)

Ne pas confondre édition et type de canal :

| Code externe | Rôle | Pièce |
|---|---|---|
| `DSS8EXV` / `DSS8EXD` / `DSS8EXAL` / `DSS8EXVDP` | Express : vidéo / porte / alarme / interphonie | `2.9.02.07.10006` … `10009` |
| `DSS8PRVB` / `DSS8PRDB` | Pro : bases vidéo / porte (**16 canaux / 16 portes** inclus) | `2.9.02.07.10011` / `10012` |
| `DSS8PRV` / `DSS8PRD` / `DSS8PRAL` / `DSS8PRVDP` | Pro : canaux / dispositifs | `2.9.02.07.10013` … `10016` |
| `DSS8EX-PR-V` | Passage Express → Pro (vidéo) | `2.9.02.07.10027` |
| `DSS8UTV` / `DSS8PR-UT-V` | Ultimate / passage Pro → Ultimate | `2.9.02.07.10231` / `10288` |

Une centrale d'alarme sous DSS consomme une licence **AL**, pas un canal **V**.

---

## 4. Analyse (si prescrite)

- Analyse **au bord** : IVSS (cartes `-nI`) ou caméras.  
- Analyse **centrale** type IVS (`DHI-IVS-F7500…`, `TB8000…`) : les P/N GKS `1.0.01.18.*` **ne figurent pas** dans 0922. Le titulaire ne les commandera que s'ils existent au tarif France.  
- **RGPD / CNIL** : reconnaissance faciale ou comportementale = traitement à risque. Finalité, durée, information, pas de fusion avec le fichier d'accès sans base légale.  
- Les serveurs « prisoner behavior » (`IVS-IP8000`) sont **hors scope** d'un CCTP civil français.

---

## 5. Exploitation

- Postes CSU : profils distincts (opérateur / chef de poste / administrateur).  
- Si report vers un centre de télésurveillance : protocole documenté (SIA ou équivalent), pas seulement un flux vidéo.  
- Cyber : comptes nominatifs, pas de mot de passe usine, journalisation (ANSSI vidéoprotection).  
- Preuve cyber catalogue : **ETSI EN 303 645** LCIE (25/05/2023) pour DSS Professional / Express — ce n'est **pas** un certificat CNPP / APSAD. Le certificat TÜV « privacy IoT » 2020 est **expiré**.

---

*Brouillon à relire avec la liste France/EUR. Capacités = comparaison V8.5, pas la sélection V8.8 chiffrée. Ne pas figer la marque dans le CCTP public.*
