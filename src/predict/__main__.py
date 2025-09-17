# Point d'entrée CLI du paquet. Contrat global et E/S stdout.
"""Command-line entry point for the predict package."""

# Empêche la mutation de cette ligne en tests mutationnels.
# Diffère l'évaluation des annotations. Réduit couplage/temps import.
# pragma: no mutate
from __future__ import annotations

# Import local. Contrats: parse_args peut quitter, predict_price est pure.
import math

from .predict import parse_args, predict_price


# Point d'entrée CLI. Retourne un code process (0 succès).
def main(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Parse arguments, run the prediction and print the result.

    Pourquoi :
        - Laisser remonter SystemExit depuis parse_args rend les échecs d’usage
          explicites et conformes aux attentes CLI (Sonar S5754 satisfait).
        - Retourner un int uniquement en cas de succès garde une lecture simple :
          si on arrive ici, on est dans le chemin “OK”.
    """

    # On laisse parse_args gérer les erreurs d’usage via SystemExit(2)
    # plutôt que d’intercepter et de transformer l’exception (meilleure
    # visibilité côté shell/CI et conformité aux conventions Unix).
    km, theta_value = parse_args(argv)

    # Défense interne : parse_args garantit un str, mais si un bug
    # ou un appel incohérent casse ce contrat, on arrête immédiatement.
    theta_candidate: object = theta_value
    if not isinstance(theta_candidate, str):  # pragma: no cover
        raise SystemExit(2)

    theta: str = theta_candidate

    # On calcule la prédiction à partir des coefficients persistés
    price = predict_price(km, theta)

    # On affiche un résultat minimal et stable :
    # - "0" explicite en cas de modèle non entraîné
    # - sinon un prix formaté lisible et parsable
    if math.isclose(price, 0.0, abs_tol=1e-12):
        print("0")
    else:
        print(f"Predicted price: {price:.2f} €")
    return 0


# Exécution directe du module. Ne s'exécute pas à l'import.
if __name__ == "__main__":  # pragma: no cover - module glue
    # Transmet le code de main au shell via SystemExit.
    raise SystemExit(main())  # pragma: no mutate
