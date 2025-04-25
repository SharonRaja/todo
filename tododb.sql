SELECT tablename
FROM pg_catalog.pg_tables
WHERE schemaname != 'pg_catalog' AND schemaname != 'information_schema';

SELECT column_name, data_type, character_maximum_length, is_nullable
FROM information_schema.columns
WHERE table_name = 'auth_user';

select * from auth_user;

CREATE TABLE tag (
  id SERIAL PRIMARY KEY,
  tag_name VARCHAR (10) UNIQUE NOT NULL
);


select * from tag

-- insert into tag(tag_name) values('Kitchen');

CREATE TABLE task (
  task_id SERIAL PRIMARY KEY,
  task_detail VARCHAR (100) NOT NULL,
  is_done boolean NOT NULL DEFAULT FALSE,
  tag_id INTEGER REFERENCES tag(id),
  user_id INTEGER REFERENCES auth_user(id),
  created_at TIMESTAMP DEFAULT NOW()
);

-- Task 1: Linked to tag_id 1 and user_id 101
INSERT INTO task (task_detail, is_done, tag_id, user_id, created_at)
VALUES ('Clean the kitchen', FALSE, 4, 2, NOW());

-- Task 2: Linked to tag_id 2 and user_id 102
INSERT INTO task (task_detail, is_done, tag_id, user_id, created_at)
VALUES ('Prepare dinner', FALSE, 1, 2, NOW());

-- Task 3: Linked to tag_id 3 and user_id 103
INSERT INTO task (task_detail, is_done, tag_id, user_id, created_at)
VALUES ('Grocery shopping', TRUE, 3, 2, NOW());

-- Task 4: Linked to tag_id 1 and user_id 104
INSERT INTO task (task_detail, is_done, tag_id, user_id, created_at)
VALUES ('Create sales report', FALSE, 2, 2, NOW());

select * from task;


