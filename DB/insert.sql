USE Police
GO
BULK INSERT Criminal FROM 'data\criminal_data.csv' WITH (FIELDTERMINATOR='|', ROWTERMINATOR = '\n');
BULK INSERT Ticket FROM 'data\ticket_data.csv' WITH (FIELDTERMINATOR='|', ROWTERMINATOR = '\n');
BULK INSERT Officer FROM 'data\officer_data.csv' WITH (FIELDTERMINATOR='|', ROWTERMINATOR = '\n');
BULK INSERT RatingOfService FROM 'data\rating_data.csv' WITH (FIELDTERMINATOR='|', ROWTERMINATOR = '\n');

BULK INSERT Criminal FROM 'data\criminal_dataT2.csv' WITH (FIELDTERMINATOR='|', ROWTERMINATOR = '\n');
BULK INSERT Ticket FROM 'data\ticket_dataT2.csv' WITH (FIELDTERMINATOR='|', ROWTERMINATOR = '\n');
BULK INSERT Officer FROM 'data\officer_dataT2.csv' WITH (FIELDTERMINATOR='|', ROWTERMINATOR = '\n');
BULK INSERT RatingOfService FROM 'data\rating_dataT2.csv' WITH (FIELDTERMINATOR='|', ROWTERMINATOR = '\n');

