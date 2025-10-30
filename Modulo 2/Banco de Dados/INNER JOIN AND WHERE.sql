SELECT FirstName, LastName FROM Customer


INNER JOIN Invoice ON Customer.CustomerId = Invoice.CustomerId

WHERE Country = 'Brazil'