DROP TABLE participation;
DROP TABLE athlete;
DROP TABLE event;

-- athletes table
CREATE TABLE athlete (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255)
);

-- events table
CREATE TABLE event (
  id SERIAL PRIMARY KEY,
  sport VARCHAR(255),
  name VARCHAR(255)
);

-- make joining table 
CREATE TABLE participation (
  id SERIAL PRIMARY KEY,
  athlete_id INT NOT NULL REFERENCES athlete(id) ON DELETE CASCADE,
  event_id INT NOT NULL REFERENCES event(id) ON DELETE CASCADE,
  position INT
);
