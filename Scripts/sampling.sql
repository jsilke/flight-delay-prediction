-- Reproducible sample of 15% (~2.4 million rows) of the flights table using Postgres.
SELECT * FROM flights TABLESAMPLE BERNOULLI(15) REPEATABLE(42)