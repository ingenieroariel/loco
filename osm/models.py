from __future__ import unicode_literals

from django.contrib.gis.db import models


class Banks(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ogc_fid')
    geom = models.PointField(blank=True, null=True, db_column='wkb_geometry')
    osm_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    barrier = models.CharField(max_length=255, blank=True, null=True)
    highway = models.CharField(max_length=255, blank=True, null=True)
    ref = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    is_in = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    man_made = models.CharField(max_length=255, blank=True, null=True)
    other_tags = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'banks'
