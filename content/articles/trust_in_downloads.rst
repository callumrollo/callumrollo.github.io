Package download stats
###########################################

:date: 2010-11-06 22:00
:modified: 2010-11-06 22:00
:tags: python, foss, science, packaging, conda
:category: foss
:slug: package_trust
:authors: Callum Rollo
:summary: What do package download stats mean?
:status: draft

About 6 months ago, I published my first package. It was nothing significant, just a Python wrapper around Fabio Crameri's `Scientific Colour Maps <http://www.fabiocrameri.ch/colourmaps.php>`_. Being too lazy to download and unzip the colourmaps and run the 2 lines of Python necessary to load each colourmap in my scripts, I decided to port the colourmaps to `PyPI <https://pypi.org/project/cmcrameri/>`_ and `conda forge <https://github.com/conda-forge/cmcrameri-feedstock>`_. My aims in doing this were:

1. Make it easier to use Fabio's colourmaps
2. Learn how to package Python libraries
3. Gauge interest in the Python community for perceptually uniform colourmaps

I achieved 1. with my first successful version of the colourmaps. They can now be installed with the simple expedient of either

``pip install cmcrameri``

or for conda

``conda install -c conda-forge cmcrameri``

Objective 2. was completed along the way. I still need to write up my notes, as creating a package was quite a learning journey and something I hope to do again in future.

Objective 3. presents a conundrum. How do you measure community engagement with a package? I had no intention of polling people or advertising the new package. I had created it principally for my own convenience, but wanted to give back to the open source community if I could. The most obvious way to measure interaction with package was how many people were using it. And to use it, they'd have to download it.

Both pip and conda provide running totals of the number of times a package has been downloaded. At time of writing, after being online for 6 months, these numbers were surprisingly high: `over 6000 for pip <https://pepy.tech/project/cmcrameri>`_ and `500 for conda-forge <https://anaconda.org/conda-forge/cmcrameri>`_.

**But do these downloads mean that people are using the package?**

I have heard anecdotally that these package stats are flawed. They can be artificially inflated by the package being downloaded as an unused dependency by another package, by mirroring services and by testing systems. On the flip side, downloads may underestimate usage if users acquire the package from an unofficial mirror, or copy it locally.

To make a start at understanding this, I started to monitor the number of downloads from conda-forge, as this seemed the smaller, more stable counter. To this end, I wrote a short script and deployed it to a linux server I maintain, to run as an hourly cron job. The scripts is quick and dirty:

	curl https://anaconda.org/conda-forge/cmcrameri -o "/home/callum/personal/condaforgepage.txt" 
	  
	printf '\n%s' "$(date "+%Y-%m-%dT%H:%M:%S")" >> /home/callum/personal/page_stats.txt
	
	printf ", " >> /home/callum/personal/page_stats.txt
	
	grep total\ downloads /home/callum/personal/condaforgepage.txt | tr -d -c 0-9 >> /home/callum/personal/page_stats.txt
	
It downloads the stats page from conda forge as plaintext, searches for ``total`` extracts the number from that line, and prints it to a file with a timestamp [#]_.

This was also inspired by chatter on the RSE Slack about the sustainability of our current software packaging excosystem. With massive data throughput with no thought. Someone, somewhere has to pay and the environmental cost of shuttling all this data around is enormous

Methodology

Interpretation

Results

.. [#] If you like poorly formatted hacky shell scripts, you'll love my shell blog post https://callumrollo.github.io/bash.html#bash
