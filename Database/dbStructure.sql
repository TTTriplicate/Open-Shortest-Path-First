CREATE DATABASE dijkstra;

CREATE USER 'dijkstra'@'%' IDENTIFIED BY 'G3n3r1cP@ssw0rd!';
GRANT ALL PRIVILEGES ON dijkstra.* TO 'dijkstra'@'%';

USE dijkstra;

CREATE TABLE nodes(
    node_id int primary key
);

CREATE TABLE edges(
    source int,
    destination int,
    weight int,
    foreign key (source) references nodes(node_id),
    foreign key (destination) references nodes(node_id)
);

INSERT INTO nodes(node_id) 
VALUES
    (0),
    (1), 
    (2), 
    (4), 
    (5), 
    (7), 
    (9), 
    (10);

INSERT INTO edges(source, destination, weight) 
VALUES
    (0, 1, 1),
    (0, 4, 8),
    (0, 7, 4),
    (1, 4, 6),
    (1, 2, 2),
    (2, 4, 6),
    (2, 5, 2),
    (2, 9, 1),
    (9, 5, 1),
    (9, 10, 4),
    (7, 4, 5),
    (5, 4, 1),
    (5, 10, 1);