Title: Link Rot
Date: 2024-11-28 17:10
Modified:  2024-11-28 17:10
Category: publishing
Tags: pelican, publishing, linkrot, web, posse
Slug: deadlinks
Summary: Tending to my little garden of links

I recently decided to change how I internally link to other parts of this site, so that the links won't break when the urls change (this site is currently hosted both at [https://callumrollo.com/](https://callumrollo.com)and [https://callumrollo.github.io/](https://callumrollo.github.io/)). In the process, I found many links that no longer worked, or never worked in the first place! 

I used the cool tool [markdown link check](https://github.com/tcort/markdown-link-check) to perform this. It reads all the markdown files in a folder and checks each of the links, producing a pretty shell output

```bash
FILE: content/articles/automation.md
  [✓] https://support.google.com/accounts/answer/185833?hl=en
  [✓] https://wiki.debian.org/nullmailer#Installation_Examples_-_GMail
  [✓] https://argos-system.cls.fr/argos-cwi2/login.html
  [✓] http://ws-argos.cls.fr/argosDws/services/DixService?wsdl
  [✓] https://github.com/callumrollo/itgc-2022-map
  [✖] https://nbp2202map.com/
  [✖] https://www.kth.se/profile/liling/
  [✓] https://github.com/callumrollo/adcp-gnss-mash
  [✓] https://github.com/callumrollo/github-scraper
  [✖] https://github.com/callumrollo/geotiff-generato
  [✖] https://github.com/callumrollo/coding/blob/master/handy_scripts/mousemove
  [✓] https://xkcd.com/196/
  [✖] /pages/toolbox.html

  13 links checked.

  ERROR: 5 dead links found!
  [✖] https://nbp2202map.com/ → Status: 0
  [✖] https://www.kth.se/profile/liling/ → Status: 0
  [✖] https://github.com/callumrollo/geotiff-generato → Status: 404
  [✖] https://github.com/callumrollo/coding/blob/master/handy_scripts/mousemove → Status: 404
  [✖] /pages/toolbox.html → Status: 400

```

There were several reasons for these failures:

- Incorrectly written links, copy paste errors by me!
- Resources that had moved
- Trying to link to a private resources (e.g. script in one of my private github repos)
- "Forbidden links", ie the tool was not allowed to check the resource. Seems to happen with paywalled scientific papers
- Improperly/incompletely formatted urls e.g. betterfigures.org not https://betterfigures.org
- Sites no longer in existence, like the map I made for the nbp2202 cruise, described in [my leaflet article]({filename}/articles/flask_leaflet.md)
- Web pages that had disappeared from the internet

Most of these I was able to resolve, several of the moved resources had redirects operating on their original urls. Others I was able to find by exploring their host site. I fixed my typos and used complete urls everywhere. I removed links to resources that have dropped off the internet and cannot be easily recreated, like my old nbp2202 map app, and used the [internet archive](https://archive.org/)'s Wayback Machine to link to a saved copy of the late, great [David Graeber's Bullshit Jobs article](https://web.archive.org/web/20190906050523/http://www.strike.coop/bullshit-jobs/).  But some resources were lost for good.


--------------------------

Our internet is such a fragile thing. Not a monolith, but a series of ramshackle structures in constant decay, adding extensions, changing street signs, erecting roadblocks and sometimes burning to the ground.

I don't know how long I will keep tending to this little corner of the internet (I bought a 10 year lease on the domain at least!) but this exercise has reminded me of how ephemeral a lot of this is. When this site sinks back into the rich loam of the internet some day in the future, will there be any links elsewhere left dangling? Like vestigial limbs, pointing to words that no longer exist.

It is said that we die twice. Once when we draw our final breath, and again the last ever time another person speaks our name.