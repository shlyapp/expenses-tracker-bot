CREATE TABLE category(
  id integer primary key,
  name varchar(255)
);

CREATE TABLE expense(
  id integer primary key,
  amount integer,
  created datetime,
  category_name varchar(255),
  comment_text,
  FOREIGN KEY(category_name) REFERENCES category(name)
);

INSERT INTO category (id, name)
VALUES 
  (0, "Транспорт"),
  (1, "Продукты"),
  (2, "Развелечения"),
  (3, "Прочее");

