Welcome to git-recipe doc page

Usage
-----

Recipe clones git repository and checkouts to revision, if it is provided 
in configuration. You can use recipe like this: ::

    [buildout]
    parts = data
    
    [data]
    recipe = gitrecipe
    repository = git://example.com/my-git-repo.git
    rev = origin/redevlop-branch
    as_egg = True

Options
-------

*repository* - repository url

*ref* of *rev* - git reference_ wich you want to checkout


*as_egg* - Set to True if you want the checkout to be registered as a
           development egg in your buildout


About
-----

This is a fork of ``gitrecipe`` , which doesn't support 
the as_egg feature of ``zerokspot.recipe.git`` .
