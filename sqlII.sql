USE jsoliman354;
IF EXISTS (
    SELECT * FROM sysobjects WHERE id = object_id(N'AverageCost') 
    AND xtype IN (N'FN', N'IF', N'TF')
)
    DROP FUNCTION AverageCost
GO
CREATE FUNCTION AverageCost (@color VARCHAR(30))
RETURNS TABLE
RETURN
(
	SELECT AVG(P.StandardCost) as 'AverageCost'
	FROM AdventureWorks.Production.Product P
	WHERE P.Color = @color
	)
	

	GO

	SELECT * FROM dbo.AverageCost('Red') 






