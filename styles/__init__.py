from pathlib import Path


def load_styles():
    """Load all CSS files and combine them."""
    project_root = Path(__file__).parent.parent

    # Load main CSS
    main_css_path = project_root / 'styles' / 'main.css'
    with open(main_css_path, 'r', encoding='utf-8') as f:
        css = f.read()

    return css
