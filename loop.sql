select * from channel;
create table channelcopy as select * from channel; 
delete from channelcopy;
select * from channelcopy;


DO $$
 DECLARE
     name_ch	  channelcopy.ch_name%TYPE;
     views_ch     channelcopy.id_views%TYPE;
     id_genrech   channelcopy.id_genre%TYPE;
     id_countrych channelcopy.id_country%TYPE;

 BEGIN
 	 name_ch := 'channel-';
	 views_ch := 2500;
     id_genrech := 0;
     id_countrych := 1;
     FOR counter IN 1..10
         LOOP
            INSERT INTO channelcopy (ch_name, id_views, id_genre, id_country)
             VALUES (name_ch || counter + 1, views_ch + counter,  counter + 1, counter + 1);
         END LOOP;
 END;
 $$
