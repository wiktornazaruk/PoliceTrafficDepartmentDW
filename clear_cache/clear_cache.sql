-- clear cache 
SELECT * FROM sys.dm_exec_cached_plans 
CROSS APPLY sys.dm_exec_sql_text(plan_handle)
WHERE usecounts > 1
ORDER BY usecounts DESC;

DBCC FREEPROCCACHE