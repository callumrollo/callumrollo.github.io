Title: Summer of Code
Date: 2021-05-17 22:00
Modified: 2021-05-17 22:00
Category: FOSS
Tags:  software, foss, oceanography
Slug: gsoc
Summary: How have I become a programmer?

Today I got some great news, I have been accepted onto the Google Summer of Code program! You can see my project [here](https://summerofcode.withgoogle.com/projects/#4657854750916608). I'm really excited for this project, it feels quite unreal though. Google will be paying me (albiet, not much) to write code. I don't feel remotely qualified for this. I did a three day intro to Python, copied a bunch of code from stack overflow and muddled my way through some projects on GitHub and now this. I'll give this project my all, but it feels distinctly weird that I've made it this far.

While the imposter syndrome takes root, I'm going to write down the steps that took me here. It may be of use to some other lost oceanographic nerd someday.

# Origins

I did not grow up soldering together an Apple II in my parents basement. Nor was I inspired to mod my first person shooter games to pwn n00bs online. In fact I had no coding experience beyond some traumatic Linux reinstallations until the second year of my undergraduate degree. My first taste of programming was creating maps of earthquakes using gmt and parsing data with trail and error changes to a single line `sed` command provided by a lecturer. It was a frustrating, but ultimately rewarding experience as I figured out how to make the computer do the repetitive tasks of geophysics. The power of a simple for-loop was far more alluring than the more prosaic methods of pencil and compass in our structural geology practicals.

This course also introduced me to the joys of multi-user Linux systems and how cunning use of `cd` and your smarter friend's username (helpfully identical to their university email) could be used to compare homework solutions. Additionally, some lecturers stored models solutions in their user directories. To this day I wonder if this was an accidental slip of group read permissions, or a subtle encouragement of outside the box problem solving.

This foray into classic and still widely used geophysical tools was followed out by a course in FORTRAN 77 at Utrecht Univeristy, modelling planetary density and gravity profiles. After this course I was hooked. Never again would I compute something by hand when *the computer can do it better*. I decided to pick the most-computing heavy MSci project I could find.

In typical university fashion, my MSci project was centered around using a convoluted series of MATLAB scripts far beyond my understanding to Do Science. In my case, this was analyzing a seismic dataset to reconstruct sound velocites of subsurface rock units. The project was a lot of fun, particularly plotting the results, but the scripts passed down from my supervisor were a black box to me. At the time, I assuumed this was how all academic software was.

# Development and FOSS

Beginning my PhD in oceanography, I began by using the tool most familiar to me and used by research group, namely MATLAB. 6 months into my studies however, I had a transformational experience in the form of an introductory Python course organised by the great [Denis Sergeev](https://dennissergeev.github.io/). In three short days I was introduced to a beautiful open language, and a wider ecosystem of open source. I took a month to convert my work to date into Python and haven't looked back since.

Learning Python was transformational. Being taught the methods of open source made me a user of Linux, not just as a free alternative to Windows, but as an alternative way of organising.

# Learner to developer

A few attending the introductory Python course, I joined my first open source community. Denis moved on to pastures new, and someone needed to take over the humble UEA Scientific Python Python Group. When no expert volunteered, I took on the job. It was a steep learning curve. I broke the website almost immediately and flailed around for anything in Python I knew enough of to present a seminar on.

Alongside Python, I started using more open source tools, notably Git and Jupyter. Both of these were instrumental in transforming my day-to-day work into something reasonably repeatable and robust.

Most of my learning was driven by necessity, hitting a problem in my research and reaching out for a tool to fix it. I started passing minor milestones more or less by accident. Setting up GitHub repos to back up my work, creating computational notebooks to share results with my supervisors, submitting a PR to an open source package to add functionality I needed, putting Fabio Crameri's colourmaps on PyPI and conda-forge so I didn't have to manually install them each time, joining a hackathon. None of these seemed important as I was doing them, I just needed to get a problem solved for my next tutor meeting, but they added up to something resembling an open source developer.

# Thoughts on this path

From informal discussions with other earth scientists, mine is a fairly typical experience. Most of us are not formally trained software engineers. I was very lucky to get on that intro to Python in the first year of my PhD. I had the luxury of taking a month to re-orient myself to open source. This is a very fragile pipeline though. There are people making great efforts to improve software literacy within research groups, particulalry [The Carpentries](https://carpentries.org/) and the [Society of Research Software Engineering](https://society-rse.org/). Change is slow in academia, but recognition of the value of open source is growing. There are many resources I wish I'd known about sooner. I try to help point junior researchers in my School to find the information they need and build more of a community. It's hard work, but in my view, more important than the research I produce in my 9-5.












