# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.contrib.gis.db import models


class AerodromesPoint(models.Model):
    id = models.IntegerField(db_column='ogc_fid', primary_key=True)
    wkb_geometry = models.TextField(blank=True, null=True)  # This field type is a guess.
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
        db_table = 'aerodromes_point'


class AerodromesPolygon(models.Model):
    id = models.IntegerField(db_column='ogc_fid', primary_key=True)
    wkb_geometry = models.TextField(blank=True, null=True)  # This field type is a guess.
    osm_id = models.CharField(max_length=255, blank=True, null=True)
    osm_way_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    aeroway = models.CharField(max_length=255, blank=True, null=True)
    amenity = models.CharField(max_length=255, blank=True, null=True)
    admin_level = models.CharField(max_length=255, blank=True, null=True)
    barrier = models.CharField(max_length=255, blank=True, null=True)
    boundary = models.CharField(max_length=255, blank=True, null=True)
    building = models.CharField(max_length=255, blank=True, null=True)
    craft = models.CharField(max_length=255, blank=True, null=True)
    geological = models.CharField(max_length=255, blank=True, null=True)
    historic = models.CharField(max_length=255, blank=True, null=True)
    land_area = models.CharField(max_length=255, blank=True, null=True)
    landuse = models.CharField(max_length=255, blank=True, null=True)
    leisure = models.CharField(max_length=255, blank=True, null=True)
    man_made = models.CharField(max_length=255, blank=True, null=True)
    military = models.CharField(max_length=255, blank=True, null=True)
    natural = models.CharField(max_length=255, blank=True, null=True)
    office = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    shop = models.CharField(max_length=255, blank=True, null=True)
    sport = models.CharField(max_length=255, blank=True, null=True)
    tourism = models.CharField(max_length=255, blank=True, null=True)
    other_tags = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'aerodromes_polygon'


class AllRoads(models.Model):
    id = models.IntegerField(db_column='ogc_fid', primary_key=True)
    wkb_geometry = models.TextField(blank=True, null=True)  # This field type is a guess.
    osm_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    highway = models.CharField(max_length=255, blank=True, null=True)
    waterway = models.CharField(max_length=255, blank=True, null=True)
    aerialway = models.CharField(max_length=255, blank=True, null=True)
    barrier = models.CharField(max_length=255, blank=True, null=True)
    man_made = models.CharField(max_length=255, blank=True, null=True)
    other_tags = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'all_roads'


class Banks(models.Model):
    id = models.IntegerField(db_column='ogc_fid', primary_key=True)
    wkb_geometry = models.PointField(blank=True, null=True)  # This field type is a guess.
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


class Buildings(models.Model):
    id = models.IntegerField(db_column='ogc_fid', primary_key=True)
    wkb_geometry = models.TextField(blank=True, null=True)  # This field type is a guess.
    osm_id = models.CharField(max_length=255, blank=True, null=True)
    osm_way_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    aeroway = models.CharField(max_length=255, blank=True, null=True)
    amenity = models.CharField(max_length=255, blank=True, null=True)
    admin_level = models.CharField(max_length=255, blank=True, null=True)
    barrier = models.CharField(max_length=255, blank=True, null=True)
    boundary = models.CharField(max_length=255, blank=True, null=True)
    building = models.CharField(max_length=255, blank=True, null=True)
    craft = models.CharField(max_length=255, blank=True, null=True)
    geological = models.CharField(max_length=255, blank=True, null=True)
    historic = models.CharField(max_length=255, blank=True, null=True)
    land_area = models.CharField(max_length=255, blank=True, null=True)
    landuse = models.CharField(max_length=255, blank=True, null=True)
    leisure = models.CharField(max_length=255, blank=True, null=True)
    man_made = models.CharField(max_length=255, blank=True, null=True)
    military = models.CharField(max_length=255, blank=True, null=True)
    natural = models.CharField(max_length=255, blank=True, null=True)
    office = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    shop = models.CharField(max_length=255, blank=True, null=True)
    sport = models.CharField(max_length=255, blank=True, null=True)
    tourism = models.CharField(max_length=255, blank=True, null=True)
    other_tags = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'buildings'


class Cities(models.Model):
    id = models.IntegerField(db_column='ogc_fid', primary_key=True)
    wkb_geometry = models.PointField(blank=True, null=True)  # This field type is a guess.
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
        db_table = 'cities'


class Farms(models.Model):
    id = models.IntegerField(db_column='ogc_fid', primary_key=True)
    wkb_geometry = models.TextField(blank=True, null=True)  # This field type is a guess.
    osm_id = models.CharField(max_length=255, blank=True, null=True)
    osm_way_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    aeroway = models.CharField(max_length=255, blank=True, null=True)
    amenity = models.CharField(max_length=255, blank=True, null=True)
    admin_level = models.CharField(max_length=255, blank=True, null=True)
    barrier = models.CharField(max_length=255, blank=True, null=True)
    boundary = models.CharField(max_length=255, blank=True, null=True)
    building = models.CharField(max_length=255, blank=True, null=True)
    craft = models.CharField(max_length=255, blank=True, null=True)
    geological = models.CharField(max_length=255, blank=True, null=True)
    historic = models.CharField(max_length=255, blank=True, null=True)
    land_area = models.CharField(max_length=255, blank=True, null=True)
    landuse = models.CharField(max_length=255, blank=True, null=True)
    leisure = models.CharField(max_length=255, blank=True, null=True)
    man_made = models.CharField(max_length=255, blank=True, null=True)
    military = models.CharField(max_length=255, blank=True, null=True)
    natural = models.CharField(max_length=255, blank=True, null=True)
    office = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    shop = models.CharField(max_length=255, blank=True, null=True)
    sport = models.CharField(max_length=255, blank=True, null=True)
    tourism = models.CharField(max_length=255, blank=True, null=True)
    other_tags = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'farms'


class Forest(models.Model):
    id = models.IntegerField(db_column='ogc_fid', primary_key=True)
    wkb_geometry = models.TextField(blank=True, null=True)  # This field type is a guess.
    osm_id = models.CharField(max_length=255, blank=True, null=True)
    osm_way_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    aeroway = models.CharField(max_length=255, blank=True, null=True)
    amenity = models.CharField(max_length=255, blank=True, null=True)
    admin_level = models.CharField(max_length=255, blank=True, null=True)
    barrier = models.CharField(max_length=255, blank=True, null=True)
    boundary = models.CharField(max_length=255, blank=True, null=True)
    building = models.CharField(max_length=255, blank=True, null=True)
    craft = models.CharField(max_length=255, blank=True, null=True)
    geological = models.CharField(max_length=255, blank=True, null=True)
    historic = models.CharField(max_length=255, blank=True, null=True)
    land_area = models.CharField(max_length=255, blank=True, null=True)
    landuse = models.CharField(max_length=255, blank=True, null=True)
    leisure = models.CharField(max_length=255, blank=True, null=True)
    man_made = models.CharField(max_length=255, blank=True, null=True)
    military = models.CharField(max_length=255, blank=True, null=True)
    natural = models.CharField(max_length=255, blank=True, null=True)
    office = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    shop = models.CharField(max_length=255, blank=True, null=True)
    sport = models.CharField(max_length=255, blank=True, null=True)
    tourism = models.CharField(max_length=255, blank=True, null=True)
    other_tags = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'forest'


class Grassland(models.Model):
    id = models.IntegerField(db_column='ogc_fid', primary_key=True)
    wkb_geometry = models.TextField(blank=True, null=True)  # This field type is a guess.
    osm_id = models.CharField(max_length=255, blank=True, null=True)
    osm_way_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    aeroway = models.CharField(max_length=255, blank=True, null=True)
    amenity = models.CharField(max_length=255, blank=True, null=True)
    admin_level = models.CharField(max_length=255, blank=True, null=True)
    barrier = models.CharField(max_length=255, blank=True, null=True)
    boundary = models.CharField(max_length=255, blank=True, null=True)
    building = models.CharField(max_length=255, blank=True, null=True)
    craft = models.CharField(max_length=255, blank=True, null=True)
    geological = models.CharField(max_length=255, blank=True, null=True)
    historic = models.CharField(max_length=255, blank=True, null=True)
    land_area = models.CharField(max_length=255, blank=True, null=True)
    landuse = models.CharField(max_length=255, blank=True, null=True)
    leisure = models.CharField(max_length=255, blank=True, null=True)
    man_made = models.CharField(max_length=255, blank=True, null=True)
    military = models.CharField(max_length=255, blank=True, null=True)
    natural = models.CharField(max_length=255, blank=True, null=True)
    office = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    shop = models.CharField(max_length=255, blank=True, null=True)
    sport = models.CharField(max_length=255, blank=True, null=True)
    tourism = models.CharField(max_length=255, blank=True, null=True)
    other_tags = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'grassland'


class Hamlets(models.Model):
    id = models.IntegerField(db_column='ogc_fid', primary_key=True)
    wkb_geometry = models.TextField(blank=True, null=True)  # This field type is a guess.
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
        db_table = 'hamlets'


class Helipads(models.Model):
    id = models.IntegerField(db_column='ogc_fid', primary_key=True)
    wkb_geometry = models.TextField(blank=True, null=True)  # This field type is a guess.
    osm_id = models.CharField(max_length=255, blank=True, null=True)
    osm_way_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    aeroway = models.CharField(max_length=255, blank=True, null=True)
    amenity = models.CharField(max_length=255, blank=True, null=True)
    admin_level = models.CharField(max_length=255, blank=True, null=True)
    barrier = models.CharField(max_length=255, blank=True, null=True)
    boundary = models.CharField(max_length=255, blank=True, null=True)
    building = models.CharField(max_length=255, blank=True, null=True)
    craft = models.CharField(max_length=255, blank=True, null=True)
    geological = models.CharField(max_length=255, blank=True, null=True)
    historic = models.CharField(max_length=255, blank=True, null=True)
    land_area = models.CharField(max_length=255, blank=True, null=True)
    landuse = models.CharField(max_length=255, blank=True, null=True)
    leisure = models.CharField(max_length=255, blank=True, null=True)
    man_made = models.CharField(max_length=255, blank=True, null=True)
    military = models.CharField(max_length=255, blank=True, null=True)
    natural = models.CharField(max_length=255, blank=True, null=True)
    office = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    shop = models.CharField(max_length=255, blank=True, null=True)
    sport = models.CharField(max_length=255, blank=True, null=True)
    tourism = models.CharField(max_length=255, blank=True, null=True)
    other_tags = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'helipads'


class Hotels(models.Model):
    id = models.IntegerField(db_column='ogc_fid', primary_key=True)
    wkb_geometry = models.TextField(blank=True, null=True)  # This field type is a guess.
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
        db_table = 'hotels'


class IdpCamps(models.Model):
    id = models.IntegerField(db_column='ogc_fid', primary_key=True)
    wkb_geometry = models.TextField(blank=True, null=True)  # This field type is a guess.
    osm_id = models.CharField(max_length=255, blank=True, null=True)
    osm_way_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    aeroway = models.CharField(max_length=255, blank=True, null=True)
    amenity = models.CharField(max_length=255, blank=True, null=True)
    admin_level = models.CharField(max_length=255, blank=True, null=True)
    barrier = models.CharField(max_length=255, blank=True, null=True)
    boundary = models.CharField(max_length=255, blank=True, null=True)
    building = models.CharField(max_length=255, blank=True, null=True)
    craft = models.CharField(max_length=255, blank=True, null=True)
    geological = models.CharField(max_length=255, blank=True, null=True)
    historic = models.CharField(max_length=255, blank=True, null=True)
    land_area = models.CharField(max_length=255, blank=True, null=True)
    landuse = models.CharField(max_length=255, blank=True, null=True)
    leisure = models.CharField(max_length=255, blank=True, null=True)
    man_made = models.CharField(max_length=255, blank=True, null=True)
    military = models.CharField(max_length=255, blank=True, null=True)
    natural = models.CharField(max_length=255, blank=True, null=True)
    office = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    shop = models.CharField(max_length=255, blank=True, null=True)
    sport = models.CharField(max_length=255, blank=True, null=True)
    tourism = models.CharField(max_length=255, blank=True, null=True)
    other_tags = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'idp_camps'


class Lakes(models.Model):
    id = models.IntegerField(db_column='ogc_fid', primary_key=True)
    wkb_geometry = models.TextField(blank=True, null=True)  # This field type is a guess.
    osm_id = models.CharField(max_length=255, blank=True, null=True)
    osm_way_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    aeroway = models.CharField(max_length=255, blank=True, null=True)
    amenity = models.CharField(max_length=255, blank=True, null=True)
    admin_level = models.CharField(max_length=255, blank=True, null=True)
    barrier = models.CharField(max_length=255, blank=True, null=True)
    boundary = models.CharField(max_length=255, blank=True, null=True)
    building = models.CharField(max_length=255, blank=True, null=True)
    craft = models.CharField(max_length=255, blank=True, null=True)
    geological = models.CharField(max_length=255, blank=True, null=True)
    historic = models.CharField(max_length=255, blank=True, null=True)
    land_area = models.CharField(max_length=255, blank=True, null=True)
    landuse = models.CharField(max_length=255, blank=True, null=True)
    leisure = models.CharField(max_length=255, blank=True, null=True)
    man_made = models.CharField(max_length=255, blank=True, null=True)
    military = models.CharField(max_length=255, blank=True, null=True)
    natural = models.CharField(max_length=255, blank=True, null=True)
    office = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    shop = models.CharField(max_length=255, blank=True, null=True)
    sport = models.CharField(max_length=255, blank=True, null=True)
    tourism = models.CharField(max_length=255, blank=True, null=True)
    other_tags = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'lakes'


class MainRoads(models.Model):
    id = models.IntegerField(db_column='ogc_fid', primary_key=True)
    wkb_geometry = models.TextField(blank=True, null=True)  # This field type is a guess.
    osm_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    highway = models.CharField(max_length=255, blank=True, null=True)
    waterway = models.CharField(max_length=255, blank=True, null=True)
    aerialway = models.CharField(max_length=255, blank=True, null=True)
    barrier = models.CharField(max_length=255, blank=True, null=True)
    man_made = models.CharField(max_length=255, blank=True, null=True)
    other_tags = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'main_roads'


class MedicalPoint(models.Model):
    id = models.IntegerField(db_column='ogc_fid', primary_key=True)
    wkb_geometry = models.TextField(blank=True, null=True)  # This field type is a guess.
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
        db_table = 'medical_point'


class MedicalPolygon(models.Model):
    id = models.IntegerField(db_column='ogc_fid', primary_key=True)
    wkb_geometry = models.TextField(blank=True, null=True)  # This field type is a guess.
    osm_id = models.CharField(max_length=255, blank=True, null=True)
    osm_way_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    aeroway = models.CharField(max_length=255, blank=True, null=True)
    amenity = models.CharField(max_length=255, blank=True, null=True)
    admin_level = models.CharField(max_length=255, blank=True, null=True)
    barrier = models.CharField(max_length=255, blank=True, null=True)
    boundary = models.CharField(max_length=255, blank=True, null=True)
    building = models.CharField(max_length=255, blank=True, null=True)
    craft = models.CharField(max_length=255, blank=True, null=True)
    geological = models.CharField(max_length=255, blank=True, null=True)
    historic = models.CharField(max_length=255, blank=True, null=True)
    land_area = models.CharField(max_length=255, blank=True, null=True)
    landuse = models.CharField(max_length=255, blank=True, null=True)
    leisure = models.CharField(max_length=255, blank=True, null=True)
    man_made = models.CharField(max_length=255, blank=True, null=True)
    military = models.CharField(max_length=255, blank=True, null=True)
    natural = models.CharField(max_length=255, blank=True, null=True)
    office = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    shop = models.CharField(max_length=255, blank=True, null=True)
    sport = models.CharField(max_length=255, blank=True, null=True)
    tourism = models.CharField(max_length=255, blank=True, null=True)
    other_tags = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'medical_polygon'


class Military(models.Model):
    id = models.IntegerField(db_column='ogc_fid', primary_key=True)
    wkb_geometry = models.TextField(blank=True, null=True)  # This field type is a guess.
    osm_id = models.CharField(max_length=255, blank=True, null=True)
    osm_way_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    aeroway = models.CharField(max_length=255, blank=True, null=True)
    amenity = models.CharField(max_length=255, blank=True, null=True)
    admin_level = models.CharField(max_length=255, blank=True, null=True)
    barrier = models.CharField(max_length=255, blank=True, null=True)
    boundary = models.CharField(max_length=255, blank=True, null=True)
    building = models.CharField(max_length=255, blank=True, null=True)
    craft = models.CharField(max_length=255, blank=True, null=True)
    geological = models.CharField(max_length=255, blank=True, null=True)
    historic = models.CharField(max_length=255, blank=True, null=True)
    land_area = models.CharField(max_length=255, blank=True, null=True)
    landuse = models.CharField(max_length=255, blank=True, null=True)
    leisure = models.CharField(max_length=255, blank=True, null=True)
    man_made = models.CharField(max_length=255, blank=True, null=True)
    military = models.CharField(max_length=255, blank=True, null=True)
    natural = models.CharField(max_length=255, blank=True, null=True)
    office = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    shop = models.CharField(max_length=255, blank=True, null=True)
    sport = models.CharField(max_length=255, blank=True, null=True)
    tourism = models.CharField(max_length=255, blank=True, null=True)
    other_tags = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'military'


class Neighborhoods(models.Model):
    id = models.IntegerField(db_column='ogc_fid', primary_key=True)
    wkb_geometry = models.TextField(blank=True, null=True)  # This field type is a guess.
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
        db_table = 'neighborhoods'


class Orchards(models.Model):
    id = models.IntegerField(db_column='ogc_fid', primary_key=True)
    wkb_geometry = models.TextField(blank=True, null=True)  # This field type is a guess.
    osm_id = models.CharField(max_length=255, blank=True, null=True)
    osm_way_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    aeroway = models.CharField(max_length=255, blank=True, null=True)
    amenity = models.CharField(max_length=255, blank=True, null=True)
    admin_level = models.CharField(max_length=255, blank=True, null=True)
    barrier = models.CharField(max_length=255, blank=True, null=True)
    boundary = models.CharField(max_length=255, blank=True, null=True)
    building = models.CharField(max_length=255, blank=True, null=True)
    craft = models.CharField(max_length=255, blank=True, null=True)
    geological = models.CharField(max_length=255, blank=True, null=True)
    historic = models.CharField(max_length=255, blank=True, null=True)
    land_area = models.CharField(max_length=255, blank=True, null=True)
    landuse = models.CharField(max_length=255, blank=True, null=True)
    leisure = models.CharField(max_length=255, blank=True, null=True)
    man_made = models.CharField(max_length=255, blank=True, null=True)
    military = models.CharField(max_length=255, blank=True, null=True)
    natural = models.CharField(max_length=255, blank=True, null=True)
    office = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    shop = models.CharField(max_length=255, blank=True, null=True)
    sport = models.CharField(max_length=255, blank=True, null=True)
    tourism = models.CharField(max_length=255, blank=True, null=True)
    other_tags = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'orchards'


class Paths(models.Model):
    id = models.IntegerField(db_column='ogc_fid', primary_key=True)
    wkb_geometry = models.TextField(blank=True, null=True)  # This field type is a guess.
    osm_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    highway = models.CharField(max_length=255, blank=True, null=True)
    waterway = models.CharField(max_length=255, blank=True, null=True)
    aerialway = models.CharField(max_length=255, blank=True, null=True)
    barrier = models.CharField(max_length=255, blank=True, null=True)
    man_made = models.CharField(max_length=255, blank=True, null=True)
    other_tags = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'paths'


class Placenames(models.Model):
    id = models.IntegerField(db_column='ogc_fid', primary_key=True)
    wkb_geometry = models.TextField(blank=True, null=True)  # This field type is a guess.
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
        db_table = 'placenames'


class PoliceStations(models.Model):
    id = models.IntegerField(db_column='ogc_fid', primary_key=True)
    wkb_geometry = models.TextField(blank=True, null=True)  # This field type is a guess.
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
        db_table = 'police_stations'


class Residential(models.Model):
    id = models.IntegerField(db_column='ogc_fid', primary_key=True)
    wkb_geometry = models.TextField(blank=True, null=True)  # This field type is a guess.
    osm_id = models.CharField(max_length=255, blank=True, null=True)
    osm_way_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    aeroway = models.CharField(max_length=255, blank=True, null=True)
    amenity = models.CharField(max_length=255, blank=True, null=True)
    admin_level = models.CharField(max_length=255, blank=True, null=True)
    barrier = models.CharField(max_length=255, blank=True, null=True)
    boundary = models.CharField(max_length=255, blank=True, null=True)
    building = models.CharField(max_length=255, blank=True, null=True)
    craft = models.CharField(max_length=255, blank=True, null=True)
    geological = models.CharField(max_length=255, blank=True, null=True)
    historic = models.CharField(max_length=255, blank=True, null=True)
    land_area = models.CharField(max_length=255, blank=True, null=True)
    landuse = models.CharField(max_length=255, blank=True, null=True)
    leisure = models.CharField(max_length=255, blank=True, null=True)
    man_made = models.CharField(max_length=255, blank=True, null=True)
    military = models.CharField(max_length=255, blank=True, null=True)
    natural = models.CharField(max_length=255, blank=True, null=True)
    office = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    shop = models.CharField(max_length=255, blank=True, null=True)
    sport = models.CharField(max_length=255, blank=True, null=True)
    tourism = models.CharField(max_length=255, blank=True, null=True)
    other_tags = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'residential'


class Restaurants(models.Model):
    id = models.IntegerField(db_column='ogc_fid', primary_key=True)
    wkb_geometry = models.TextField(blank=True, null=True)  # This field type is a guess.
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
        db_table = 'restaurants'


class Riverbanks(models.Model):
    id = models.IntegerField(db_column='ogc_fid', primary_key=True)
    wkb_geometry = models.TextField(blank=True, null=True)  # This field type is a guess.
    osm_id = models.CharField(max_length=255, blank=True, null=True)
    osm_way_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    aeroway = models.CharField(max_length=255, blank=True, null=True)
    amenity = models.CharField(max_length=255, blank=True, null=True)
    admin_level = models.CharField(max_length=255, blank=True, null=True)
    barrier = models.CharField(max_length=255, blank=True, null=True)
    boundary = models.CharField(max_length=255, blank=True, null=True)
    building = models.CharField(max_length=255, blank=True, null=True)
    craft = models.CharField(max_length=255, blank=True, null=True)
    geological = models.CharField(max_length=255, blank=True, null=True)
    historic = models.CharField(max_length=255, blank=True, null=True)
    land_area = models.CharField(max_length=255, blank=True, null=True)
    landuse = models.CharField(max_length=255, blank=True, null=True)
    leisure = models.CharField(max_length=255, blank=True, null=True)
    man_made = models.CharField(max_length=255, blank=True, null=True)
    military = models.CharField(max_length=255, blank=True, null=True)
    natural = models.CharField(max_length=255, blank=True, null=True)
    office = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    shop = models.CharField(max_length=255, blank=True, null=True)
    sport = models.CharField(max_length=255, blank=True, null=True)
    tourism = models.CharField(max_length=255, blank=True, null=True)
    other_tags = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'riverbanks'


class Rivers(models.Model):
    id = models.IntegerField(db_column='ogc_fid', primary_key=True)
    wkb_geometry = models.TextField(blank=True, null=True)  # This field type is a guess.
    osm_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    highway = models.CharField(max_length=255, blank=True, null=True)
    waterway = models.CharField(max_length=255, blank=True, null=True)
    aerialway = models.CharField(max_length=255, blank=True, null=True)
    barrier = models.CharField(max_length=255, blank=True, null=True)
    man_made = models.CharField(max_length=255, blank=True, null=True)
    other_tags = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'rivers'


class SchoolsPoint(models.Model):
    id = models.IntegerField(db_column='ogc_fid', primary_key=True)
    wkb_geometry = models.TextField(blank=True, null=True)  # This field type is a guess.
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
        db_table = 'schools_point'


class SchoolsPolygon(models.Model):
    id = models.IntegerField(db_column='ogc_fid', primary_key=True)
    wkb_geometry = models.TextField(blank=True, null=True)  # This field type is a guess.
    osm_id = models.CharField(max_length=255, blank=True, null=True)
    osm_way_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    aeroway = models.CharField(max_length=255, blank=True, null=True)
    amenity = models.CharField(max_length=255, blank=True, null=True)
    admin_level = models.CharField(max_length=255, blank=True, null=True)
    barrier = models.CharField(max_length=255, blank=True, null=True)
    boundary = models.CharField(max_length=255, blank=True, null=True)
    building = models.CharField(max_length=255, blank=True, null=True)
    craft = models.CharField(max_length=255, blank=True, null=True)
    geological = models.CharField(max_length=255, blank=True, null=True)
    historic = models.CharField(max_length=255, blank=True, null=True)
    land_area = models.CharField(max_length=255, blank=True, null=True)
    landuse = models.CharField(max_length=255, blank=True, null=True)
    leisure = models.CharField(max_length=255, blank=True, null=True)
    man_made = models.CharField(max_length=255, blank=True, null=True)
    military = models.CharField(max_length=255, blank=True, null=True)
    natural = models.CharField(max_length=255, blank=True, null=True)
    office = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    shop = models.CharField(max_length=255, blank=True, null=True)
    sport = models.CharField(max_length=255, blank=True, null=True)
    tourism = models.CharField(max_length=255, blank=True, null=True)
    other_tags = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'schools_polygon'


class SpatialRefSys(models.Model):
    srid = models.IntegerField(primary_key=True)
    auth_name = models.CharField(max_length=256, blank=True, null=True)
    auth_srid = models.IntegerField(blank=True, null=True)
    srtext = models.CharField(max_length=2048, blank=True, null=True)
    proj4text = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spatial_ref_sys'


class Tracks(models.Model):
    id = models.IntegerField(db_column='ogc_fid', primary_key=True)
    wkb_geometry = models.TextField(blank=True, null=True)  # This field type is a guess.
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
        db_table = 'tracks'


class TrainStations(models.Model):
    id = models.IntegerField(db_column='ogc_fid', primary_key=True)
    wkb_geometry = models.TextField(blank=True, null=True)  # This field type is a guess.
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
        db_table = 'train_stations'


class VillageGreen(models.Model):
    id = models.IntegerField(db_column='ogc_fid', primary_key=True)
    wkb_geometry = models.TextField(blank=True, null=True)  # This field type is a guess.
    osm_id = models.CharField(max_length=255, blank=True, null=True)
    osm_way_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    aeroway = models.CharField(max_length=255, blank=True, null=True)
    amenity = models.CharField(max_length=255, blank=True, null=True)
    admin_level = models.CharField(max_length=255, blank=True, null=True)
    barrier = models.CharField(max_length=255, blank=True, null=True)
    boundary = models.CharField(max_length=255, blank=True, null=True)
    building = models.CharField(max_length=255, blank=True, null=True)
    craft = models.CharField(max_length=255, blank=True, null=True)
    geological = models.CharField(max_length=255, blank=True, null=True)
    historic = models.CharField(max_length=255, blank=True, null=True)
    land_area = models.CharField(max_length=255, blank=True, null=True)
    landuse = models.CharField(max_length=255, blank=True, null=True)
    leisure = models.CharField(max_length=255, blank=True, null=True)
    man_made = models.CharField(max_length=255, blank=True, null=True)
    military = models.CharField(max_length=255, blank=True, null=True)
    natural = models.CharField(max_length=255, blank=True, null=True)
    office = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    shop = models.CharField(max_length=255, blank=True, null=True)
    sport = models.CharField(max_length=255, blank=True, null=True)
    tourism = models.CharField(max_length=255, blank=True, null=True)
    other_tags = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'village_green'


class Villages(models.Model):
    id = models.IntegerField(db_column='ogc_fid', primary_key=True)
    wkb_geometry = models.TextField(blank=True, null=True)  # This field type is a guess.
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
        db_table = 'villages'
