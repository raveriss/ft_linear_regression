VULTURE_ARGS=src .vulture-whitelist.py --min-confidence=80 --exclude="**/tests/**,**/docs/**,.venv,build,dist" --verbose

.PHONY: vulture
vulture:
	poetry run vulture $(VULTURE_ARGS)
