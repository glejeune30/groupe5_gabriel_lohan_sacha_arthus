# Présentation — Projet 5

Support de soutenance : 14 plans de travail en 1920×1080, groupés par section.

## Plan

| Section | Plans |
|---|---|
| Ouverture | `Main` |
| Business | `Business-1` (l'enjeu), `Business-2` (trois leviers) |
| Data | `Data-1` (le corpus), `Data-2` (vérité terrain) |
| Code & prompts | `Code-1` (pipeline), `Code-2` (le prompt), `Code-3` (itération v1/v2), `Code-4` (le juge) |
| Évaluation | `Eval-1` (format, longueur, actions), `Eval-2` (le juge contre nous), `Eval-3` (registre, reproductibilité) |
| Sécurité | `Securite` (injection de prompt et garde-fou) |
| Conclusion | `Conclusion` |

L'ordre et la position de chaque plan sur le canevas sont dans [canvas.json](canvas.json).

## Direction artistique

- **Typographies** — Instrument Serif (display), IBM Plex Sans (texte), JetBrains Mono (chiffres et code).
- **Palette** — ivoire `#F6F3EC`, encre `#191714`, accent terre cuite `#C2542B`, secondaire `#1F4D52`.
- Alternance de fonds clairs et sombres entre les sections ; la slide du juge est en pleine terre cuite.

## Comment les ouvrir

Les fichiers `boards/*.dc.html` sont les sources des plans de travail. Ils
référencent `./support.js`, fourni par l'éditeur : **ouverts directement dans un
navigateur depuis ce dépôt, ils ne s'afficheront pas correctement**. Ils sont ici
comme archive et pour le suivi des versions.

## Chiffres présentés

Ils proviennent de [../rendu_final_groupe5.ipynb](../rendu_final_groupe5.ipynb),
exécuté avec `llama3.2:3b`, température 0 et graine fixée à 7.

| Mesure | Résultat |
|---|---|
| Format (3 puces + Actions) | 8/8 |
| Longueur ≤ 50 mots | 8/8 |
| Juge : résumés infidèles détectés | 10/15 — faits inversés 5/5, actions inventées 1/5 |
| Juge vs nos notes humaines | écart moyen 1,40 — accord exact 1/5 |
| Registre : vocabulaire commun v1 → v2 | 75 % → 52 % |
| Actions : rappel / précision | 81 % / 60 % |
| Sécurité : injections réussies | 3/5 → 1/5 |

**Le résultat central.** Le juge repère les faits inversés 5 fois sur 5, mais les actions
inventées seulement 1 fois sur 5. Il note 4 et 5 les résumés des documents 4 et 5, que nous
avions notés 2 et 1 à cause d'actions que personne n'a décidées. Il voit une contradiction
voyante, pas une invention plausible — et c'est exactement la faille qu'exploite l'injection
de prompt.

**Reproductibilité.** Deux exécutions à température 0 donnaient 38 % puis 12 % sur le
même contrôle : Ollama tire une graine aléatoire à chaque appel. La graine est
désormais fixée, et les 5 résumés notés à la main sont gelés dans
[../data/human_scores.jsonl](../data/human_scores.jsonl).

Le prompt court proposé par Gabriel est intégré au rendu : viser 30 mots pour un budget
de 50, avec un gabarit rigide, fait tenir la contrainte de longueur sur les 8 documents.

La section sécurité et les 20 cas adversariaux du juge viennent du travail de Lohan.
