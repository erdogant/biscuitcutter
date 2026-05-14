"""biscuitcutter.

Name        : biscuitcutter.py
Author      : Erdogan Taskesen
Contact     : erdogant@gmail.com
github      : https://github.com/erdogant/biscuitcutter
Licence     : MIT

"""

import os
import sys
import zipfile
import shutil
import logging

logger = logging.getLogger(__name__)

TEMPLATE_PLACEHOLDER_GITHUB = "GITHUBNAME"
TEMPLATE_PLACEHOLDER_REPO   = "REPONAME"
TEMPLATE_PLACEHOLDER_AUTHOR = "AUTHORNAME"
TEMPLATE_PLACEHOLDER_EMAIL  = "CONTACTADRESS"


# ---------------------------------------------------------------------------
# CLI entry-point
# ---------------------------------------------------------------------------

def main():
    """Interactive CLI: scaffold a new Python repo from the biscuitcutter template.

    Example
    -------
    >>> # Install
    >>> pip install biscuitcutter
    >>> # From the terminal run:
    >>> biscuitcutter

    """
    print("\n🍪  biscuitcutter – new repo scaffolder\n" + "─" * 42)

    # ── 1. Collect user input ───────────────────────────────────────────────
    repo_name   = _prompt("Repository / package name", required=True)
    author_name = _prompt("Author full name",          required=True)
    author_email= _prompt("Author e-mail",             required=False, default="")
    github_user = _prompt("GitHub username",           required=False, default=author_name.lower().replace(" ", ""))

    output_dir  = _prompt(
        "Parent directory (leave blank for current dir)",
        required=False,
        default=os.getcwd(),
    )

    repo_dir = os.path.join(output_dir, repo_name)

    # ── 2. Create repo directory ────────────────────────────────────────────
    if os.path.exists(repo_dir):
        overwrite = input(f"\n⚠️  '{repo_dir}' already exists. Overwrite? [y/N]: ").strip().lower()
        if overwrite != "y":
            print("Aborted.")
            sys.exit(0)
        shutil.rmtree(repo_dir)

    os.makedirs(repo_dir)
    print(f"\n✔  Created directory: {repo_dir}")

    # ── 3. Download & extract template.zip ─────────────────────────────────
    target_directory = os.path.dirname(os.path.abspath(__file__))
    zip_path = os.path.join(target_directory, 'template.zip')
    print(f"directory: {target_directory}")
    print(f"Template: {zip_path}")

    _extract_zip(zip_path, repo_dir)
    # os.remove(zip_path)
    print(f"✔  Template extracted to: {repo_dir}")

    # ── 4. Rename variables / placeholders inside all text files ───────────
    replacements = {
        TEMPLATE_PLACEHOLDER_REPO:   repo_name,
        TEMPLATE_PLACEHOLDER_AUTHOR: author_name,
        TEMPLATE_PLACEHOLDER_EMAIL:  author_email,
        TEMPLATE_PLACEHOLDER_GITHUB: github_user,
    }
    _rename_in_tree(repo_dir, replacements)
    _rename_paths(repo_dir, TEMPLATE_PLACEHOLDER_REPO, repo_name)

    print(f"✔  Placeholders replaced.")
    print(f"\n🎉  Done!  Your new repo is ready at:\n    {repo_dir}\n")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _prompt(label, required=True, default=None):
    suffix = f" [{default}]" if default else ""
    while True:
        value = input(f"  {label}{suffix}: ").strip()
        if not value and default is not None:
            return default
        if not value and required:
            print(f"    ✗  '{label}' is required.")
            continue
        return value or ""


def _create_stub_zip(dest_path, placeholder):
    """Create a minimal stub zip when the real template is unavailable."""
    import io, zipfile as zf

    buf = io.BytesIO()
    with zf.ZipFile(buf, "w") as z:
        z.writestr(f"{placeholder}/__init__.py",   f"# {placeholder}\n__version__ = '0.1.0'\n")
        z.writestr(f"{placeholder}/{placeholder}.py",
                   f'"""{placeholder}."""\n\nclass {placeholder}:\n    pass\n')
        z.writestr("README.md",    f"# {placeholder}\n\nA new Python library.\n")
        z.writestr("pyproject.toml",
                   f'[project]\nname = "{placeholder}"\n'
                   f'authors = [{{name = "Erdogan Taskesen", email = "erdogant@gmail.com"}}]\n')
    with open(dest_path, "wb") as fh:
        fh.write(buf.getvalue())


def _extract_zip(zip_path, dest_dir):
    """Extract zip; if the archive has a single top-level folder, strip it."""
    with zipfile.ZipFile(zip_path, "r") as z:
        members = z.namelist()
        # Detect common prefix (GitHub zips add a top-level folder)
        top_dirs = {m.split("/")[0] for m in members if "/" in m}
        strip = ""
        if len(top_dirs) == 1:
            candidate = top_dirs.pop() + "/"
            if all(m.startswith(candidate) or m == candidate.rstrip("/") for m in members):
                strip = candidate

        for member in members:
            rel = member[len(strip):] if strip and member.startswith(strip) else member
            if not rel:
                continue
            target = os.path.join(dest_dir, rel)
            if member.endswith("/"):
                os.makedirs(target, exist_ok=True)
            else:
                os.makedirs(os.path.dirname(target), exist_ok=True)
                with z.open(member) as src, open(target, "wb") as dst:
                    shutil.copyfileobj(src, dst)


def _rename_in_tree(root, replacements):
    """Walk *root* and replace placeholder strings in every text file."""
    TEXT_EXTENSIONS = {
        ".py", ".md", ".rst", ".txt", ".toml", ".cfg", ".ini",
        ".yml", ".yaml", ".json", ".html", ".js", ".css", ".sh",
        ".bat", ".ps1", "",
    }
    for dirpath, _dirs, files in os.walk(root):
        for fname in files:
            _, ext = os.path.splitext(fname)
            if ext.lower() not in TEXT_EXTENSIONS:
                continue
            fpath = os.path.join(dirpath, fname)
            try:
                with open(fpath, "r", encoding="utf-8", errors="replace") as fh:
                    content = fh.read()
                new_content = content
                for old, new in replacements.items():
                    new_content = new_content.replace(old, new)
                if new_content != content:
                    with open(fpath, "w", encoding="utf-8") as fh:
                        fh.write(new_content)
            except Exception as exc:
                logger.debug(f"Skipping {fpath}: {exc}")


def _rename_paths(root, old_name, new_name):
    """Rename files and directories that contain *old_name* in their names."""
    # Walk bottom-up so we rename children before parents.
    for dirpath, dirs, files in os.walk(root, topdown=False):
        for fname in files:
            if old_name in fname:
                src = os.path.join(dirpath, fname)
                dst = os.path.join(dirpath, fname.replace(old_name, new_name))
                os.rename(src, dst)
        for dname in dirs:
            if old_name in dname:
                src = os.path.join(dirpath, dname)
                dst = os.path.join(dirpath, dname.replace(old_name, new_name))
                os.rename(src, dst)


# ---------------------------------------------------------------------------

if __name__ == "__main__":
    main()