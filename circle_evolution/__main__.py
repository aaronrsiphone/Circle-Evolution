"""Entry point when running ``python -m circle_evolution``.

This module simply re-exports the :func:`main` function from
``circle_evolution.main``.  The original implementation attempted to import
``main`` using an absolute import which fails when the package is executed as a
module.  By using a relative import we ensure the ``main`` module within the
package is used.
"""

from .main import main


if __name__ == "__main__":
    main()
