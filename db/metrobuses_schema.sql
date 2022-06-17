CREATE TABLE alcaldias(
  _id INTEGER NOT NULL PRIMARY KEY,
  id INTEGER NOT NULL,
  nomgeo TEXT NOT NULL,
  cve_mun INTEGER NOT NULL,
  cve_ent INTEGER NOT NULL,
  cvegeo INTEGER NOT NULL,
  geo_point_2d TEXT NOT NULL,
  geo_shape TEXT NOT NULL,
  municipio INTEGER NOT NULL
);

CREATE TABLE metrobuses(
  _id INTEGER NOT NULL PRIMARY KEY,
  id INTEGER NOT NULL,
  date_updated TEXT NOT NULL,
  vehicle_id INTEGER NOT NULL,
  vehicle_label INTEGER NOT NULL,
  vehicle_current_status INTEGER NOT NULL,
  position_latitude REAL NOT NULL,
  position_longitude REAL NOT NULL,
  geographic_point TEXT NOT NULL,
  position_speed INTEGER NOT NULL,
  position_odometer INTEGER NOT NULL,
  trip_schedule_relationship INTEGER NOT NULL,
  trip_id INTEGER DEFAULT NULL,
  trip_start_date INTEGER DEFAULT NULL,
  trip_route_id INTEGER DEFAULT NULL
);
