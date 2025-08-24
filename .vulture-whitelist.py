# Whitelist for Vulture to ignore symbols used dynamically.
#
# Add functions, classes, or variables here when they are accessed via
# reflection or as CLI entry points so that Vulture doesn't report them as
# unused. Each item should be documented with a comment explaining why it's
# safe to ignore.


# Example: CLI entry point invoked via packaging metadata.
def cli() -> None:  # pragma: no cover - used by entry points
    ...


# Example: version constant read dynamically by tooling.
__version__ = "0.0.0"
