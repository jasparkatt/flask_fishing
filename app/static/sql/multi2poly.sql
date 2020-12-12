CREATE TABLE watershed_count AS
SELECT gid, wi_watersheds_2017.wshed_name, (ST_DUMP(geom)).geom::geometry(Polygon,4326) AS geom FROM wi_watersheds_2017;