CREATE DATABASE IF NOT EXISTS Library;


USE Library;


CREATE TABLE Books 
(
    BookId INT PRIMARY KEY,
    Title VARCHAR(50),
    Author VARCHAR(50),
    PublicationYear INT
);

ALTER TABLE Books
RENAME TO BookCollection;

ALTER TABLE BookCollection
ADD COLUMN Genre VARCHAR(30);


INSERT INTO BookCollection (BookId, Title, Author, PublicationYear, Genre)
VALUES 
    (1, 'To Kill a Mockingbird', 'Harper Lee', 1960, 'Fiction'),
    (2, '1984', 'George Orwell', 1949, 'Dystopian'),
    (3, 'Pride and Prejudice', 'Jane Austen', 1813, 'Romance');

SELECT * FROM BookCollection;


UPDATE BookCollection
SET Author = 'Harper Lee Jr.'
WHERE BookId = 1;


DELETE FROM BookCollection
WHERE BookId = 3;


SELECT * FROM BookCollection;

