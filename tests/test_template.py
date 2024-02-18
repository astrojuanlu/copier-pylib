def test_template(copie):
    expected_files = [
        ".gitignore",
        "LICENSE",
        "README.md",
        "pyproject.toml",
        "tox.ini",
    ]
    expected_dirs = [
        "src",
        "src/project_name",
        "docs",
        "docs/source",
        "tests",
    ]

    result = copie.copy(
        extra_answers={
            "github_org": "johndoe",
            "project_name": "project-name",
            "short_description": "Short description",
            "author_name": "John Doe",
            "author_email": "john@doe.me",
        },
    )

    assert result.exit_code == 0, result.exception
    assert result.exception is None
    assert result.project_dir.is_dir()

    for path in expected_files:
        assert (result.project_dir / path).is_file()
    for path in expected_dirs:
        assert (result.project_dir / path).is_dir()
