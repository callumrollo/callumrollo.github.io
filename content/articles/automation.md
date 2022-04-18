Title: Automation for oceanographers
Date: 2022-01-07 15:20
Modified: 2022-04-18 14:15
Category: FOSS
Tags:  linux, bash, software, optimise, oceanography, cruise, bandwidth
Slug: automation
Summary: Writing hacky scripts for oceanography


As a physical oceanographer, I occasionally spend chunks of time at sea. Typically this will be aboard a scientific research vessel with very limited shoreside connectivity. In order to keep oceanographic data flowing, I have developed several hacky scripts to perform routine analysis and transfer data in an efficient manner.

### Read emails in Python

This script is used to periodically check a mailbox for emails and take an action if they match certain criteria. I developed this to read automated emails of glider locations and add them to a database

```python
import json
import imaplib
import email
from datetime import datetime
import time
import os
from pathlib import Path


def read_email_from_gmail():
    # check what time email was last checked
    timefile = Path("lastcheck.txt")
    if timefile.exists():
        with open("lastcheck.txt", "r") as variable_file:
            for line in variable_file.readlines():
                last_check = datetime.fromisoformat((line.strip()))
    else:
        last_check = datetime(1970,1,1)
    # Write the time of this run
    with open('lastcheck.txt', 'w') as f:
        f.write(str(datetime.now()))
    # Check gmail account for emails
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login("youremail@gmail.com", "password")
    mail.select('inbox')

    result, data = mail.search(None, 'ALL')
    mail_ids = data[0]

    id_list = mail_ids.split()
    first_email_id = int(id_list[0])
    latest_email_id = int(id_list[-1])
    # Cut to last 10 emails
    if len(id_list) > 10:
        first_email_id = int(id_list[-10])

    # Check which emails have arrived since the last run of this script
    unread_emails = []
    for i in range(first_email_id,latest_email_id+1):
        result, data = mail.fetch(str(i), '(RFC822)')

        for response_part in data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                date_tuple = email.utils.parsedate_tz(msg['Date'])
                if date_tuple:
                    local_date = datetime.fromtimestamp(
                        email.utils.mktime_tz(date_tuple))
                    if local_date > last_check:
                        unread_emails.append(i)
    # Exit if no new emails
    if not unread_emails:
        with open('mqtt-log.txt', 'a') as f:
            f.write(str(datetime.now()) + ' no new mail' + '\n')
        exit(0)

    # Check new emails
    for i in unread_emails:
        result, data = mail.fetch(str(i), '(RFC822)')
        for response_part in data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                email_subject = msg['subject']
                email_from = msg['from']
                #print ('From : ' + email_from + '\n')
                #print ('Subject : ' + email_subject + '\n')
                # If email is from UEA domain and subject is GPS, pass to glider_loc script
                if email_from[-10:-1] == 'uea.ac.uk' and email_subject == 'GPS':
                    # The function glider_loc takes the glider location and relays it over MQTT
                    glider_loc(data, email_from)
```

Note: to avoid getting locked out by Gmail, I recommend enabling 2FA and creating an [app password](https://support.google.com/accounts/answer/185833?hl=en) for this script to use.

### Automated emails for data transfer

The simplest method I have found for sending automated emails is to install [nullmailer](https://wiki.debian.org/nullmailer#Installation_Examples_-_GMail) on a Linux box then run a short shell script.

```bash
#!/bin/bash
mv /home/pilot/data-to-nbp/most-recent /home/pilot/data-to-nbp/dives-`date +"%Y-%m-%dT%H:%M"`
mv /home/pilot/data-to-nbp/dives-to-nbp.zip /home/pilot/data-to-nbp/dives-to-nbp.zip-`date +"%Y-%m-%dT%H:%M"`
mkdir /home/pilot/data-to-nbp/most-recent
find /home/sg**/p*.mat -mtime -0.25 -exec cp {} /home/pilot/data-to-nbp/most-recent  \;
zip -rj /home/pilot/data-to-nbp/dives-to-nbp.zip /home/pilot/data-to-nbp/most-recent
echo "data last 6 hours" | mail -s "data4u" email@provider -A  /home/pilot/data-to-nbp/dives-to-nbp.zip
printf '\n%s' "$(date "+%Y-%m-%dT%H:%M:%S")" >> /home/pilot/data-to-nbp/transfer.log
printf ", transferred data" >> /home/pilot/data-to-nbp/transfer.log
```

This script performs several useful tasks. Here's a line by line breakdown
- Archives the folder `/home/pilot/data-to-nbp/most-recent` with a timestamp
- archives the previously sent zip file
- creates a directory
- finds files matching a certain pattern created in the last 6 hours and copies them to that directory
- zips the files
- emails the zip file to a recipient
- logs that the transfer was successful

### Read locations from Argos tags

This Python script accesses the [Argos web portal](https://argos-system.cls.fr/argos-cwi2/login.html) through a dedicated [web API](http://ws-argos.cls.fr/argosDws/services/DixService?wsdl). This enable automated access to Argos tag locations

```python

import datetime
import json
import os
import zeep
import xmltodict

wsdl = "http://ws-argos.cls.fr/argosDws/services/DixService?wsdl"

client = zeep.Client(wsdl=wsdl)
resp_xml = client.service.getXml(username="argos username", password="argo password", nbPassByPtt=100,
								 nbDaysFromNow=20,
								 displayLocation="true", displayRawData="true",
								 mostRecentPassages="true", platformId=str(tag_number))

resp_dict = xmltodict.parse(resp_xml)
bar = resp_dict['data']
# Only some records have valid locations
if 'program' not in bar.keys():
	return
baz = bar['program']
b = baz['platform']
b0 = b['satellitePass']


for b1 in b0:
	if 'location' not in b1.keys():
		continue
	argo_dict = b1['location']
	location_ate = datetime.datetime.strptime(argo_dict['locationDate'], '%Y-%m-%dT%H:%M:%S.%fZ')
	location_tag_number = int(tag_number)
	location_longitude = float(argo_dict['longitude'])
	location_latitude = float(argo_dict['latitude'])
	location_quality = argo_dict['locationClass']
	location_altitude = float(argo_dict['altitude'])

```

### GDAL for creating webtiles

Short bash script that will take any input geotiff and create webtiles for use with leaflet maps. This is how I generated the ice maps for the [nbp2202map](https://github.com/callumrollo/itgc-2022-map) and [website](https://nbp2202map.com/). Credit to [Li Ling](https://www.kth.se/profile/liling/) for figuring out how to warp the geotiffs to a usable projection.

```bash
PATH=$PATH:/home/callum/anaconda3/envs/geospatial/bin
infile=input_filename.tif
gdalwarp -t_srs EPSG:4326 -te -140 -76 -90 -66 $infile liproj.tif
gdal_translate -of vrt -expand rgba liproj.tif li.vr
gdal2tiles.py li.vrt AMSR  --zoom 1-9
```
Line by line:

- Add Anaconda environment to path which has cartopy installed. This is the easiest way to reliably install GDAL in my experience
- Specify input file
- Warp input file to EPSG:4236 (lazy, unprojected data)
- Colour the input file to RGBA
- Create webtiles at set zoom levels

### Other handy scripts
- [ADCP GNSS mash](https://github.com/callumrollo/adcp-gnss-mash) a Python script that combines two timestamped datasets from an autonomous platform to add location information to ADCP data. Includes parsing NMEA, manipulating files and using datetime
- [webscraping](https://github.com/callumrollo/github-scraper) a nice little example of scraping data from GitHub
- [geotiff-generator](https://github.com/callumrollo/geotiff-generato) A Python program to generate geotiffs from EMODnet, GEBCO or user supplied bathymetry. Includes taking user input from the command-line, stitching together EMODnet netCDFs and working with tri-band rasters
- [move your mouse every 30 seconds](https://github.com/callumrollo/coding/blob/master/handy_scripts/mousemove) you never know when you might [need it](https://xkcd.com/196/)

--------------------------------


### Tools used
These scripts use python and/or bash. The Python stuff probably works on Windows, but all were developed on Linux. For more tools check out out [my toolbox](https://callumrollo.github.io/pages/toolbox)

### Further reading


