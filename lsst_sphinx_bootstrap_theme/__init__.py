import os
import pkg_resources


__version__ = pkg_resources.get_distribution(
    'lsst_sphinx_bootstrap_theme').version
__version_full__ = __version__


def get_html_theme_path():
    """Return list of HTML theme paths."""
    return os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
