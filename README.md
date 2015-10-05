loco: LOcation COlombia
=================

Teaching OSM and GeoDjango with local data.

Installation
============

 1. Install osmosis
 2. Install latest gdal with spatialite, expat and python
 3. Install postgres with postgis
 4. Install latest Django

Configuration
=============

 1. createdb loco
 2. psql loco
 3. CREATE EXTENSION postgis;
 4. CREATE EXTENSION hstore;
 5. make cities.postgis
