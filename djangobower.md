Installation
------------

Install django-bower package:

.. code-block:: bash

    pip install django-bower

Add django-bower to `INSTALLED_APPS` in your settings:

.. code-block:: python

    'djangobower',

Add staticfinder to `STATICFILES_FINDERS`:

.. code-block:: python

    'djangobower.finders.BowerFinder',

Specify path to components root (you need to use an absolute path):

.. code-block:: python

    BOWER_COMPONENTS_ROOT = '/PROJECT_ROOT/components/'


If you need, you can manually set the path to bower:

.. code-block:: python

    BOWER_PATH = '/usr/bin/bower'

You can see an example settings file in `example project <https://github.com/nvbn/django-bower/blob/master/example/example/settings.py>`_.

Usage
-----

Specify `BOWER_INSTALLED_APPS` in settings, like:

.. code-block:: python

    BOWER_INSTALLED_APPS = (
        'jquery#1.9',
        'underscore',
    )

Download bower packages with the management command:

.. code-block:: bash

    ./manage.py bower install

Add scripts in the template, like:

.. code-block:: html+django

    {% load static %}
    <script type="text/javascript" src='{% static 'jquery/dist/jquery.js' %}'></script>

In production you need to call `bower install` before `collectstatic`:

.. code-block:: bash

    ./manage.py bower install
    ./manage.py collectstatic

If you need to pass arguments to bower, like `--allow-root`, use:

.. code-block:: bash

    ./manage.py bower install -- --allow-root

You can use `bower freeze` to receive `BOWER_INSTALLED_APPS` with fixed current versions:

.. code-block:: bash

    ./manage.py bower freeze

You can call bower commands like `info` and `update` with:

.. code-block:: bash

    ./manage.py bower info backbone
    ./manage.py bower update
