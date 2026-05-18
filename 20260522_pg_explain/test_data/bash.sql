-- tenk1 & tenk2 (same structure)
CREATE TABLE tenk1 (
  unique1 int4, unique2 int4, two int4, four int4, ten int4,
  twenty int4, hundred int4, thousand int4, twothousand int4,
  fivethous int4, tenthous int4, odd int4, even int4,
  stringu1 name, stringu2 name, string4 name
);
CREATE INDEX tenk1_unique1 ON tenk1(unique1);
CREATE INDEX tenk1_unique2 ON tenk1(unique2);
CREATE INDEX tenk1_hundred ON tenk1(hundred);


CREATE TABLE tenk2 AS SELECT * FROM tenk1;
CREATE INDEX tenk2_unique1 ON tenk2(unique1);
CREATE INDEX tenk2_unique2 ON tenk2(unique2);
CREATE INDEX tenk2_hundred ON tenk2(hundred);

CREATE TABLE onek AS SELECT * FROM tenk1 LIMIT 0;

CREATE TABLE unit (un name, flt8 float8);

CREATE TABLE polygon_tbl (f1 polygon);


COPY tenk1 FROM 'D:/an.ntb/workspace/technical_sharings/test_data/tenk.data';
COPY tenk2 FROM 'D:/an.ntb/workspace/technical_sharings/test_data/tenk.data';
COPY onek  FROM 'D:/an.ntb/workspace/technical_sharings/test_data/onek.data';



-- unit table
INSERT INTO unit VALUES ('cm', 1.0), ('m', 100.0), ('km', 100000.0),
('in', 2.54), ('ft', 30.48), ('yd', 91.44), ('mi', 160934.4);

-- polygon_tbl
INSERT INTO polygon_tbl VALUES
('((1,1),(2,2))'), ('((0,0),(1,1),(2,0))'),
('((0,0),(2,0),(2,2),(0,2))'), ('((1,0),(2,1),(1,2),(0,1))');