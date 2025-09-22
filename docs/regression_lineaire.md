# Galerie — Descente de gradient (Pourquoi > Comment)

> Chaque figure illustre le « pourquoi » de l’étape.
> Les images sont **générées par script** (cf. `scripts/gen_plots.py`).

## Étape 1 — Données brutes
![Données brutes](./plots/etape1_donnees_brutes.png)
*Pourquoi : relier km → prix pour prédire et négocier.*

## Étape 2 — Point de départ
![Droite initiale](./plots/etape2_droite_initiale.png)
*Pourquoi : partir simple pour laisser les données corriger.*

## Étape 3 — Droites successives
![Droites successives](./plots/etape3_droites_successives.png)
*Pourquoi : les grands km dictent la pente au début.*

## Étape 4 — Erreurs initiales
![Erreurs initiales](./plots/etape4_erreurs_initiales.png)
*Pourquoi : J(θ) ∝ somme des flèches au carré.*

## Étape 5 — Erreurs finales
![Erreurs finales](./plots/etape5_erreurs_finales.png)
*Pourquoi : moins de flèches ⇒ moindre coût global.*

## Étape 6 — Évolution de θ0
![θ0 vs itérations](./plots/etape6_theta0_vs_iter.png)
*Pourquoi : l’intercept bouge moins que la pente.*

## Étape 7 — Évolution de θ1
![θ1 vs itérations](./plots/etape7_theta1_vs_iter.png)
*Pourquoi : normaliser permet un α plus grand.*

## Étape 8 — Coût J(θ)
![J(θ) vs itérations](./plots/etape8_cout_vs_iter.png)
*Pourquoi : échelle équilibrée ⇒ pas de zigzag.*
