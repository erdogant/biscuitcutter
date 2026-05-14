[![Python](https://img.shields.io/pypi/pyversions/biscuitcutter)](https://img.shields.io/pypi/pyversions/biscuitcutter)
[![Pypi](https://img.shields.io/pypi/v/biscuitcutter)](https://pypi.org/project/biscuitcutter/)
[![Docs](https://img.shields.io/badge/Sphinx-Docs-Green)](https://erdogant.github.io/biscuitcutter/)
[![LOC](https://sloc.xyz/github/erdogant/biscuitcutter/?category=code)](https://github.com/erdogant/biscuitcutter/)
[![Downloads](https://static.pepy.tech/personalized-badge/biscuitcutter?period=month&units=international_system&left_color=grey&right_color=brightgreen&left_text=PyPI%20downloads/month)](https://pepy.tech/project/biscuitcutter)
[![Downloads](https://static.pepy.tech/personalized-badge/biscuitcutter?period=total&units=international_system&left_color=grey&right_color=brightgreen&left_text=Downloads)](https://pepy.tech/project/biscuitcutter)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/erdogant/biscuitcutter/blob/master/LICENSE)
[![Forks](https://img.shields.io/github/forks/erdogant/biscuitcutter.svg)](https://github.com/erdogant/biscuitcutter/network)
[![Issues](https://img.shields.io/github/issues/erdogant/biscuitcutter.svg)](https://github.com/erdogant/biscuitcutter/issues)
[![Project Status](http://www.repostatus.org/badges/latest/active.svg)](http://www.repostatus.org/#active)

<div>
<a href="https://erdogant.github.io/biscuitcutter/"><img src="https://github.com/erdogant/biscuitcutter/blob/master/docs/figs/logo.png" width="350" align="left" /></a>
**biscuitcutter** is a new repository scaffolder for Python projects.

Create a new Python package or repository with a single command! ⭐️Star it if you like it⭐️
</div>

---

### Key Features

| Feature | Description |
|--------|-------------|
| [**Interactive CLI**](https://erdogant.github.io/biscuitcutter/pages/html/Installation.html) | Scaffold a new Python repository with prompts for repo name, author info, and more. |
| [**Template-Based**](https://erdogant.github.io/biscuitcutter/) | Uses a pre-configured template to create a ready-to-use project structure. |
| [**Placeholder Replacement**](https://erdogant.github.io/biscuitcutter/) | Automatically replaces placeholders (repo name, author, email, GitHub username) in all files. |

---

### Resources and Links
- **Documentation:** [Website](https://erdogant.github.io/biscuitcutter)
- **Bug Reports and Feature Requests:** [GitHub Issues](https://github.com/erdogant/biscuitcutter/issues)

---

### Installation

##### Install biscuitcutter from PyPI
```bash
pip install biscuitcutter
```

##### Install from GitHub source
```bash
pip install git+https://github.com/erdogant/biscuitcutter
```

---

### Usage

After installation, run the interactive CLI:

```bash
biscuitcutter
```

This will prompt you for:

- **Repository / package name** (required)
- **Author full name** (required)
- **Author e-mail** (optional)
- **GitHub username** (optional, defaults to lowercase author name without spaces)
- **Parent directory** (optional, defaults to current directory)

Alternatively, you can import and call the main function directly:

```python
from biscuitcutter import main
main()
```

---

### Example Session

```console
🍪  biscuitcutter – new repo scaffolder

───────────────────────────────────────────
  Repository / package name: my_project
  Author full name: Erdogan Taskesen
  Author e-mail: erdogant@gmail.com
  GitHub username: erdogant
  Parent directory (leave blank for current dir):

✔  Created directory: /path/to/my_project
✔  Template extracted to: /path/to/my_project
✔  Placeholders replaced.

🎉  Done!  Your new repo is ready at:
    /path/to/my_project
```

---

### Contributors

Setting up and maintaining biscuitcutter has been possible thanks to users and contributors. Thanks to:

<p align="left">
  <a href="https://github.com/erdogant/biscuitcutter/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=erdogant/biscuitcutter" />
  </a>
</p>

### Maintainer
* Erdogan Taskesen, github: [erdogant](https://github.com/erdogant)
* Contributions are welcome.
