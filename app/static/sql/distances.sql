-- Closest 10 streams to point id
SELECT
	streams.id,
	streams.local_name,
	streams.geom
FROM
	class_1_2 streams
ORDER BY
	streams.geom <->
	(SELECT geom FROM all_spots WHERE id = 1)
LIMIT 10;

-- find all points along a given stream segment within a distance
SELECT x.*, ST_Distance(streams.geom, x.geom)/1000.0 AS distance_km
FROM class_1_2 streams, all_spots x
WHERE streams.local_name = 'Bishop Branch' AND ST_DWithin(streams.geom, x.geom, 5000.0)
ORDER BY ST_LineLocatePoint(streams.geom, x.geom),
         ST_Distance(streams.geom, x.geom);

SELECT c.stream, b.geom, ST_Distance(c.geom, b.geom) As dist_m
FROM all_spots AS c CROSS JOIN class_1_2 As b
WHERE c.stream = 'Spirit River';

SELECT
  all_spots.id,
  all_spots.geom,
  closest_wi_springs.id,
  closest_wi_springs.dist,
  closest_wi_springs.name
FROM all_spots
CROSS JOIN LATERAL 
  (SELECT
     id,
   	 name,	
     ST_Distance(wi_springs.geom, all_spots.geom)/10 as dist
     FROM wi_springs
     ORDER BY all_spots.geom <-> wi_springs.geom
   LIMIT 1) AS closest_wi_springs
		 