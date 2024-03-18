Title: ERDDAP tools and tutorials
Date: 2024-03-06 07:20
Modified: 2024-03-06 07:20
Category: FOSS
Tags: software, foss, oceanography, ERDDAP, erddapy
Slug: erddaptools
Summary: Various ERDDAP resources I have created, contributed to or found useful

# Core resources

- [ERDDAP](https://erddap.github.io/)
- [awesome ERDDAP](https://github.com/IrishMarineInstitute/awesome-erddap) - a list of materials and ERDDAP servers maintained by the Irish Marine Institute 
- [ERDDAP google group](https://groups.google.com/g/erddap) useful mailing list for ERDDAP admin questions
# Tutorials

I made a 15 minute video demonstrating setting up an ERDDAP server and adding a new dataset using the axiom docker image. From the many methods I tried, this was the easiest way to get started with ERDDAP.


<iframe src="https://callumrollo.com/files/docker-erddap.mp4" title="Video demo of setting up an ERDDAP server"></iframe>

You can download the video here [callumrollo.com/files/docker-erddap.mp4](https://callumrollo.com/files/docker-erddap.mp4)

Transcript of all commands used in the video:  [callumrollo.com/files/erddap-docker-transcript.md](https://callumrollo.com/files/erddap-docker-transcript.md)


# Tools

- [erddapy](https://github.com/ioos/erddapy) essential python client for downloading data from ERDDAP. I contributed to this during Google summer of code 2021 [adding griddap support to erddapy](griddap)
- [gliderpy](https://github.com/ioos/gliderpy) a wrapper around erddapy to make downloading glider data easier. I contributed to this during OceanHackWeek 2020
- [ERDDAPlogs](https://github.com/callumrollo/erddaplogs) a tool for ERDDAP admins to get an idea of how their ERDDAP is being used. Work in progress!
- [VOTO ERDDAP demo](https://github.com/voto-ocean-knowledge/erddap_demo) A series of jupyter notebooks demonstrating how to use ERDDAP to download various datasets, using VOTO glider data as the core examples
- [GOOS ERDDAP demo](https://github.com/voto-ocean-knowledge/goos-erddap-demo) similar material but using a wider range of datasets with more time focused on gridded data

I have given various talks on ERDDAP,  mostly focused on using erddapy to access various oceanographic datasets. Here are a few of them:

- Data sharing workshop Gothenburg January 2023
- ERDDAP webinar series GOOS autumn/winter 2023
- Low cost sensor workshop Brest, November 2023
- GOOS Low cost technologies and data workshop, Cape Town June 2023
- Coastwatch webinar February 2024

---------------------------------------------------

### Rationale

I've put a lot of hours into various ERDDAP-adjacent tasks. It makes sense to have a list of all of them to point people to.

### Acknowledgements

- I was first introduced to ERDDAP by the excellent OceanHackWeek project
- [Filiipe](https://github.com/ocefpaf) has been an invaluable mentor on all things ERDDAP and on my journey from oceanography PhD student to amateur research software engineer
- Patrick Gorringe of SMHI has tirelessly worked to introduce ERDDAP into the Swedish ocean data ecosystem. It is with his help, and that of Marco Alba and Antonio Novellino at ETT solutions, that I was able to set up the first ERDDAP server in Sweden to feed into EMODnet
- The ERDDAP tutorials and projects here were greatly improved by contributions and feedback from, among others Martin Mohrmann (VOTO), Chiara Moneforte (VOTO), Joanna Paczkowska (VOTO) and Samantha Ouertani (NOAA AOML)
