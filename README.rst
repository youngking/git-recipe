Welcome to git-recipe doc page

Usage
-----

Recipe clones git repository and checkouts to revision, if it is provided
in configuration. You can use recipe like this:


For python ::

    [buildout]
    parts = data

    [data]
    recipe = git-recipe
    repository = git://example.com/my-git-repo.git
    ref = origin/redevlop-branch
    as_egg = True
    newest = True

For static resouces ::

    [jquery]
    recipe = git-recipe
    repository = git://github.com/jquery/jquery.git
    ref = origin/master
    download-directory = ${buildout:directory}/static/js/

For django plugins with bad repository name ::

    [paypal]
    recipe = git-recipe
    repository = git://github.com/johnboxall/django-paypal.git
    ref = origin/master
    repo_name = paypal
    as_egg = True

Options
-------

*repository* - repository url

*ref* - git reference_ wich you want to checkout.For example, it can be a
        branch name or a tag name like "origin/master"、or "v1.0".

*download-directory* - If filled it will make the clone in this folder.

*repo_name* - If filled it will change the repository name.

*as_egg* - Set to True if you want the checkout to be registered as a
           development egg in your buildout.

*newest* - always download newest repository, default is true.

And you can use buildout's global *offline* configure.

About
-----

This is a fork of ``gitrecipe`` , which doesn't support
the as_egg feature of ``zerokspot.recipe.git`` .

CHANGES
---------

- 0.2    add custom repository name for django plugins.
- 0.1    add custom directory support for static resources.
- 0.0.4  determine repository  now support '.' and '_' in its name.
- 0.0.3  add offline/newest configuration.


.. _reference: http://book.git-scm.com/7_git_references.html
