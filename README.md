# tescolabsapi
An unofficial Python client for querying products with Tesco Labs API.

Work in progress - no error handling, API not stable.

Example::

    >>> import tescolabsapi
    >>> t = tescolabsapi.TescoLabsApi(tescolabsapi.API_URL,
    ...                               '<your developer key>', 
    ...                               '<your application key>')
    >>> r = t.productsearch('cornflakes')
    >>> print r.content
    {
    "StatusCode": 0,
    "StatusInfo": "Command Processed OK",
    "PageNumber": 1,
    "TotalPageCount": 2,
    "TotalProductCount": 22,
    "PageProductCount": 20,
    "Products":
    [
    {
    "BaseProductId": "50342861",
    "EANBarcode": "5000127013094",
    "CheaperAlternativeProductId": "",
    "HealthierAlternativeProductId": "",
    "ImagePath": "http://img.tesco.com/Groceries/pi/094/5000127013094/IDShot_90x90.jpg",
    "MaximumPurchaseQuantity": 99,
    "Name": "Kelloggs Cornflakes 750G",
    "OfferPromotion": "",
    "OfferValidity": "",
    "OfferLabelImagePath": "",
    "ShelfCategory": "",
    "ShelfCategoryName": "",
    "Price": 1.98,
    "PriceDescription": "£1.98 each",
    "ProductId": "254852397",
    "ProductType": "QuantityOnlyProduct",
    "UnitPrice": 0.264,
    "UnitType": "100g"
    },
    ...
    ]
    }

To register for a developer key and an application key vist https://secure.techfortesco.com/tescoapiweb/Login.aspx. For documentation of the underlying API visit https://secure.techfortesco.com/tescoapiweb/wiki/index.html.

Neither this project nor it's author are associated with Tesco PLC. YMMV

