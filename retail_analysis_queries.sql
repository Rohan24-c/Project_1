
-- 1. Add Total Sales Column
SELECT *, Quantity * UnitPrice AS TotalSales
FROM retail_data
LIMIT 10;

-- 2. Profit by Product Description
SELECT Description, 
       SUM(Quantity * UnitPrice) AS TotalRevenue
FROM retail_data
GROUP BY Description
ORDER BY TotalRevenue DESC
LIMIT 10;

-- 3. Profit by Country
SELECT Country,
       SUM(Quantity * UnitPrice) AS Revenue
FROM retail_data
GROUP BY Country
ORDER BY Revenue DESC;

-- 4. Monthly Sales Trends
SELECT SUBSTR(InvoiceDate, 1, 7) AS Month,
       SUM(Quantity * UnitPrice) AS Revenue
FROM retail_data
GROUP BY Month
ORDER BY Month;

-- 5. Most Frequently Bought Products
SELECT Description, SUM(Quantity) AS TotalQuantity
FROM retail_data
GROUP BY Description
ORDER BY TotalQuantity DESC
LIMIT 10;

-- 6. Average Order Value
SELECT AVG(Quantity * UnitPrice) AS AvgOrderValue
FROM retail_data;
