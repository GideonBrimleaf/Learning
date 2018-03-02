WITH cte AS 
(SELECT dimUserId
FROM DWInternal.DimUser
WHERE age BETWEEN 25 AND 35 
)

SELECT COUNT(DISTINCT cte.dimUserId) as userCount,
       SUM(debitAmount) as sumOfSpend,
       COUNT(factTransactionId) as transactionCount
FROM DWInternal.FactTransaction
INNER JOIN cte ON 
DWInternal.FactTransaction.dimUserId = cte.dimUserId