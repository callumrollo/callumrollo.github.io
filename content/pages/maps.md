Title: Maps and files
Date: 2025-04-24
Category: Generic
Slug: maps
Summary: Useful map data

I am a big fan of maps (see my [post on leaflet maps with Python]({filename}/articles/flask_leaflet.md)). I have collected various useful map files that I will share here. 

### Useful files


- Vindskyddskartan ([vindskyddskartan.se](https://vindskyddskartan.se/en/)) . Incredibly useful resource. Locationss and descriptions of over 4000 windshelters in Sweden that you can sleep in for free, no booking required. [download all locations of windshelters as kml file](https://callumrollo.com/files/vindskyddskartan.kml)
- Bohusleden ([homepage](https://www.westswedentrails.com/en/delled/bohusleden)) 350 km of hiking trails that wind from Gothenburg up to the Norwegian border. I've only hiked the southern ~ 100 km [download route as kml file](https://callumrollo.com/files/bohusleden.kml) 
- Pilgrimsleden ([homepage](https://www.vastsverige.com/mellerud/produkter/pilgrimsleden/)) Lovely 3-4 day pretty remote hike ending in Åmål. Good in winter as well. [Download route as kml file](https://callumrollo.com/files/Pilgrimsleden-Norra-Dalsland.kml). 
- Kattegatleden ([kattegattleden.se](https://kattegattleden.se/en)) 400 km cycling route along the coast from Gothenburg to Helsinborg. Nice and gentle, mostly on cycle paths/quiet roads. [Download route as kml file](https://callumrollo.com/files/Kattegattleden.kml)
- Dalsland gravel ([website](https://www.vastsverige.com/en/dalsland/cycling/gravel-cycling)) 850 km of primarily gravel trails centred around Bengtfors in Dalsland. [Download all routes as kml file](https://callumrollo.com/files/dalsland_gravel.kml)
- Gravel trails around Gothenburg . This is a subset file copied from mollbrink.se, described below. [Download all roads as kml file](https://callumrollo.com/files/VastraGotalandGrus.kml) Warning! This file is > 200 MB

You can import these .kml files easily as bookmarks/routes into maps.me. Alternatively, you can convert them to GPX files for use with e.g. oruxmaps (see gptx2kml below).

### Cool sites

- [https://gpx2kml.com](https://gpx2kml.com) convert between GPX and KML formats
- Lots of gravel data available on [mollbrink.se](https://www.mollbrink.se/). The author has extracted all the gravel maps in Sweden from OSM data.
### Navigation and software

I describe my navigation setup in some detail in [cycle touring]({filename}/articles/cycle_touring.md).
### Future work

One day I might include a dynamic leaflet map here which displays all this data. But then this wouldn't be a pure clean static site anymore...