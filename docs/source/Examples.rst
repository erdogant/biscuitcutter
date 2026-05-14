Quickstart
################

Using biscuitcutter is simple - just run the interactive CLI:

.. code-block:: console

    biscuitcutter

This will prompt you for:

- Repository / package name (required)
- Author full name (required)
- Author e-mail (optional)
- GitHub username (optional, defaults to lowercase author name without spaces)
- Parent directory (optional, defaults to current directory)


Example Session
################

Here's what a typical session looks like:

.. code-block:: console

    🍪  biscuitcutter – new repo scaffolder
    ────────────────────────────────────────────
      Repository / package name: my-awesome-project
      Author full name: Erdogan Taskesen
      Author e-mail: erdogant@gmail.com
      GitHub username: erdogant
      Parent directory (leave blank for current dir): 

    ✔  Created directory: /path/to/my-awesome-project
    ✔  Template extracted to: /path/to/my-awesome-project
    ✔  Placeholders replaced.

    🎉  Done!  Your new repo is ready at:
        /path/to/my-awesome-project


Using Programmatically
######################

You can also call the main function directly from Python:

.. code-block:: python

    from biscuitcutter import main
    
    # This will launch the interactive CLI
    main()


Creating a Project in a Specific Directory
##########################################

Here's an example of creating a new project in a specific parent directory:

.. code-block:: console

    $ cd /path/to/your/projects
    $ biscuitcutter
      Repository / package name: data-analysis-tool
      Author full name: Jane Smith
      Author e-mail: jane.smith@example.com
      GitHub username: janesmith
      Parent directory (leave blank for current dir): 

    ✔  Created directory: /path/to/your/projects/data-analysis-tool
    ✔  Template extracted to: /path/to/your/projects/data-analysis-tool
    ✔  Placeholders replaced.

    🎉  Done!  Your new repo is ready at:
        /path/to/your/projects/data-analysis-tool


What Gets Created?
##################

After running biscuitcutter, you'll have a complete Python project structure with:

- ``__init__.py`` - Package initialization file
- ``README.md`` - Project documentation (with your name and repo details filled in)
- ``pyproject.toml`` - Modern Python project configuration
- Additional template files as needed

All placeholders for repository name, author name, email, and GitHub username have been automatically replaced throughout all text files.


Overwriting Existing Directories
################################

If a directory with the same name already exists, biscuitcutter will ask for confirmation before overwriting:

.. code-block:: console

    ⚠️  '/path/to/my-project' already exists. Overwrite? [y/N]: y

This safety check helps prevent accidental data loss.



.. include:: add_bottom.add