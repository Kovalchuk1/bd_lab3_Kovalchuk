CREATE TABLE country(
  id_country INT NOT NULL,
  country_name varchar(50) NOT NULL
);

CREATE TABLE genre(
  id_genre INT NOT NULL,
  genre_name varchar(50) NOT NULL
);

CREATE TABLE viewss(
  id_views INT NOT NULL,
  views_v INT NOT NULL,
  date_first  DATE DEFAULT CURRENT_DATE,
  date_last  DATE DEFAULT CURRENT_DATE
);

CREATE TABLE channel(
  ch_name char(50) NOT NULL,
  id_views INT NOT NULL,
  id_genre INT NOT NULL,
  id_country INT NOT NULL
);

ALTER TABLE channel ADD PRIMARY KEY (ch_name); 
ALTER TABLE viewss ADD PRIMARY KEY (id_views); 
ALTER TABLE country ADD PRIMARY KEY (id_country); 
ALTER TABLE genre ADD PRIMARY KEY (id_genre); 
 
 
ALTER TABLE channel ADD CONSTRAINT FK_channel_country FOREIGN KEY (id_country) 
REFERENCES country(id_country);
ALTER TABLE genre ADD CONSTRAINT FK_channel_genre FOREIGN KEY (id_genre) 
REFERENCES genre(id_genre);
ALTER TABLE viewss ADD CONSTRAINT FK_channel_viewss FOREIGN KEY (id_views) 
REFERENCES viewss(id_views);


