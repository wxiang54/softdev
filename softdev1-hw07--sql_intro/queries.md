# Standard SQL Queries
### Setup
```sql
CREATE TABLE peeps (
  name TEXT,
  age SMALLINT,
  id INT
);

CREATE TABLE courses (
  code TEXT,
  mark TINYINT,
  id INT
);
```


### Insertion
```sql
INSERT INTO peeps VALUES (
  "<name>",
  <age>,
  <id>
);

INSERT INTO courses VALUES (
  "<code>",
  <mark>,
  <id>
);
```


### Debugging
```sql
/* Show tables */
SELECT * FROM peeps;
SELECT * FROM courses;
```
