LOcation COlombia
=================

Teaching OSM and GeoDjango with local data.

Installation
============

 #. Install osmosis
 #. Install latest gdal with spatialite, expat and python
 #. Install postgres with postgis
 #. Install latest Django

Configuration
=============

 #. createdb loco
 #. psql loco
 #. CREATE EXTENSION postgis;
 #. CREATE EXTENSION hstore;
 #. make cities.postgis
