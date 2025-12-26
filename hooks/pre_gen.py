"""Validate required answers before rendering."""

from copier.errors import UserMessageError


def _require(name: str, value: str) -> None:
    if not value or not str(value).strip():
        raise UserMessageError(f"Answer for '{name}' is required.")


def main(answers):
    # Required even with suggestions (user could delete them)
    for field in (
        "project_name",
        "project_slug",
        "package_name",
        "project_description",
        "git_remote",
        "repository_url",
    ):
        _require(field, answers.get(field))

    # Required with no intrinsic suggestion
    for field in ("author_name", "author_email", "github_username"):
        _require(field, answers.get(field))

