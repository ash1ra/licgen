# licgen 📃

[![PyPI Version](https://img.shields.io/pypi/v/licgen.svg)](https://pypi.org/project/licgen/)
[![Python Versions](https://img.shields.io/pypi/pyversions/licgen.svg)](https://pypi.org/project/licgen/)
[![License](https://img.shields.io/pypi/l/licgen.svg)](https://pypi.org/project/licgen/)
[![CI Status](https://github.com/ash1ra/licgen/actions/workflows/ci.yml/badge.svg)](https://github.com/ash1ra/licgen/actions)

**licgen** is a fast, reliable, and dependency-free CLI tool designed to instantly generate standard open-source LICENSE files for your projects.

Whether you need a quick permissive license for a hobby script or a strict copyleft license for an enterprise repository, `licgen` handles template rendering, copyright holder injection, and automated project/year detection out of the box.

## ✨ Features

* 🗃️ **Curated License Library**: Includes all major open-source licenses (MIT, Apache 2.0, GPLv3, AGPLv3, Unlicense, and more) pre-loaded as native resources.
* 🤖 **Smart Autocomplete & Detection**: Automatically resolves the current copyright year and dynamically infers the project name from your current directory if omitted.
* 🔍 **Interactive Discovery**: Built-in quick list command (`--list`) to instantly view all available license types directly in your terminal.
* 📦 **Zero Dependencies**: Pure Python implementation with zero third-party dependencies, leveraging modern `importlib.resources` and `argparse` for maximum portability and speed.
* 🪶 **Lightweight & Global**: Seamlessly installs as a global binary command that can be invoked from any directory.

## 🎯 Motivation

While creating open-source projects (like [pairgen](https://github.com/ash1ra/pairgen) or [manigen](https://github.com/ash1ra/manigen)), setting up the right LICENSE file is always annoying. You usually have to search for the template online, copy-paste it, and manually edit the year and author name. 

`licgen` was created to standardize and automate this routine into a single, straightforward CLI command. It perfectly complements your existing development workflow, making project initialization effortless and compliant from second one.

## 📦 Installation

You can install `licgen` directly from PyPI using `pip`:

```bash
pip install licgen
```

Or, if you use uv (recommended for CLI tools):

```bash
uv tool install licgen
```

## 🚀 Quick Start

Generate a standard MIT license for the current year in your working directory:

```bash
licgen mit -a "Your Name"
```

## 💡 Advanced Usage Examples

#### 1. Listing Available Licenses

If you are unsure which license type string to pass, list all built-in templates:

```bash
licgen -l
```

#### 2. Setup with Specific Year and Project Name

Generate desired license, explicitly defining the project name and a custom copyright year:

```bash
licgen apache-2.0 -a "Your name" -y 2048 -p "Project name"
```

#### 3. Custom Output Directory

Initialize a license inside a specific sub-folder or a newly initialized git repository path:

```bash
licgen mit -a "Your name" -o ./my-new-project
```

## 🛠️ CLI Reference

| Argument | Short | Description | Default |
| --- | :---: | --- | :---: |
| `LICENSE_TYPE` | - | **(Required)** Type of license to generate. | - |
| `--author` | `-a` | **(Required)** Name of the copyright holder / author. | - |
| `--list` | `-l` | Show all available license types and exit. | `False` |
| `--year` | `-y` | Copyright year. | *Current Year* |
| `--project` | `-p` | Project name. | *Current Dir Name* |
| `--output-path` | `-o` | Directory where the LICENSE file will be saved. | *Current Dir* |

## 🤝 Contributing

#### 1. Clone the repository

```bash
git clone https://github.com/ash1ra/licgen
cd licgen
```

#### 2. Install dependencies using uv

```bash
uv sync
# On Windows
.venv\Scripts\activate
# on Unix or MacOS
source .venv/bin/activate
```

#### 3. Format and lint the code

```bash
uv run ruff format .
uv run ruff check .
```

#### 4. Run the tests

```bash
uv run pytest tests/ -v
```

#### 5. Submit a pull request

If you'd like to contribute, please fork the repository and open a pull request to the main branch.
