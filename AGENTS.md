# Repository Guidelines

## Project Structure & Module Organization

This repository is a small pygame shooting-game teaching project.

- `main.py` is the complete reference game.
- `mondai.py` is the student debugging exercise; `mondai_kotae.py` is its completed answer.
- `hatten.py` and `hatten_kotae.py` contain the optional extension challenge and answer.
- `images/` contains the player, enemy, and bullet PNG assets.
- `デバッグチャレンジ.docx` is the classroom handout.
- `pyproject.toml` and `uv.lock` define the Python 3.14 environment and dependencies.

There is currently no dedicated test directory or automated test suite.

## Build, Test, and Development Commands

Use `uv` from the repository root:

```sh
uv sync                         # Install the locked environment
uv run python main.py           # Run the reference game
uv run python mondai.py         # Run the student exercise
uv run python hatten.py         # Run the extension exercise
uv run python -m py_compile main.py mondai.py mondai_kotae.py hatten.py hatten_kotae.py
uv run ruff check .             # Static checks
uv run ruff format --check .    # Verify formatting
```

The games open a pygame window. Close with Esc or the window close control. For headless smoke checks, set `SDL_VIDEODRIVER=dummy` and terminate the process after startup.

## Coding Style & Naming Conventions

Use four spaces, double-quoted strings, and an 88-character line limit, matching Ruff configuration. Run Ruff formatting after code changes. Existing teaching code intentionally uses descriptive Japanese identifiers and comments; preserve that style when editing educational examples. Keep `main()` as the executable entry point and avoid introducing dependencies beyond `pygame-ce` without updating `pyproject.toml` and `uv.lock`.

## Testing Guidelines

No coverage threshold is configured. Every change should at least pass compilation and Ruff checks, followed by a manual game smoke test. Verify controls, collision behavior, score updates, restart behavior, image mode, and required assets. Changes to `mondai.py` should be checked against `mondai_kotae.py` so the exercise contains only intended omissions.

## Commit & Pull Request Guidelines

Use short, imperative commit subjects (for example, `Improve mondai.py debugging exercises`). Keep commits focused. Pull requests should explain the learner-facing behavior, list validation commands, note any control or asset changes, and include screenshots or a short recording when pygame visuals or the classroom handout change.
