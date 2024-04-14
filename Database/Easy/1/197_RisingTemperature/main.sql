SELECT W1.id
FROM Weather AS W1, Weather AS W2
WHERE W1.recordDate - INTERVAL'1 day' = W2.recordDate AND W1.temperature > W2.temperature