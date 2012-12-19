Welcome to git-recipe doc page

Usage
-----

Recipe clones git repository and checkouts to revision, if it is provided 
in configuration. You can use recipe like this:


for python ::

    [buildout]
    parts = data
    
    [data]
    recipe = git-recipe
    repository = git://example.com/my-git-repo.git
    rev = origin/redevlop-branch
    as_egg = True
    newest = True

for static resouces ::

    [jquery]
    recipe = git-recipe
    repository = git://github.com/jquery/jquery.git
    rev = origin/master
    download-directory = ${buildout:directory}/static/js/



Options
-------

*repository* - repository url

*ref* of *rev* - git reference_ wich you want to checkout.For example, it can be a branch name or a tag name like: 
"origin/master"、"v1.0"


*as_egg* - Set to True if you want the checkout to be registered as a
           development egg in your buildout

*newest* - always download newest repository, default is true.

And you can use buildout's global *offline* configure. 

About
-----

This is a fork of ``gitrecipe`` , which doesn't support 
the as_egg feature of ``zerokspot.recipe.git`` .

CHANGES
---------

- 0.1    add custom directory support for static resources. 
- 0.0.4  determine repository  now support '.' and '_' in its name.
- 0.0.3  add offline/newest configuration.


.. _reference: http://book.git-scm.com/7_git_references.html 
