-- Script that displays the average temperature (Fahrenheit)
-- by city ordered by temperature (descending)
SELECT AVG(value) AS temperature
FROM temperatures
ORDER BY value DESC;
