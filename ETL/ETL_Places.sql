use TrafficDepartmentDW
go

DECLARE @json NVARCHAR(MAX);

SELECT @json = BulkColumn
FROM OPENROWSET(
    BULK 'gdansk_districts.json',
    SINGLE_CLOB -- Read the file as a single string
) AS j;

INSERT INTO Place (Street, District)
SELECT 
    street AS Street,
    district AS District
FROM OPENJSON(@json, '$.districts')
WITH (
    district NVARCHAR(50) '$.name',
    streets NVARCHAR(MAX) '$.streets' AS JSON -- Extract the streets array as JSON
) AS districts
CROSS APPLY OPENJSON(districts.streets)
WITH (
    street NVARCHAR(100) '$' -- Extract each street name
) AS streets;