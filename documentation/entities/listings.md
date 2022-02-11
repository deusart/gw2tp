# Listings
Current buy and sell listings for items from the trading post. 

## Wiki Link
https://wiki.guildwars2.com/wiki/API:2/commerce/listings

## Fields:  
- **id** (number) – The item id.  
- **buys** (array) – A list of all buy listings, ascending from lowest buy order. Each listing object has the following properties:  
  - listings (number) – The number of individual listings this object refers to (e.g. two players selling at the same price will end up in the same listing)  
  - unit_price (number) – The sell offer or buy order price in coins.  
  - quantity (number) – The amount of items being sold/bought in this listing.

- **sells** (array) – A list of all sell listings, ascending from lowest sell offer. Each listing object has the following properties:  
  - listings (number) – The number of individual listings this object refers to (e.g. two players selling at the same price will end up in the same listing)  
  - unit_price (number) – The sell offer or buy order price in coins.  
  - quantity (number) – The amount of items being sold/bought in this listing.

## Staging data
- **id** (bigint)
- **type** (nvarchar(4)) Possible values:  
  - buy
  - sell

- **listings** (bigint)
- **unit_price** (bigint)
- **quantity** (bigint)
- **hash_diff** (binary(16))
- **created_at** (datetime)

## Web API Request example
**One Item request (GET):**  
```
https://api.guildwars2.com/v2/commerce/listings/19684
```
**Response example**
```
{
  "id": 19684,
  "buys": [
    { "listings":  23, "unit_price":   1, "quantity": 1962 },
    { "listings":   1, "unit_price":   5, "quantity":   45 },
    { "listings": 105, "unit_price":   9, "quantity": 7033 },
    …
  ],
  "sells": [
    { "listings":   1, "unit_price":  99, "quantity":   211 },
    { "listings":   5, "unit_price": 100, "quantity":   699 },
    { "listings":  74, "unit_price": 101, "quantity": 17746 },
    …
  ]
}
```

**Multiply Item request (GET):**  
```
https://api.guildwars2.com/v2/commerce/listings?ids=19684,19709
```
**Response example**
```
[
  {
    "id": 19709,
    "buys": [
      { "listings":  9, "unit_price":  1, "quantity":  335 },
      { "listings": 81, "unit_price":  8, "quantity": 3092 },
      …
    ],
    "sells": [
      { "listings":  2, "unit_price": 63, "quantity":  499 },
      { "listings":  3, "unit_price": 64, "quantity":  289 },
      …
    ]
  },
  {
    "id": 19684,
    "buys": [
      { "listings": 23, "unit_price":  1, "quantity": 1962 },
      { "listings":  1, "unit_price":  5, "quantity":   45 },
      …
    ],
    "sells": [
      { "listings":  4, "unit_price": 98, "quantity":  951 },
      { "listings":  1, "unit_price": 99, "quantity":  211 },
      …
    ]
  }
]
```

**List of listed items (GET):**  
```
https://api.guildwars2.com/v2/commerce/listings
```
**Response example**
```
[
  24,
  68,
  69,
  70,
  …
]
```