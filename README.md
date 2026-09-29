# Projet 5 - Résumeur contrôlable

Groupe 5 - Gabriel, Lohan, Sacha, Arthus.

Un résumeur de transcriptions de réunion dont on contrôle l'audience, la longueur
et le format, évalué par des contrôles automatiques et un juge LLM validé.

## Contenu

| Fichier | Rôle |
|---|---|
| `05_controllable_summarizer.ipynb` | Le notebook complet : prompts, évaluation, résultats |
| `data/transcripts.jsonl` | 8 transcriptions, avec `reference_summary` et `action_items` |

## Prérequis

Le notebook réutilise les helpers du cours (`utils.ask`, `utils.count_tokens`).
Le dépôt `langchain_courses` doit donc être cloné **à côté** de celui-ci :

```
GitHub/
├── langchain_courses/
└── groupe5_gabriel_lohan_sacha_arthus/   ← ce dépôt
```

Le chemin est résolu automatiquement : le notebook remonte l'arborescence jusqu'à
trouver `langchain_courses/prompt-engineering-course`.

Modèle utilisé : **`llama3.2:3b`** via Ollama local, température 0 pour que
l'évaluation soit reproductible.

```bash
ollama pull llama3.2:3b
```

## Ce que fait le notebook

1. **Contrat de format explicite** : 3 bullets + une section `Actions:`, et surtout
   des contrôles qui vérifient que le modèle obéit.
2. **Contrôles automatiques** sur les 8 documents : longueur et format, en pass/fail.
3. **Juge LLM de fidélité**, tolérant au bruit de formatage d'un petit modèle
   (extraction du JSON + seconde tentative).
4. **Validation du juge** par un test contradictoire objectif (résumé fidèle contre
   résumé falsifié) et par comparaison avec nos propres notes.
5. **Itération mesurée sur l'audience** : v1 (audience nommée) contre v2 (consignes
   de registre explicites), avec la même mesure de part et d'autre.
6. **Rappel des `action_items`** contre la vérité terrain du jeu de données.

## Résultats (llama3.2:3b, 8 transcriptions)

| Mesure | Résultat |
|---|---|
| Format respecté (3 bullets + Actions) | 100 % |
| Longueur ≤ 50 mots | 38 % (médiane : 54 mots) |
| Juge : résumé fidèle vs falsifié | 4 contre 2 |
| Juge vs nos notes humaines | écart moyen 2,0 - accord exact 0/5 |
| Registre v1 (audience nommée) | 100 % de recouvrement - aucun effet |
| Registre v2 (consignes explicites) | 24 % de recouvrement |
| Rappel des action items | 94 % |

**À retenir.** Le modèle suit parfaitement une contrainte *structurelle* mais mal une
contrainte *quantitative* : compter des mots n'est pas une opération que le décodage
effectue. Et une consigne d'audience purement nominale ne change rien à la sortie -
seule une consigne qui dit *quoi changer* fonctionne.

## Le juge LLM n'est pas fiable seul

C'est le résultat central du projet. Le test contradictoire était rassurant (4 contre 2
face à un résumé grossièrement falsifié), mais confronté à nos propres notes le juge
s'effondre : écart moyen de 2 points, aucun accord exact sur 5 documents.

Il attribue 5/5 aux documents 4 et 5, dont les sections `Actions:` contiennent des
décisions que personne n'a prises. Il repère donc une contradiction voyante mais valide
sans broncher une invention plausible - exactement le cas dangereux en production.

Un juge validé uniquement par un test automatique aurait donné une fausse assurance :
c'est la confrontation à un jugement humain qui révèle le problème.
