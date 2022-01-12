-- Reproducible sample of 15% (~2.4 million rows) of the flights table using Postgres.
SELECT * FROM flights TABLESAMPLE BERNOULLI(15) REPEATABLE(42)

-- Obtaining the submission subset of flights_test (flights between Jan. 01 and Jan. 7 of 2020 inclusive).
SELECT fl_date, mkt_carrier, mkt_carrier_fl_num, origin, dest 
FROM flights_test 
WHERE fl_date BETWEEN '2020-01-01' AND '2020-01-08'