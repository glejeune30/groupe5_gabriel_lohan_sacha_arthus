# Présentation — Projet 5

Support de soutenance : 13 plans de travail en 1920×1080, groupés par section.

## Plan

| Section | Plans |
|---|---|
| Ouverture | `Main` |
| Business | `Business-1` (l'enjeu), `Business-2` (trois leviers) |
| Data | `Data-1` (le corpus), `Data-2` (vérité terrain) |
| Code & prompts | `Code-1` (pipeline), `Code-2` (le prompt), `Code-3` (itération v1/v2), `Code-4` (le juge) |
| Évaluation | `Eval-1` (format et longueur), `Eval-2` (le juge contre nous), `Eval-3` (registre, rappel, reproductibilité) |
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

Ils proviennent de [../05_controllable_summarizer.ipynb](../05_controllable_summarizer.ipynb),
exécuté avec `llama3.2:3b`, température 0 et graine fixée à 7.

| Mesure | Résultat |
|---|---|
| Format (3 points + Actions) | 100 % |
| Longueur ≤ 50 mots, v1 → v2 | 25 % → **100 %** |
| Juge : fidèle vs falsifié | 4 contre 2 |
| Juge vs nos notes humaines | écart moyen 2,0 — accord exact 0/5 |
| Registre v1 → v2 | 100 % → 30 % de recouvrement |
| Rappel des action items | 88 % |

**Le résultat central.** Le juge LLM repère une falsification grossière mais valide
une invention plausible : il met 5/5 aux documents 4 et 5, dont les sections
`Actions:` contiennent des décisions que personne n'a prises. Seule la confrontation
à un jugement humain l'a révélé — le test automatique seul donnait une fausse assurance.

**Reproductibilité.** Deux exécutions à température 0 donnaient 38 % puis 12 % sur le
même contrôle : Ollama tire une graine aléatoire à chaque appel. La graine est
désormais fixée, et les 5 résumés notés à la main sont gelés dans
[../data/scored_summaries.json](../data/scored_summaries.json).

> **Incohérence à trancher.** `rendu_final_groupe5.ipynb` utilise encore
> `manual_scores = [5, 5, 5, 5, 5]`, le placeholder non rempli, et conclut donc que
> le juge est à peu près fiable — l'inverse de l'évaluation humaine réelle. Son
> prompt court a en revanche été repris et remesuré : c'est lui qui fait passer la
> conformité de longueur de 25 % à 100 %.
