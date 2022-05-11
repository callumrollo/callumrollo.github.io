Title: Leaflet maps with Python-flask
Date: 2022-04-25 17:00
Modified: 2022-04-25 17:00
Category: FOSS
Tags:  python, maps, flask, automation, front-end
Slug: flask_leaflet
Summary: Creating interactive maps using Python-flask and leaflet

I have one website gimmick: interactive webmaps using leaflet and backed by Python-flask.

This may sound like a word salad, but it's a useful and simple (trust me) software stack for making visualisation and exploration of spatio-temporal data easy. 

I call it a gimmick because I've used the same core method to create:
- The UEA glider group [piloting website](https://ueaglider.uea.ac.uk/) ([source](https://github.com/ueaglider/ueaglider-web))
- The NBP 2202 cruise [data website](https://nbp2202map.com/) (the main subject of this article) [source](https://github.com/callumrollo/itgc-2022-map)
- The VOTO public facing live data website (work in progress) ([source]())

### Why you might want a site like this
If you want to display geospatial data:
- at varying scale
- with selectable layers
- with different overlays/backgrounds
- in an interactive manner
- to non-technical users

This works best with data that can be plotted as lines and points, but polygons are possible too.

### Prerequisites
- Some data
- A reasonable grasp of Python
- Ability to setup a basic linux cloud server

If any of these are missing, check out the links at the end of this article for some tutorials and datasets.

### Tech stack
The core library here is [flask](https://flask.palletsprojects.com), a Python micro-framework. It is a very minimal framework that allows us to make a slim website with no real database to complicate things. We will also use:
- leaflet maps
- jinja2 templates
- json

# First, imitate

I personally find it a lot easier to start by downloading, building and deploying a functional app than to start from scratch. This gives you a realistic view of the amount of work required to share your app and helps separate errors of code from errors of implementation.

With that said, let's begin!

1.  download the [nbp2202 website source code](https://github.com/callumrollo/itgc-2022-map) from GitHub
[click here](https://github.com/callumrollo/itgc-2022-map/archive/refs/heads/main.zip) to get the zip file
2. Create a Python environment using pip and the requirements.txt file or conda and the environment.yml file. Each works as well as the other
3. navigate to the directory where the environment files are and run the command `python itgc/app.py`
4. Open a browser window and go to http://127.0.0.1:5000/
5. That's it! You're running the app on your very own PC. You should see a website that looks and functions just like the one at [nbp2202map.com](https://nbp2202map.com) but it is running solely on your PC


# Next, remix
I recommend using [git](https://git-scm.com/docs/gittutorial) to keep track of changes to the codebase of this project. If you're particularly keen, maybe you already forked the repo in step 1 to start editing your own version.

The first place to make changes is in `index.html` this is the code for the webpage that the user interacts with
Here are some suggestions of things you might change:
- The default starting location and zoom with `map.setView`
- The base layer and optional overlays of the map in  `maplayers`
- The text on the page in the `container instructions`  section.

If you want to change the data itself, like adding more points and lines, you'll need to make a couple of changes.

First, each dataset is made into its own layer, which is then added to the map. See, for example, how we add the kasten and megacore sites. This is done in three steps on the map:

First we define an icon, with a size and an anchor point (which part of the image is placed at the location of the core site).
```html
let thorIcon = L.icon({
	iconUrl: '/static/img/icons/thor.png',
	iconSize:     [30, 35], // size of the icon
	iconAnchor:   [20, 15], // point of the icon which will correspond to marker's location
	popupAnchor:  [0, -15] // point from which the popup should open relative to the iconAnchor
});
```

Next,  we create a layer for the map. For this we read in a geoJSON dictionary and make a layer from points, calling an extra function `popupText` to make the little popup boxes that contain metadata on the core site
```html
let thorLayer =  L.geoJSON(thorDict, {
		pointToLayer: function (feature, latlng) {
			return L.marker(latlng, {icon: thorIcon});
		},
		onEachFeature: popupText
})
```

Finally, we add the layer to the map as an optional layer that the user can select
```html
"mega/kasten core ⛏": thorLayer,
```

These are the steps to display the data, but first we need to coerce our dataset itself into geoJSON. geoJSON is a well defined format. I have written a few scripts to write geoJSON from a pandas dataframe of lon, lat, datetime and metadata of some kind. You can download it [here](../images/df_to_json.py). You should be able to adapt it to your needs.

Once you have a way of converting your data to geoJSON, you import it into the app in the file `viewmodels/mission/mission_viewmodel.py`. The process of importing json files happens at the top of the `add_events` function. Just add your dataset to the list and copy the json file to the `static/json/nbp_data` directory. The advantage of adding the data through Python rather than just reading geoJSON straight into the leaflet map, is that it enables the temporal subsetting feature that allows a user to display only data within a certain time window.

Exploring this file, you will see similar functions for adding isobaths and may optional layers of satellite data. 
# On to the web

You've done it! A website of your own. Assuming you wish to share it with others (why else would you make a website?) you now need to host this on a server somewhere. This can seem daunting at first, but it's just a few easy steps:

# Going further

If this has given you an appetite for web development, you can build on this simple web app.

This app only has one webpage, but you can easily add more. You could also try adding a database. This makes your application more performant and really increases the scope of actions you can support. I recommend TalkPython fm's Flask course for a thorough explanation of these, link in the section below. You can also check out the source code for the other two projects linked above for examples with SQL and MongoDB.


-------------------------------
### Resources and links
- I learned flask from [TalkPython Training's Flask course](https://training.talkpython.fm/courses/explore_flask/building-data-driven-web-applications-in- python-with-flask-sqlalchemy-and-bootstrap) it goes into a lot more detail and enables you to make a really powerful, flexible website. It also covers deployment to the web in good detail
- You can learn enough html and CSS to get by just by googling things when they break. [w3schools](www.w3schools.com) have some good resources though, and the [bootstap docs](https://getbootstrap.com/docs/3.4/css/) are pretty good.
- [leaflet maps](leafletjs.com) have some great tutorials. You could get most of the functionality of this app just using leaflet and json.
- You can set yourself up with a cloud server for less than $/£/€ 10 a month from a cloud host like [Linode](https://www.linode.com/docs/guides/set-up-and-secure/) or [DigitalOcean](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04). Personally I'd avoid AWS at first as the learning curve is steeper, and it's a lot easier to end up accidentally running up a large bill.