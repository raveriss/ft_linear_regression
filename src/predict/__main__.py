# Point d'entrée CLI du paquet. Contrat global et E/S stdout.
"""Command-line entry point for the predict package."""

# Empêche la mutation de cette ligne en tests mutationnels.
# Diffère l'évaluation des annotations. Réduit couplage/temps import.
# pragma: no mutate
from __future__ import annotations

# Import local. Contrats: parse_args peut quitter, predict_price est pure.
from .predict import parse_args, predict_price


# Point d'entrée CLI. Retourne un code process (0 succès).
def main(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Parse arguments, run the prediction and print the result."""
    # Barrière d'erreurs. Laisse remonter SystemExit avec son code.
    try:
        # Pré: argv list[str]|None. Peut lire sys.argv si None.
        # Effet: parse_args peut faire sys.exit en cas d'usage invalide.
        # Post: km>=0 float. theta est un chemin str vers le fichier.
        km, theta = parse_args(argv)

        # Défense interne (utile pour mutation testing) :
        # si un refacto casse le contrat et que theta n’est pas un str,
        # on arrête immédiatement. Pylance pense ce chemin inatteignable.
        if not isinstance(theta, str):  # pragma: no cover  # type: ignore[unreachable]
            raise SystemExit(2)  # pragma: no cover
        price = predict_price(km, theta)
    except (SystemExit,) as exc:  # pragma: no cover
        # Propagate exit codes while avoiding re-raising.  # NOSONAR
        return exc.code if isinstance(exc.code, int) else 1  # pragma: no cover
    output = "0" if price == 0 else f"Predicted price: {price:.2f} €"
    print(output)
    return 0


# Exécution directe du module. Ne s'exécute pas à l'import.
if __name__ == "__main__":  # pragma: no cover - module glue
    # Transmet le code de main au shell via SystemExit.
    raise SystemExit(main())  # pragma: no mutate
