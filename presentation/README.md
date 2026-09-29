# Présentation — Projet 5

Support de soutenance, 13 slides, calibré pour 10-12 minutes.

## Plan

| Section | Slides |
|---|---|
| Ouverture | `cover` |
| Business | `business-enjeu`, `business-usage` |
| Data | `data-corpus`, `data-verite` |
| Code & prompts | `code-pipeline`, `code-prompt`, `code-audience`, `code-juge` |
| Évaluation | `eval-format`, `eval-juge`, `eval-registre` |
| Conclusion | `conclusion` |

L'ordre de lecture est donné par `order` dans [deck.json](deck.json).

## Contenu

Chaque fichier de `slides/` contient une slide (format 1920×1080, styles en ligne).
Les **notes d'orateur** sont dans la balise `<aside>` en fin de chaque slide : elles
détaillent ce qui est dit et pourquoi chaque chiffre est ce qu'il est.

## Chiffres présentés

Ils proviennent de [../05_controllable_summarizer.ipynb](../05_controllable_summarizer.ipynb),
exécuté avec `llama3.2:3b` à température 0.

| Mesure | Résultat |
|---|---|
| Format respecté (3 points + Actions) | 100 % |
| Longueur ≤ 50 mots | 38 % (médiane 54) |
| Juge vs test contradictoire | 4 contre 2 |
| Juge vs notes humaines | écart moyen 2,0 — accord 0/5 |
| Registre v1 → v2 | 100 % → 24 % de recouvrement |
| Rappel des action items | 94 % |

> **Attention, incohérence à trancher.** `rendu_final_groupe5.ipynb` utilise
> `manual_scores = [5, 5, 5, 5, 5]`, c'est-à-dire le placeholder non rempli. Il
> conclut donc que le juge est à peu près fiable, alors que l'évaluation humaine
> réelle du notebook ci-dessus montre l'inverse. Les deux notebooks ne peuvent pas
> être présentés ensemble en l'état.
