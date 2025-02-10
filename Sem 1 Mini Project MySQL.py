create database aarush_events;


use aarush_events;


create table events (
     s_no int primary key not null auto_increment,
     EVENTS VARCHAR(100),
     VENUE VARCHAR(50),
     DATE VARCHAR(50),
     TIMING VARCHAR(50),
     CHARGES INT);



INSERT INTO EVENTS VALUES(1, "Stand-up Comedy", "B", "2 may", "|12:30pm|", 250),
(2, "Treasure Hunt", "A", "3 may", "|2:00pm|", 280),
(3, "Hackathon", "C", "3 may", "|5:30PM|", 300),
(4, "Marathon", "A", "4 may", "|3:00pm|", 250),
(5,"Space Workshop", "B", "2 may", "|5:30pm|", 280),
(6, "Celebrity Talk", "c", "4 may", "|6:00pm|", 280),
(7, "Aeroexspanz", "A", "5 may", "|4:30pm|", 250);

select * from events;
