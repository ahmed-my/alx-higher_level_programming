-- Script that displays the average temperature (Fahrenheit)
-- by city ordered by temperature (descending)
SELECT AVG(value)
FROM temperatures
ORDER BY value DESC;
