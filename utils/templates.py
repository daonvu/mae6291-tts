import os
from pathlib import Path


def load_css(css_path: str) -> str:
    """
    Load CSS content from a file.

    :param css_path: Path to CSS file (relative to project root)
    :return: CSS content as string
    """
    project_root = Path(__file__).parent.parent
    full_path = project_root / css_path

    if not full_path.exists():
        raise FileNotFoundError(f'CSS file not found: {full_path}')

    with open(full_path, 'r', encoding='utf-8') as f:
        return f.read()


def load_template(template_name: str) -> str:
    """
    Load HTML template from templates directory.

    :param template_name: Name of template file (e.g., 'history_entry.html')
    :return: Template content as string
    """
    project_root = Path(__file__).parent.parent
    template_path = project_root / 'templates' / template_name

    if not template_path.exists():
        raise FileNotFoundError(f'Template not found: {template_path}')

    with open(template_path, 'r', encoding='utf-8') as f:
        return f.read()


def render_template(template_name: str, **context) -> str:
    """
    Render a template with the given context.

    :param template_name: Name of template file
    :param context: Variables to inject into template
    :return: Rendered HTML string
    """
    template = load_template(template_name)
    return template.format(**context)