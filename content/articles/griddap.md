Title: Erddapy griddap support
Date: 2021-08-18 17:00
Modified: 2021-08-18 17:00
Category: FOSS
Tags: software, foss, oceanography, gsoc
Slug: griddap
Summary: Supporting gridded dataset access via erddapy

As part of the [Google Summer of Code](https://summerofcode.withgoogle.com/) I have been working with [Filipe Fernandes](https://github.com/ocefpaf) to add [griddap](https://coastwatch.pfeg.noaa.gov/erddap/griddap/documentation.html) support to the [erddapy](https://github.com/ioos/erddapy) package, along with other features and performance improvements.

erddapy is a well used Python package that enables programmatic access to the wealth of oceanographic data stored on ERDDAP servers around the world. [ERDDAP](https://coastwatch.pfeg.noaa.gov/erddap/index.html) supplies data via two methods, tabledap and griddap.

[Tabledap](https://coastwatch.pfeg.noaa.gov/erddap/tabledap/documentation.html) is used for any data that can be formatted into a tabular datastructure such as a csv, an excel spreadsheet or a pandas DataFrame. This tends to be simple time series data from oceanographic moorings, floats or gliders. erddapy supports all the standard methods of accessing tabledap data, including ERDDAP's powerful server-side subsetting and plethora of data formats.


Griddap is used for higher-dimensional regularly spaced data such as satellite datasets and model output. Prior to GSoC, support for griddap was limited to the user downloading the entire dataset into an xarray object. This is workable for smaller datasets, but impractical for model outputs that can be terabytes in size, and unworkable if the user only wants small subsets of many large datasets.

Better support for griddap was [first requested back in 2018](https://github.com/ioos/erddapy/issues/32), but support for this separate ERDDAP method without effecting erddapy's tabledap support or duplication large parts of the codebase was a time consuming proposition. Fortunately, Filipe's proposal to add griddap support to erddapy was accepted and funded through GSoC 2021. You can see the proposal [here](https://summerofcode.withgoogle.com/projects/#4657854750916608)

Adding griddap support was a challenge. I had to familiarise myself with a complicated Python library including techniques I had made little use of in the past, such as classes, local caching and robust request parsing. This was also the first time I had programmed against an API designed by someone else. I had to work out how to parse user input into queries that ERDDAP servers understood, then take the response and read it into Python. With Filipe's guidance, I was able to add griddap support to [erddapy v1.1.0](https://github.com/ioos/erddapy/releases/tag/v1.1.0). I also had time to create a [jupyter notebook](https://ioos.github.io/erddapy/01a-griddap-output.html) walking through an example griddap query.


The work has really brought home to me the importance of stability of APIs in programming. If Bob Simmons and the ERDDAP team were to make a small change to the way that griddap query urls are structured, our griddap support for erddapy would come crumbling down. It has also introduced me to a wealth of oceanographic data products that I have started to use in my PhD work, as well as a whole community of oceanography/data science wizards and all the cool projects they have built. I hope to continue my work with erddapy and support for the wider oceanographic data science ecosystem.


