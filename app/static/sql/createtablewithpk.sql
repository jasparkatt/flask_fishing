CREATE TABLE visited_county AS
SELECT county.id as pid, county.county_nam AS name, count(all_spots.geom) AS total
FROM county
LEFT JOIN all_spots ON st_contains(county.geom,all_spots.geom)
GROUP BY county.county_nam, county.id
ORDER BY total DESC;
ALTER TABLE visited_county ADD PRIMARY KEY(pid);