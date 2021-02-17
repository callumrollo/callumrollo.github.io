# TODO

- Add pictures/diagrams
### Opening points

conda is downstream of pip

Show that the package is not there already


### The scenario

You've written a kick-ass Python script for solving your knotty scientific problem and you want to share it with your peers, great! How do you do this though? Sure, you could email it to interested parties like it's 1995, post it on twitter, or seed USBs loaded with code in strategic univeristy car parks. There is, however, a far superior solution. Packaging.

![](../images/package.jpeg) 

Packaging is the act of wrapping your code up into a well defined, standalone form and distributing it over the Information Superhighway. Packaging allows to distribute you code in a way that is

- Transparent
- Reproducible
- Upgradable
- Easy to integrate

If you've coded more than a `hello world`in Python you've already used packages. When you interact with pip/conda environment or `import numpy as np` you are leveraging Python's extensive pacakging ecosystem, standing on the shoulders of giants.

Wouldn't it be great if, when people inquired about your awesome code, you could tell that installing it is a simple as `pip install my_awesome_package`?

Strap yourself in buddy, because in this tutorial, that's exactly what we're going to do.

### Prerequisites

- A basic understanding of the terminal, Python and git 
- An account on [GitHub](https://github.com/join)
- An account on [TestPyPI](https://test.pypi.org/account/register/)
- A cool script*


*for the purpose of this tutorial, a `hello world` is fine

### Disclaimers

1. There are loads of other guides out there, check out *sources* at the bottom of this page for several of them. Other people have done it before and better. I'm only writing this because, when I created my first package, I couldn't find this info all in one place.

2. You will probably hit snags when following this with your own package. All code is unique, search engines are your friend.

3. Is it hard to do/will people laugh at me if I lack mad hacker skillz? No! The FOSS community is far from perfect, buteverone has they're first time doing this stuff. Your merges will screw up the codebase, your CI checks will fail, your package will ship with half the parts missing. This is fine. In software, failure is cheap and part of learning.

### Let's go!

You start off with a script. A beautiful script. Maybe it does something super useful like doubling a number. In a script called `bignumber.py`, you have a function:

```
def double_number(input):
	return 2 * input
```

This is some pretty complex stuff, so we'll include a README.md so readers can get the précis of our project.

```markdown
# Doubler

This package is for a function that doubles your numbers, making them twice as good.

[website here](doubler-docs.org)

```

We create a **directory** for our script. This will be the name of the package, so check that it's not already taken on PyPI. I'll use the name doubler
![](../images/doubler-pypi.png) 

We'll want a licence too, go and grab one from [opensource.org](https://opensource.org/licenses). In this case I've gone with the simple and permissive MIT license.

After all this we have the following structure:
```
packaging-dir  (this name doesn't matter)
├── doubler (your package name)
│   └── bignumber.py (the actual code goes here)
├── LICENSE
├── README.md
└── setup.py (explained in the next section)

```

### Add it to git

Now is as good a time as any. 

### Add setup.py

We'll need some boilerplate in `setup.py` containing the essential information on our package. This is essential for the ship to PyPI, so check you get the info right
```python
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="doubler", 
    version="0.0.1",
    author="Callum Rollo",
    author_email="c.rollo@outlook.com",
    description="A demo package for test PyPI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/callumrollo/doubler",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)
```
You'll find detail on all these in the [python.org article](https://packaging.python.org/tutorials/packaging-projects/#packaging-your-project).

Now, we package the code using **setuptools**. If you haven't installed it already, it's on pip and conda-forge
`python setup.py sdist`


### Shipping to PyPI

For (test)PyPI to accept your package, you'll need the correct credentials. These go in a file called `.pypirc` in your home folder:

```shell
[distutils]
index-servers=
    pypi
    testpypi

[pypi]
username = <account_name>
password = <account_password>

[testpypi]
repository = https://test.pypi.org/legacy/
username = <account_name>
password = <account_password>

```
Just change the stuff in the angle brackets after you register for the sites. You probably shouldn't [reuse your password](https://xkcd.com/792/).



You ship the package to test-PyPI with `twine`

`python -m twine upload  dist/* --repository testpypi`

And that's it! Go check out your work.

You can now install your package anywhere in the world with
`pip install -i https://test.pypi.org/simple/ doubler==0.0.1`

Once that works, do it for real on PyPI by dropping the --repository testpypi


### Shipping to conda-forge

Conda-forge is the community run package repository that is fully compatible with conda core but way bigger. It works from PyPI packages which is why we do it second.

Adding to conda-forge is a little tricker, as it will need to be approved by a moderator. This gives your project a big visibility boost though, especially with scientists. And scrutiny of your code is a good thing!


### Updating

To update your package on PyPI, you simply make changes to the code, update the version number in setup.py then repeat the steps with setuptools and twine to create and ship the package.

Updating on conda forge is simple too, though it requires some Github finesse. You fork the feedstock to your git hub account, bump the version number in recipe/meta.yaml

What version number should I go to? I like [semantic versioning](https://semver.org/). Other sytems are fine too, just be consistent.

Remember to change the SHAsum too, (you can find this on the PyPI download page in Downloads >> hashes) or the CI checks will fail.

There are good instructions on this in the README of the feedstock itself.

In short, you need to:

- Create a branch on the feedstock from your own fork
- Update the SHAsum to correspond to that on pypi
- re-render the feedstock

### How about a real package?

Copy the structure of something similar if you can. The first package I made for PyPI was a series of colourmaps, so I based it off the excellent [cmocean](https://github.com/matplotlib/cmocean). I would advise pushing to git and getting a package on test-PyPI early in development, so you can make all the early packaging mistakes before going to PyPI official.

Write down your process! It will save you a world of pain when you need to update the package a year later.

----------------------

### Sources

https://packaging.python.org/tutorials/packaging-projects/#packaging-your-project

https://blog.jonasneubert.com/2017/09/13/publishing-your-first-pypi-package/

https://blog.jetbrains.com/pycharm/2017/05/how-to-publish-your-package-on-pypi/

https://conda-forge.org/docs/maintainer/00_intro.html


