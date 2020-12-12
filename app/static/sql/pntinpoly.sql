SELECT to_json(fav_county_json) FROM (SELECT * FROM all_spots) fav_county_json;

CREATE VIEW fav_watershed AS
SELECT watersheds.wshed_name, count(all_spots.geom) AS total 
FROM watersheds
LEFT JOIN all_spots ON st_contains(watersheds.geom,all_spots.geom)
GROUP BY watersheds.wshed_name
ORDER BY total DESC;

CREATE VIEW fav_county AS
SELECT county.county_nam, count(all_spots.geom) AS total
FROM county
LEFT JOIN all_spots ON st_contains(county.geom,all_spots.geom)
GROUP BY county.county_nam
ORDER BY total DESC;

CREATE VIEW fav_spots AS
SELECT all_spots.stream, count(all_spots.geom) AS total
FROM all_spots
LEFT JOIN county ON st_contains(county.geom,all_spots.geom)
GROUP BY all_spots.stream
ORDER BY total DESC;

CREATE VIEW trout_springs_county AS
SELECT county.county_nam, count(trout_spring_pond.geom) AS total 
FROM county
LEFT JOIN trout_spring_pond ON st_contains(county.geom,trout_spring_pond.geom)
GROUP BY county.county_nam
ORDER BY total DESC;

SELECT neighborhoods.name, COUNT(parcels_kcgis.geom) AS total
  FROM neighborhoods LEFT JOIN parcels_kcgis
    ON neighborhoods.geom && parcels_kcgis.geom 
   AND ST_Contains(neighborhoods.geom, ST_Centroid(parcels_kcgis.geom))
GROUP BY neighborhoods.name

SELECT 
spotxa.gid aid, 
spotxa.geom ageom, 
spotxb.gid bid, 
spotxb.geom bgeom, 
ST_Distance(spotxa.geom, spotxb.geom) dist 
FROM spotx spotxa, spotx spotxb 
WHERE spotxa.gid != spotxb.gid 
AND ST_DWithin(spotxa.geom, spotxb.geom,1000);

SELECT trout_streams.trout_clas, Sum((trout_streams.shapelen) * 0.000621371)
FROM trout_streams
GROUP BY trout_streams.trout_clas;

SELECT DISTINCT ON(g2.displaynam)  g1.gid As gref_gid, g1.county As gref_name, g2.id As gnn_id, 
g2.displaynam As gnn_name  
FROM habit_projs_pts As g2, spotx As g1   
WHERE g1.gid <> g2.id AND ST_DWithin(g1.geom, g2.geom, 300)   
ORDER BY g2.displaynam DESC, ST_Distance(g1.geom,g2.geom)


ogr2ogr -f GeoJSON
testing_ogr.json
-sql "select id, stream, county, st_x(geom) as x,st_y(geom)as y from all_spots limit 5;"

@app.route('/key')
def key():
    access_token = MAPBOX_ACCESS_TOKEN
    cursor.execute("select ST_AsGeoJSON(subq.*) from (select id, stream, county,geom from all_spots) as subq limit 5;")
    varcons = cursor.fetchall()
    geo_json = [] 
    for varcon in varcons:
        geo_json.append(varcons)                 
        return render_template('public/key.html', geo_json=geo_json)