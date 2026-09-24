# Module CCTP · Plateforme de supervision (brouillon)

Usage : coller dans un CCTP / CCTP-sûreté en **langage de performance**.  
Les modèles `DHI-DSS…` / `DSS8…` sont des **équivalents** 0922, pas un verrouillage de marque.  
Ne pas inventer de numéros de pièce. Commande : modèle interne + `1.0.01.13.*` (matériel) et `2.9.02.07.*` (licences DSS8).

Les tableaux GKS « DSS Selection V8.8 » sont chiffrés IRM : **ne pas recopier de capacités non sourcées**. La mention 500 terminaux / 1 000 portes vient du catalogue Access Control V1.0 EN (2025-10-14), pour DSS Pro.

---

## 1. Architecture

Le site disposera d'une **plateforme IP unique** pour la vidéoprotection, le contrôle d'accès et, le cas échéant, l'anti-intrusion et l'interphonie. Les droits restent applicables sur les contrôleurs / NVR en cas de perte du serveur.

Trois niveaux acceptables :

| Taille | Pilotage | Équivalent catalogue |
|---|---|---|
| Petit site / tertiaire | Appliance compacte + licences Express | `DHI-DSS4004-S2` + `DSS8EXV` / `DSS8EXD` / `DSS8EXAL` |
| Immeuble / campus / gare | Appliance Pro + bases et canaux | `DHI-DSS7016D-S2` ou `DHI-DSS7016DR-S2` / `DHI-DSS7116DR` + `DSS8PRVB` + N×`DSS8PRV` |
| Plusieurs sites | Idem + cascade / multi-sites | `DSS8PRCAS` (`2.9.02.07.10034`) et/ou `DSS8PRMS` |

Le maître d'œuvre fixe le nombre de **canaux vidéo**, de **portes**, de **centrales d'alarme** et de **postes client**. Le titulaire produit la matrice de licences (base ≠ canal).

**IVSS** (`DHI-IVSS5108-1I`, `DHI-IVSS7108-1I-V2`, `DHI-IVSS7116…`, famille `1.0.01.23`) est un enregistreur analytique de bord, **pas** le serveur de supervision. Il peut alimenter la plateforme ; il ne la remplace pas.

---

## 2. Fonctions minimales

- Enregistrement et restitution des flux vidéo selon le lot vidéoprotection (NF EN 62676).  
- Liaison **événement d'accès ↔ caméra** (ouverture, forçage, duress).  
- Report **anti-intrusion** et, si prescrit, **SSI / incendie**.  
- Clients multiples (PC / mobile), journaux horodatés, profils opérateurs.  
- Horodatage NTP ; sauvegarde de configuration ; restauration documentée.

Modules 0922 à n'exiger que s'ils sont au CCTP : stationnement `DSS8PRPML`, visiteurs `DSS8PRVML`, analyse vidéo `DSS8PRVAML`, protocole **SIA** `DSS8PRSIA` (télésurveillance / CSU).

---

## 3. Licences (DSS 8)

Ne pas confondre édition et type de canal :

| Code externe | Rôle | Pièce |
|---|---|---|
| `DSS8EXV` / `DSS8EXD` / `DSS8EXAL` / `DSS8EXVDP` | Express : vidéo / porte / alarme / interphonie | `2.9.02.07.10006` … `10009` |
| `DSS8PRVB` / `DSS8PRDB` | Pro : bases vidéo / porte | `2.9.02.07.10011` / `10012` |
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
- Cyber : comptes nominatifs, pas de mot de passe usine, journalisation des accès à la plateforme (aligné ANSSI vidéoprotection).

---

*Brouillon à relire avec la liste France/EUR et le tableau de licences DSS 8.8 non chiffré. Ne pas figer la marque dans le CCTP public.*
