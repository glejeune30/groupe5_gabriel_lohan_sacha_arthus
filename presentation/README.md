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
exécuté avec `llama3.2:3b`, température 0 **et graine fixée à 7**.
Sans graine, deux exécutions donnaient 38 % puis 12 % sur le même contrôle.

| Mesure | Résultat |
|---|---|
| Format respecté (3 points + Actions) | 100 % |
| Longueur ≤ 50 mots, v1 → v2 | 25 % → **100 %** |
| Juge vs test contradictoire | 4 contre 2 |
| Juge vs notes humaines | écart moyen 2,0 — accord 0/5 |
| Registre v1 → v2 | 100 % → 30 % de recouvrement |
| Rappel des action items | 88 % |

> **Incohérence restante à trancher.** `rendu_final_groupe5.ipynb` utilise encore
> `manual_scores = [5, 5, 5, 5, 5]`, le placeholder non rempli, et conclut donc que
> le juge est à peu près fiable — l'inverse de l'évaluation humaine réelle.
> En revanche son prompt court a été repris et remesuré ici : c'est lui qui fait
> passer la conformité de longueur de 25 % à 100 %.
