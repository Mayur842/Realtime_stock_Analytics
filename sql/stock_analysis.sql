-- Realtime Stock Analytics
-- SQL Analysis Queries

-- 1. View all stock records
SELECT *
FROM reliance_processed;


-- 2. Highest closing price
SELECT MAX(Close) AS Highest_Close
FROM reliance_processed;


-- 3. Lowest closing price
SELECT MIN(Close) AS Lowest_Close
FROM reliance_processed;


-- 4. Average closing price
SELECT AVG(Close) AS Average_Close
FROM reliance_processed;


-- 5. Total trading volume
SELECT SUM(Volume) AS Total_Volume
FROM reliance_processed;


-- 6. Count of anomalies
SELECT COUNT(*) AS Total_Anomalies
FROM reliance_processed
WHERE Combined_Anomaly = 1;


-- 7. Risk level distribution
SELECT Risk_Level, COUNT(*) AS Record_Count
FROM reliance_processed
GROUP BY Risk_Level
ORDER BY Record_Count DESC;


-- 8. High-risk records
SELECT *
FROM reliance_processed
WHERE Risk_Level = 'High Risk';


-- 9. Records with unusual volume
SELECT *
FROM reliance_processed
WHERE Volume_Ratio > 2;


-- 10. Highest volume records
SELECT *
FROM reliance_processed
ORDER BY Volume DESC;