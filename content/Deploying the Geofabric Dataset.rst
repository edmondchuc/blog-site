Deploying the Geofabric Dataset
===============================


:date: 2018-11-27 21:55
:category: Software Development
:author: Edmond Chuc
:tags: Geoserver, Geofabric, Linked Data, PostgreSQL, OpenStreetMaps, Web, GIS
:summary: A self-reflection on the Location Index Project.


I worked as a software developer in the technical team of the Location Index project. The team consisted of 3 members; a senior scientific researcher who was also our technical lead, a senior software developer and myself.

I was assigned the task to expose the `Bureau of Meteorology's`_ `Geofabric`_ dataset as a `Web Feature Service`_ (WFS) as well as a `Web Map Service`_ (WMS). The WMS was required to overlay the features of the Geofabric on top of a styled map of Australia.

My first step was to import the Geofabric dataset into a PostgreSQL datastore. I then set up a Geoserver instance to symbolically link to the PostgreSQL datastore. To fulfil the requirement of a styled map, I imported OpenStreetMap data of Australia into the PostgreSQL datastore and styled it in CSS so that it looked like Google Maps. I was then able to contruct layers in Geoserver and serve them via WFS and WMS endpoints. Issues arose when the WMS was embedded inside HTML iframes due to CORS rules. This issue could not be resolved directly so I created a proxypass in Apache to force the WMS to *think* it was on the same network.

The outcome of the task was a success and the results of my actions allowed my team and I to deliver the Geofabric as a `Linked Data`_ product. Without the Geoserver exposing the dataset as WFS and WMS, it would have been quite difficult to create a Linked Data API with features overlaid on a geo-spatial map.

This experience has shown me how to tackle new technology that I am unfamiliar with. I learned the importance of *learning by example* by watching video tutorials and reading lots of documentation. I am aware that the Geoserver is a rather *ancient* tool for exposing WFS and WMS so I plan to investigate in more modern technologies such as `Mapbox`_ for my future GIS-related projects.


.. _Bureau of Meteorology's: http://www.bom.gov.au
.. _Geofabric: http://www.bom.gov.au/water/geofabric/
.. _Web Feature Service: https://en.wikipedia.org/wiki/Web_Feature_Service
.. _Web Map Service: https://en.wikipedia.org/wiki/Web_Map_Service
.. _Linked Data: http://www.linked.data.gov.au
.. _Mapbox: https://www.mapbox.com
