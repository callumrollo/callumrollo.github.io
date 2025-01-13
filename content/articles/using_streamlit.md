Title: A Python web app in under an hour
Date: 2025-01-13 13:15
Modified:  2025-01-13 14:15
Category: FOSS
Tags: python, web-dev, science,tutorials
Slug: using_streamlit
Summary: When you just wanna chuck some stuff on the net

As I was packing up on Friday, I received an email from a old scientific collaborator Dr. D. asking for advice on how to share some scientific data on the internet. He wanted to share the real time status of some [automatic weather stations](https://en.wikipedia.org/wiki/Automatic_weather_station) (AWS, not the Bezos one) and some timeseries of temperature humidity etc. My interest was sufficiently piqued that ,when I got home[ref]I do not endorse working outside of office hours. Do as I say not as I do.[/ref], I gave myself an hour to knock together the best solution I could. It resulted in this:

[https://aws-demo.streamlit.app/](https://aws-demo.streamlit.app/)

Source code: [https://github.com/callumrollo/streamlit-demo-aws](https://github.com/callumrollo/streamlit-demo-aws)

### Requirements/Motivation

As communicated by Dr. D., the web app needed to:

- Show near real time uptime stas and science time-series data
- Be easy to implement and maintain
- Be python based

Some additional requests were:

- To run locally on-site where the weather station is
- Be interactive (zoom/pan data)


I had been meaning to try out streamlit for a while now. While my usual go-to is to whip up a python-flask app for all my website and slippy map purposes (for more see [this post]({filename}/articles/flask_leaflet.md)), this request called for something much simpler and more user-friendly to create.

### Steps

1. Search the internet for "streamlit"
2. Copy and paste their [quickstart](https://streamlit.io/#install) `pip install streamlit && streamlit hello`[ref] After creating and activating a virtual environment. I'm not a monster[/ref]
3. Realise I actually wanted more of a chart
4. Read the [Docs](https://docs.streamlit.io/) (yuck)
5. Copy and paste an [example](https://docs.streamlit.io/get-started/fundamentals/main-concepts) with a chart I wanted
6. Run that locally with `streamlit run app.py`
7. Make some fake data in a pandas dataframe
8. Edit the example to show the two basic charts I wanted
9. Add some [download functionality](https://docs.streamlit.io/develop/api-reference/widgets/st.download_button)
10. Publish the app to github
11. Deploy the app to streamlit community
12. Add instructions
13. Present this to Dr. D.
14. Write this blog post in case others may benefit!

Steps 1 - 12 took just under an hour. I chatted with Dr. D. for 30 minutes about the solution (he was very happy!) and took another 30 to write this blog post. It's rough and ready but does the job.
### Reflection

When I talk to friends in tech, they are often surprised/alarmed by the outdated tech stack and approaches that scientists use to do our work. Public perception is that we're at the cutting edge, most people would be shocked to see how old-school and just plain old a lot of the tools we depend on are. While I personally think novelty is overrated (climate models are fine in FORTRAN, please stop suggesting we rewrite X in rust) a lot of science, particularly on the data-viz/public outreach front, could be much better if it used modern, dynamic tooling.

It's brings me a lot of joy to help colleagues with things like this. If there is any through line to my career and personal ethos, it is creating/improving/teaching tooling that makes other scientists more effective. Some of my proudest moments during my PhD were spending a few hours writing bash scripts that saved my fellow students weeks of manual work.



-------------
### Footnotes

- I listened to [Deafheaven - Ordinary Corrupt Human Love](https://www.youtube.com/watch?v=ITgslYJhfx0&list=PLJ7QPuvv91JvpyTZ0qvs9bKeUXhYdKNuF)and [Charli XCX- Crash](https://www.youtube.com/watch?v=nwNQexRDAf0&list=OLAK5uy_n0UZxsAiOCnXxbPeznWGzuV4Ly4Mf-I6c&index=1) while writing this post




