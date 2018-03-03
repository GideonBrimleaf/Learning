WITH cte AS 
(SELECT dimUserId
FROM DWInternal.DimUser
WHERE age BETWEEN 25 AND 35 
)

SELECT calendarYearMonth,
       COUNT(DISTINCT cte.dimUserId) as userCount,
       SUM(debitAmount) as sumOfSpend,
       COUNT(factTransactionId) as transactionCount
FROM DWInternal.FactTransaction
INNER JOIN cte ON 
DWInternal.FactTransaction.dimUserId = cte.dimUserId
INNER JOIN DWInternal.DimDate
ON DWInternal.DimDate.dimDateId = 
DWInternal.FactTransaction.dimTransactionDateId
WHERE calendarYearMonth > '201708'
GROUP BY calendarYearMonth
ORDER BY calendarYearMonth