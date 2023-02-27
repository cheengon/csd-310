# Database initializations script
# Author: Mario Calderon


# Create the whatabook Database
CREATE DATABASE whatabook;

# Create user account with permissions to use the DB
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';
GRANT ALL PRIVILEGES ON whatabook.* TO 'whatabook_user'@'localhost';

# Switch to use the whatabook DB and begin the initialization of the schema
USE whatabook;

# Table: store
CREATE TABLE store (
    store_id    INT UNSIGNED    NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

# Table: book
CREATE TABLE book (
    book_id     INT UNSIGNED    NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

# Table: user
CREATE TABLE user (
    user_id         INT UNSIGNED    NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75)     NOT NULL,
    last_name       VARCHAR(75)     NOT NULL,
    PRIMARY KEY(user_id) 
);

# Table: wishlist
CREATE TABLE wishlist (
    wishlist_id     INT UNSIGNED    NOT NULL    AUTO_INCREMENT,
    user_id         INT UNSIGNED    NOT NULL,
    book_id         INT UNSIGNED    NOT NULL,
    PRIMARY KEY(wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_id),
    INDEX idx_wishlist_user_id (user_id),
    INDEX idx_wishlist_book_id (book_id)
);

# Create user accounts
INSERT INTO user (first_name, last_name)
VALUES
    ('Mike', 'Piazza'),
    ('Mookie', 'Betts'),
    ('Kirk', 'Gibson');

# Create Book List
INSERT INTO book (book_name, author, details)
VALUES
    ('The Hidden World', 'Tara Sanderson', 'A thrilling mystery set in the heart of the Amazon rainforest.'),
    ('The Last Time', 'Ryan Johnson', 'A heart-wrenching story of love, loss, and redemption.'),
    ('The Forgotten Island', 'Sarah Black', 'An exciting adventure tale of a group of survivors stranded on a deserted island.'),
    ('The Secret Room', 'Rachel Taylor', 'A gripping suspense story of a woman who discovers a hidden room in her new home.'),
    ('The Lost Treasure', 'Alex Thompson', 'A fun and exciting treasure hunt for the whole family.'),
    ('The Perfect Stranger', 'Amanda Jones', 'A twisty psychological thriller that will keep you guessing until the very end.'),
    ('The Road Home', 'Emily Carter', 'A heartwarming story of a young woman who returns to her hometown to find her place in the world.'),
    ('The Midnight Caller', 'Jake Williams', 'A creepy and atmospheric horror story about a mysterious phone call that leads to terror.'),
    ('The Enchanted Forest', 'Megan Lee', 'A magical tale of a young girl who discovers a hidden forest full of wonders and secrets.');

# Create Store Location
INSERT INTO store (locale)
VALUES ('2304 San Diego Ave Ste A, San Diego, CA 92110');

# Add one book to each user's wishlist
INSERT INTO wishlist (user_id, book_id)
VALUES 
    ((SELECT user_id FROM user WHERE first_name = 'Mike'), 
     (SELECT book_id FROM book WHERE book_name = 'The Hidden World')),
    ((SELECT user_id FROM user WHERE first_name = 'Mookie'),
     (SELECT book_id FROM book WHERE book_name = 'The Last Time')),
    ((SELECT user_id FROM user WHERE first_name = 'Kirk'),
     (SELECT book_id FROM book WHERE book_name = 'The Forgotten Island'));



