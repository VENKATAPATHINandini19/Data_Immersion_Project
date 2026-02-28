
PRAGMA table_info(sales);
SELECT SUM(Total_Sales) AS Total_Revenue
FROM sales;
SELECT Product,
       SUM(Total_Sales) AS Revenue
FROM sales
GROUP BY Product
ORDER BY Revenue DESC
LIMIT 5;
SELECT Country,
       SUM(Total_Sales) AS Total_Revenue
FROM sales
GROUP BY Country
ORDER BY Total_Revenue DESC;
SELECT strftime('%Y-%m', Order_Date) AS Month,
       SUM(Total_Sales) AS Monthly_Revenue
FROM sales
GROUP BY Month
ORDER BY Month;
SELECT Gender,
       SUM(Total_Sales) AS Revenue
FROM sales
GROUP BY Gender;