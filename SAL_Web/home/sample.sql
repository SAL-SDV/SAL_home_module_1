--  INSERT INTO sal.imagelist
--   (path,imagedata)
--  VALUES
--   ('3.jpg','2019-08-23T01:02:27');
--  select * from sal.imagelist;
--  INSERT INTO sal.SensorList
--   (ID,Name)
--  VALUES
--   ('oiu','寝室');
--  select * from sal.imagelist;

-- SELECT path 
-- FROM sal.imagelist
-- where id = (select MAX(id) from sal.imagelist)

--  CREATE TABLE sal.ImageList (
--  ID int(11)  ,
--  ImageData datetime,
--  path varchar(255)
--  )
--  CREATE TABLE sal.SensorList (
--  ID varchar(5) not null primary key ,
--  Name varchar(100)
--  )
-- CREATE TABLE sal.SensorLog (
--     ID int(11),
--     SensorID varchar(5),
--     LogData datetime
--     );
--   INSERT INTO sal.SensorList
--    (ID, Name)
--   VALUES
--    ('sin','寝室');
-- ALTER TABLE sal.imagelist
--  RENAME COLUMN ImageData TO Date
--    INSERT INTO sal.SensorLog
--     (ID, SensorID,LogData)
--    VALUES
--     (3,'abc','2019-08-23T07:02:27');
-- update sal.SensorList
-- set Name = 'げん'
-- where ID = 'abc';
 select * from sal.imagelist;
 select * from sal.SensorList;
 select * from sal.SensorLog;
