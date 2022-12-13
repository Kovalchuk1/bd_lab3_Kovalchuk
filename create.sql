CREATE TABLE country(
  id_country INT NOT NULL,
  country_name varchar(50) NOT NULL
);

CREATE TABLE genre(
  id_genre INT NOT NULL,
  genre_name varchar(50) NOT NULL
);

CREATE TABLE channel(
  ch_name char(50) NOT NULL,
  ch_views INT NOT NULL,
  ch_subscribers INT NOT NULL,
  id_genre INT NOT NULL,
  id_country INT NOT NULL
);

ALTER TABLE country ADD PRIMARY KEY (id_country); 
ALTER TABLE genre ADD PRIMARY KEY (id_genre); 
 
 
ALTER TABLE channel ADD CONSTRAINT FK_channel_country FOREIGN KEY (id_country) 
REFERENCES country(id_country);
ALTER TABLE genre ADD CONSTRAINT FK_channel_genre FOREIGN KEY (id_genre) 
REFERENCES genre(id_genre);