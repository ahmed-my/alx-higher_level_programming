-- Script that displays the average temperature (Fahrenheit)
-- by city ordered by temperature (descending)
SELECT city, AVG(value) AS temperature
FROM temperatures
GROUP BY city
ORDER BY temperature DESC;
