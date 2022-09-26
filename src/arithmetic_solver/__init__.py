from importlib.metadata import PackageNotFoundError, version  # pragma: no cover

# METADATA ====================================================================

__author__ = "Clément HUBER"
__copyright__ = "Clément HUBER"
__license__ = "MIT"
__email__ = "clement.victor.huber@gmail.com"

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = __name__
    __version__ = version(dist_name)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"
finally:
    del version, PackageNotFoundError