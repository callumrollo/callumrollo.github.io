Title: Gliderpy first release
Date: 2021-08-11 10:45
Modified: 2021-08-11 10:45
Category: FOSS
Tags: software, foss, oceanography, gsoc
Slug: gliderpy
Summary: The journey of an open source oceanography package

As part of the [Google Summer of Code](https://summerofcode.withgoogle.com/) I have been working with [Filipe Fernandes](https://github.com/ocefpaf) to improve access to ocean glider data served through [ERDDAP](https://coastwatch.pfeg.noaa.gov/erddap/index.html).

We were continuing work on the [gliderpy](https://github.com/ioos/gliderpy) project that we created together with [Lindsay Abrams](https://github.com/LindsayRAbrams) during the 2020 [OceanHackWeek](https://oceanhackweek.github.io/). This package aims to streamline the process of downloading and visualising glider data stored on ERDDAP servers and providing a simple way to directly import it into Python. We created gliderpy to do for glider data what [argopy](https://github.com/euroargodev/argopy) does for argo data.

During the two project days of OceanHackWeek, we created a working prototype of the package, with basic support for two ERDDAP servers and some plotting capability. This summer, with funding from GSoC, we were able to overhaul the codebase. We increased reliability with unit tests, added support for more data servers, a server-side metadata search function and standardisation of variable names. Most importantly, we packaged gliderpy and uploaded it to [PyPI](https://pypi.org/project/gliderpy/) and [conda-forge](https://anaconda.org/conda-forge/gliderpy).



Taking part in GSoC has been a great experience for me as I develop my skills a data scientist. The most valuable part of GSoC has been learning automated package management. Using tools like [GitHub Actions](https://github.com/features/actions) and the [grayskull](https://github.com/conda-incubator/grayskull) conda recipe creator greatly reduced the time needed to create and update the package, as well as removing several error-prone manual steps from the process. I also took part in live code review for the first time. This really improved the quality of the code I merged into gliderpy and made me think a lot more about how important structure and design patterns are in a software project. I would recommend GSoC to anyone in the ocean science community who wants to improve their software engineering skills and contribute to useful open source projects.

---

### The future of gliderpy

We plan to continue development of gliderpy, building on its visualisation capabilities and supporting more ERDDAP servers. Progress will be slower now that GSoC is over and other projects take priority. However, with a package published we hope to engage glider data users in testing and improving gliderpy in the FOSS tradition.

Next steps for gliderpy include more elegant plotting of oceanographic data, support for more servers and visualisation of data availability. Want to get involved? Head over to [gliderpy](https://github.com/ioos/gliderpy) and submit an Issue or drop me an [email](mailto:c.rollo@outlook.com).

