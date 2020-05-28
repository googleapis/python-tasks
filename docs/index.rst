.. include:: README.rst

.. include:: multiprocessing.rst

API Reference
-------------

This package includes clients for multiple versions of the Tasks
API. By default, you will get ``v2``, the latest version.

.. toctree::
    :maxdepth: 2
    
    gapic/v2/api
    gapic/v2/types


The previous beta releases, spelled ``v2beta3`` and ``v2beta2``, are provided to continue to
support code previously written against them. In order to use them, you
will want to import from e.g.  ``google.cloud.tasks_v2beta3`` in lieu of
``google.cloud.tasks`` (or the equivalent ``google.cloud.tasks_v2``).

v2beta3:

.. toctree::
    :maxdepth: 2

    gapic/v2beta3/api
    gapic/v2beta3/types
    
v2beta2:

.. toctree::
    :maxdepth: 2
    
    gapic/v2beta2/api
    gapic/v2beta2/types

Changelog
---------

For a list of all `google-cloud-tasks` releases.

.. toctree::
    :maxdepth: 2

    changelog
