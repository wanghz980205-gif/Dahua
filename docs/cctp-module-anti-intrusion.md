# Module CCTP · Anti-intrusion (brouillon)

Usage : coller dans un CCTP / CCTP-sûreté en **langage de performance**.  
Modèles `DHI-ARC…` / `ARD…` = équivalents 0922 et catalogue Access Control (p. 59–63), pas un verrouillage de marque.  
Commande : modèle interne + `1.0.01.19.*`. **Ne pas inventer de numéro de pièce.**

Le fichier GKS « Alarm Product Selection 20260804 » est chiffré IRM : capacités détaillées (zones, utilisateurs) **non recopiées**. La mention EN 50131 Grade 2 pour `ARC3008C` vient du catalogue Access 2025.

---

## 1. Fréquence et architecture (France)

Pour tout système **sans fil**, la bande utilisée en France est **868 MHz**. Les équivalents catalogue portent le suffixe **`W2(868)`** (radio), **`FW2(868)`** (Wi-Fi + radio) ou **`GW2(868)`** (cellulaire + radio).  
Ne pas prescrire de centrale 433 MHz.

Deux architectures acceptables :

| Type | Usage | Équivalent |
|---|---|---|
| Sans fil résidentiel / petit tertiaire | Hub + détecteurs + sirène + clavier | `DHI-ARC3000H-W2(868)` ou `DHI-ARC3800H-FW2(868)` ; kit `DHI-ART-ARC3800H-03-FW2(868)` |
| Filaire / local technique | Centrale bus, Grade 2 catalogue | `DHI-ARC3008C` (`1.0.01.19.10457`) ; 16 zones type `DHI-ARC2016C` / `DHI-ARC9016C` |

Le maître d'œuvre choisit filaire / radio / hybride. Le titulaire justifie la couverture radio (répéteurs `ARA43` / `ARA46-N`) et l'alimentation de secours.

Liaison à la plateforme de supervision : licence d'alarme DSS (`DSS8EXAL` / `DSS8PRAL`), distincte des canaux vidéo.

---

## 2. Fonctions minimales

- Armement / désarmement total et partiel (clavier, badge, télécommande, application selon le lot).  
- Zones : intrusion, 24 h, incendie/technique si prescrit, inhibitions journalisées.  
- Transmissions : IP ; option cellulaire sur les hubs `GW2`.  
- Sirène intérieure et, en extérieur, sirène IP65 analogue `ARA13`.  
- Journal d'événements horodaté, exportable.  
- Report vers télésurveillance si le CCTP l'exige (protocole à nommer ; côté plateforme voir `DSS8PRSIA`).

---

## 3. Détecteurs (équivalents 868, rôles d'après 0922 / alias OEM)

| Usage | Modèle externe | Pièce |
|---|---|---|
| Contact d'ouverture | `DHI-ARD323-W2(868)` | `1.0.01.19.10551` |
| Contact longue portée | `DHI-ARD333-W2(868S)` | `1.0.01.19.10989-9001` |
| Volumétrique PIR | `DHI-ARD1233-W2(868)` | `1.0.01.19.10555-0078` |
| Double technologie | `DHI-ARD2231-W2(868)` | `1.0.01.19.10640-0003` |
| Bris de glace | `DHI-ARD512-W2(868)` | `1.0.01.19.10784-0002` |
| Extérieur | `DHI-ARD2251E-W2(868)` | `1.0.01.19.10815-9002` |
| Extérieur + capture | `DHI-ARD2251E-W2(868V)` | `1.0.01.19.10829-9001` |
| Inondation | `DHI-ARD912-W2(868D)` | `1.0.01.19.10695-9001` |

Clavier `DHI-ARK30T-W2(868)` / LCD `DHI-ARK30C-RW2(868)`. Télécommande `DHI-ARA24-W2(868)`. Extension E/S `DHI-ARM310-W2(868)`.

Les alias `WCENT`, `WPIRDET`, `WDCONT` du 0922 sont des **noms OEM**, pas à écrire dans le CCTP.

---

## 4. Conformité France (à faire prouver)

- **EN 50131** : le catalogue Access indique Grade 2 pour `ARC3008C`. Le titulaire joint la déclaration et le grade réellement commandé.  
- **APSAD R82 / CNPP** : **non démontré** par ce pack GKS. Si le CCTP impose une centrale certifiée, le titulaire produit l'attestation CNPP du matériel livré — ne pas assimiler EN 50131 et certification APSAD.  
- Détecteurs d'incendie radio (`DHI-HY-SA21A-W2(868)`, famille `1.0.01.36`) : lot SSI distinct, pas un substitut de l'intrusion.

---

## 5. Ce qu'il ne faut pas écrire

- Ne pas mélanger 868 (France) et 433.  
- Ne pas présenter un kit `ART-ARC3800H` comme centrale de site industriel classé.  
- Ne pas copier un tableau de zones depuis une sélection Excel illisible.  
- Ne pas écrire « certifié CNPP » sans tableau interne.

---

*Brouillon à relire avec la liste France/EUR et les certificats CNPP. Ne pas figer la marque dans le CCTP public.*
