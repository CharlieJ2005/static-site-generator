# Static Site Generator

Static Site Generator is a Python project that builds a simple, recursive static site generator from scratch.  
This project is part of the [Boot.dev guided project series](https://www.boot.dev/courses/build-static-site-generator-python).

## Features

- Converts Markdown files in the `content/` directory to HTML pages using a template
- Recursively processes subdirectories for nested pages
- Copies static assets (images, CSS, JS, etc.) from `static/` to the output directory
- Supports custom base paths for generated links
- Automatically extracts titles from Markdown files
- Simple CLI usage (including build and deploy scripts)
- Outputs a complete static website in the `docs/` directory, ready for deployment (e.g. GitHub Pages)

## Usage

1. Prepare your directories:
    - Place Markdown content in the `content/` directory.
    - Place your HTML template in `template.html`.
    - Place static assets in the `static/` directory.

2. To **build and deploy the site locally**, run:

    ```bash
    ./main.sh
    ```

3. To **build the site for web deployment** (e.g., GitHub Pages), run:

    ```bash
    ./build.sh
    ```

4. (Manual usage) To generate your site directly with Python:

    ```bash
    python main.py [basepath]
    ```
    - `[basepath]` is optional. It sets the base path for generated href/src links (default is `/`).

5. The generated website will appear in the `docs/` directory.

## Notes

- The generator will overwrite the `docs/` directory each time it runs.
- All static files from `static/` are copied into `docs/`.
- Only Markdown files (`*.md`) in `content/` are converted to HTML.
- Scripts (`main.sh`, `build.sh`) automate common workflows.
- An example site (text content provided by the course) is currently deployed on my [GitHub Pages](https://charliej2005.github.io/static-site-generator).
