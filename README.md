repo for the website https://callumrollo.github.io/

## Steps to making this github pages site:

- Install and activate the environment in the yaml file
- Create core files with `pelican-quickstart`, including YES to github pages
- Link to Flex pelican theme. It can be downloaded here https://github.com/alexandrevicenzi/flex
- Most configuration is in pelicanconf. Most important is the SITEURL. I have configured this to be optionally read from a json file, so that you can build the site for different urls by making a local `secrets.json` file
- Content as Markdown files
- In git, do all editing on source branch
- Test site with `make html && make serve`
- Push to github with `make github` this will push content to master to make it a pages site


