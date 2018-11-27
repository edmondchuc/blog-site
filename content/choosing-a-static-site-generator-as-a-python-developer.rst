Choosing a Static Site Generator as a Python Developer
======================================================

:date: 2018-11-18 21:51
:category: Software Development
:author: Edmond Chuc
:tags: Python, static site generator, Pelican, Jekyll, Hugo, Sphinx, blog, Ruby, Markdown, reStructured Text, web
:summary: An initial impressions on Pelican and some other static site generators.

I started looking into static site generators to simplify my workflow and the maintenance of my personal website. As with many before me, I stumbled across the popular names in static site generators such as `Jekyll`_, `Hugo`_ and others. At the time, I had a single-paged portfolio website set up, but I  wanted to also start blogging online to share my knowledge with others and have a medium to reflect on my learning experiences. I knew static site generators were the go-to solutions but I never expected how immensely powerful they were and how easy they were to use. Read on to see why I chose `Pelican`_ as my static site generator.

.. _Jekyll: https://jekyllrb.com/
.. _Hugo: https://gohugo.io/
.. _Pelican: https://github.com/getpelican/pelican

I initially started with Jekyll, the top-dog of static site generators, backed by GitHub. Their documentation was easy to follow and the installation process was reasonably straight forward. However, I soon ran into a problem. Jekyll was developed with Ruby, and I was not familiar with their technology stack. At the time I was a full-blown Python developer so naturally, all the jargon to do with Ruby like gems and bundlers were unfamiliar to me. Despite the clear and well-explained "Ruby 101" that Jekyll documentation provided, I started seeing the similar patterns of the Ruby ecosystem to Python's. This was in terms of static site generators and thought, if the workflow is so similar and that Python was fully capable of doing the same job, then I'd rather use something that's Python-based. This means that in the future, I'd have a much easier time creating extensions and themes for the static site generator since I was already adept with Python's technology stack.

I went on to `Static Gen`_, a website that is capable of filtering static site generators by programming languages and other variables. I filtered it for Python static site generators and it seemed the most popular one was Pelican. I started reading the Pelican documentation and soon realised how technically inspired the project was from `Sphinx`_, which was another popular static site generator, albeit used mostly for technical documentation.

.. _Static Gen: https://www.staticgen.com/
.. _Sphinx: http://www.sphinx-doc.org/en/master/

The installation process of Pelican was super easy. I was able to use a command line interface program to generate the configuration files for me by executing :code:`pelican-quickstart`. I was then able to easily create my first blog post in a simple Markdown file (or more recently, I've now switched to reStructured Text). I imaginatively named the file `hello_world.md` and wrote some basic content to test it out. To build, I had to run :code:`pelican content` and viewed it by serving the output using :code:`pelican --listen`. Magically, my Markdown content is now rendered perfectly in HTML.

Overall the experience of Pelican has surpassed my expectations. Since it is a Python framework as well as it being highly similar to Sphinx, you could say I was *ecstatic*. I was also very happy to know that if I wanted to, I could use reStructured Text, which an easy-to-use markup language like Markdown albeit much more powerful. Time to get busy and look into theming Pelican.
