select * from channel;
create table channelcopy as select * from channel; 
delete from channelcopy;
select * from channelcopy;


DO $$
 DECLARE
     name_ch	  channelcopy.ch_name%TYPE;
	 views_ch     channelcopy.ch_views%TYPE;
	 ch_sub       channelcopy.ch_subscribers%TYPE;
     id_genrech   channelcopy.id_genre%TYPE;
     id_countrych channelcopy.id_country%TYPE;

 BEGIN
 	 name_ch := 'channel-';
	 views_ch := 2500;
	 ch_sub := 100;
     id_genrech := 0;
     id_countrych := 1;
     FOR counter IN 1..10
         LOOP
            INSERT INTO channelcopy (ch_name, ch_views, ch_subscribers, id_genre, id_country)
             VALUES (name_ch || counter + 1, views_ch + counter, ch_sub - counter + 10,  counter + 1, counter + 1);
         END LOOP;
 END;
 $$