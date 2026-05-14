Installation and Usage
######################


Pypi
**********************

.. code-block:: console

    # Install from Pypi:
    pip install -U biscuitcutter


GitHub Source
*************

.. code-block:: console

    # Install directly from GitHub source
    pip install git+https://github.com/erdogant/biscuitcutter


Usage
**********************

After installation, ``biscuitcutter`` provides an interactive CLI to scaffold a new Python repository:

.. code-block:: console

    biscuitcutter

This will prompt you for:

- Repository / package name (required)
- Author full name (required)
- Author e-mail (optional)
- GitHub username (optional, defaults to lowercase author name without spaces)
- Parent directory (optional, defaults to current directory)

Alternatively, you can import and call the main function directly:

.. code-block:: python

    from biscuitcutter import main
    main()


Remove Installation
**********************

If you installed ``biscuitcutter`` in a virtual environment, removing that environment will also remove the installation. To uninstall ``biscuitcutter`` directly:

.. code-block:: console

    pip uninstall biscuitcutter


.. include:: add_bottom.add
