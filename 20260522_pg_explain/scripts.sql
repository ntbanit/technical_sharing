EXPLAIN SELECT * FROM tenk1;

SELECT relpages, reltuples FROM pg_class WHERE relname = 'tenk1';


EXPLAIN SELECT * FROM tenk1 WHERE unique1 < 7000;

EXPLAIN SELECT * FROM tenk1 WHERE unique1 < 100;

EXPLAIN SELECT * FROM tenk1 WHERE unique1 < 100 AND stringu1 = 'xxx';

EXPLAIN SELECT * FROM tenk1 WHERE unique1 = 42;


EXPLAIN SELECT * FROM tenk1 ORDER BY unique1;

EXPLAIN SELECT unique1 FROM tenk1 ORDER BY unique1;



EXPLAIN SELECT * FROM tenk1 ORDER BY hundred, ten LIMIT 100;

EXPLAIN SELECT * FROM tenk1 WHERE unique1 < 100 AND unique2 > 9000;


EXPLAIN SELECT * FROM tenk1 WHERE unique1 < 100 AND unique2 > 9000 limit 2;

EXPLAIN SELECT *
FROM tenk1 t1, tenk2 t2
WHERE t1.unique1 < 10 AND t1.unique2 = t2.unique2;





