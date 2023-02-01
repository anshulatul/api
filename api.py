from flask import Flask,jsonify

app = Flask(__name__)

sales=[
 {
  "InvoiceNo": 536373,
  "StockCode": 20679,
  "Description": "EDWARDIAN PARASOL RED",
  "Quantity": 6,
  "InvoiceDate": 40190.376388888886,
  "UnitPrice": 4.95,
  "CustomerId": 12850,
  "Country": "United Kingdom",
  "EmployeeID": 108
 },
 {
  "InvoiceNo": 536373,
  "StockCode": 37370,
  "Description": "RETRO COFFEE MUGS ASSORTED",
  "Quantity": 6,
  "InvoiceDate": 40190.376388888886,
  "UnitPrice": 1.06,
  "CustomerId": 12850,
  "Country": "United Kingdom",
  "EmployeeID": 108
 },
 {
  "InvoiceNo": 536373,
  "StockCode": 21871,
  "Description": "SAVE THE PLANET MUG",
  "Quantity": 6,
  "InvoiceDate": 40190.376388888886,
  "UnitPrice": 1.06,
  "CustomerId": 12850,
  "Country": "United Kingdom",
  "EmployeeID": 108
 },
 {
  "InvoiceNo": 536373,
  "StockCode": 21071,
  "Description": "VINTAGE BILLBOARD DRINK ME MUG",
  "Quantity": 6,
  "InvoiceDate": 40190.376388888886,
  "UnitPrice": 1.06,
  "CustomerId": 12850,
  "Country": "United Kingdom",
  "EmployeeID": 108
 },
 {
  "InvoiceNo": 536373,
  "StockCode": 21068,
  "Description": "VINTAGE BILLBOARD LOVE\/HATE MUG",
  "Quantity": 6,
  "InvoiceDate": 40190.376388888886,
  "UnitPrice": 1.06,
  "CustomerId": 12850,
  "Country": "United Kingdom",
  "EmployeeID": 108
 },
 {
  "InvoiceNo": 536373,
  "StockCode": 82483,
  "Description": "WOOD 2 DRAWER CABINET WHITE FINISH",
  "Quantity": 2,
  "InvoiceDate": 40190.376388888886,
  "UnitPrice": 4.95,
  "CustomerId": 12850,
  "Country": "United Kingdom",
  "EmployeeID": 108
 },
 {
  "InvoiceNo": 536373,
  "StockCode": 82486,
  "Description": "WOOD S\/3 CABINET ANT WHITE FINISH",
  "Quantity": 4,
  "InvoiceDate": 40190.376388888886,
  "UnitPrice": 6.95,
  "CustomerId": 12850,
  "Country": "United Kingdom",
  "EmployeeID": 108
 },
 {
  "InvoiceNo": 536373,
  "StockCode": 82482,
  "Description": "WOODEN PICTURE FRAME WHITE FINISH",
  "Quantity": 6,
  "InvoiceDate": 40190.376388888886,
  "UnitPrice": 2.1,
  "CustomerId": 12850,
  "Country": "United Kingdom",
  "EmployeeID": 108
 },
 {
  "InvoiceNo": 536373,
  "StockCode": "82494L",
  "Description": "WOODEN FRAME ANTIQUE WHITE ",
  "Quantity": 6,
  "InvoiceDate": 40190.376388888886,
  "UnitPrice": 2.55,
  "CustomerId": 12850,
  "Country": "United Kingdom",
  "EmployeeID": 108
 },
 {
  "InvoiceNo": 536373,
  "StockCode": "84029G",
  "Description": "KNITTED UNION FLAG HOT WATER BOTTLE",
  "Quantity": 6,
  "InvoiceDate": 40190.376388888886,
  "UnitPrice": 3.39,
  "CustomerId": 12850,
  "Country": "United Kingdom",
  "EmployeeID": 108
 },
 {
  "InvoiceNo": 536373,
  "StockCode": "84029E",
  "Description": "RED WOOLLY HOTTIE WHITE HEART.",
  "Quantity": 6,
  "InvoiceDate": 40190.376388888886,
  "UnitPrice": 3.39,
  "CustomerId": 12850,
  "Country": "United Kingdom",
  "EmployeeID": 108
 },
 {
  "InvoiceNo": 536373,
  "StockCode": 22752,
  "Description": "SET 7 BABUSHKA NESTING BOXES",
  "Quantity": 2,
  "InvoiceDate": 40190.376388888886,
  "UnitPrice": 7.65,
  "CustomerId": 12850,
  "Country": "United Kingdom",
  "EmployeeID": 108
 },
 {
  "InvoiceNo": 536373,
  "StockCode": 21730,
  "Description": "GLASS STAR FROSTED T-LIGHT HOLDER",
  "Quantity": 6,
  "InvoiceDate": 40190.376388888886,
  "UnitPrice": 4.25,
  "CustomerId": 12850,
  "Country": "United Kingdom",
  "EmployeeID": 108
 },
 {
  "InvoiceNo": 536374,
  "StockCode": 21258,
  "Description": "VICTORIAN SEWING BOX LARGE",
  "Quantity": 32,
  "InvoiceDate": 40190.38125,
  "UnitPrice": 10.95,
  "CustomerId": 12446,
  "Country": "United Kingdom",
  "EmployeeID": 109
 },
 {
  "InvoiceNo": 536375,
  "StockCode": "85123A",
  "Description": "WHITE HANGING HEART T-LIGHT HOLDER",
  "Quantity": 6,
  "InvoiceDate": 40190.39722222222,
  "UnitPrice": 2.55,
  "CustomerId": 12850,
  "Country": "United Kingdom",
  "EmployeeID": 110
 },
 {
  "InvoiceNo": 536375,
  "StockCode": 71053,
  "Description": "WHITE METAL LANTERN",
  "Quantity": 6,
  "InvoiceDate": 40190.39722222222,
  "UnitPrice": 3.39,
  "CustomerId": 12850,
  "Country": "United Kingdom",
  "EmployeeID": 110
 },
 {
  "InvoiceNo": 536375,
  "StockCode": "84406B",
  "Description": "CREAM CUPID HEARTS COAT HANGER",
  "Quantity": 8,
  "InvoiceDate": 40190.39722222222,
  "UnitPrice": 2.75,
  "CustomerId": 12850,
  "Country": "United Kingdom",
  "EmployeeID": 110
 },
 {
  "InvoiceNo": 536375,
  "StockCode": 20679,
  "Description": "EDWARDIAN PARASOL RED",
  "Quantity": 6,
  "InvoiceDate": 40190.39722222222,
  "UnitPrice": 4.95,
  "CustomerId": 12850,
  "Country": "United Kingdom",
  "EmployeeID": 110
 },
 {
  "InvoiceNo": 536375,
  "StockCode": 37370,
  "Description": "RETRO COFFEE MUGS ASSORTED",
  "Quantity": 6,
  "InvoiceDate": 40190.39722222222,
  "UnitPrice": 1.06,
  "CustomerId": 12850,
  "Country": "United Kingdom",
  "EmployeeID": 110
 },
 {
  "InvoiceNo": 536375,
  "StockCode": 21871,
  "Description": "SAVE THE PLANET MUG",
  "Quantity": 6,
  "InvoiceDate": 40190.39722222222,
  "UnitPrice": 1.06,
  "CustomerId": 12850,
  "Country": "United Kingdom",
  "EmployeeID": 110
 },
 {
  "InvoiceNo": 536375,
  "StockCode": 21071,
  "Description": "VINTAGE BILLBOARD DRINK ME MUG",
  "Quantity": 6,
  "InvoiceDate": 40190.39722222222,
  "UnitPrice": 1.06,
  "CustomerId": 12850,
  "Country": "United Kingdom",
  "EmployeeID": 110
 },
 {
  "InvoiceNo": 536375,
  "StockCode": 21068,
  "Description": "VINTAGE BILLBOARD LOVE\/HATE MUG",
  "Quantity": 6,
  "InvoiceDate": 40190.39722222222,
  "UnitPrice": 1.06,
  "CustomerId": 12850,
  "Country": "United Kingdom",
  "EmployeeID": 110
 },
 {
  "InvoiceNo": 536375,
  "StockCode": 82483,
  "Description": "WOOD 2 DRAWER CABINET WHITE FINISH",
  "Quantity": 2,
  "InvoiceDate": 40190.39722222222,
  "UnitPrice": 4.95,
  "CustomerId": 12850,
  "Country": "United Kingdom",
  "EmployeeID": 110
 },
 {
  "InvoiceNo": 536375,
  "StockCode": 82486,
  "Description": "WOOD S\/3 CABINET ANT WHITE FINISH",
  "Quantity": 4,
  "InvoiceDate": 40190.39722222222,
  "UnitPrice": 6.95,
  "CustomerId": 12850,
  "Country": "United Kingdom",
  "EmployeeID": 110
 },
 {
  "InvoiceNo": 536375,
  "StockCode": 82482,
  "Description": "WOODEN PICTURE FRAME WHITE FINISH",
  "Quantity": 6,
  "InvoiceDate": 40190.39722222222,
  "UnitPrice": 2.1,
  "CustomerId": 12850,
  "Country": "United Kingdom",
  "EmployeeID": 110
 },
 {
  "InvoiceNo": 536375,
  "StockCode": "82494L",
  "Description": "WOODEN FRAME ANTIQUE WHITE ",
  "Quantity": 6,
  "InvoiceDate": 40190.39722222222,
  "UnitPrice": 2.55,
  "CustomerId": 12850,
  "Country": "United Kingdom",
  "EmployeeID": 110
 },
 {
  "InvoiceNo": 536375,
  "StockCode": "84029G",
  "Description": "KNITTED UNION FLAG HOT WATER BOTTLE",
  "Quantity": 6,
  "InvoiceDate": 40190.39722222222,
  "UnitPrice": 3.39,
  "CustomerId": 12850,
  "Country": "United Kingdom",
  "EmployeeID": 110
 },
 {
  "InvoiceNo": 536375,
  "StockCode": "84029E",
  "Description": "RED WOOLLY HOTTIE WHITE HEART.",
  "Quantity": 6,
  "InvoiceDate": 40190.39722222222,
  "UnitPrice": 3.39,
  "CustomerId": 12850,
  "Country": "United Kingdom",
  "EmployeeID": 110
 },
 {
  "InvoiceNo": 536375,
  "StockCode": 22752,
  "Description": "SET 7 BABUSHKA NESTING BOXES",
  "Quantity": 2,
  "InvoiceDate": 40190.39722222222,
  "UnitPrice": 7.65,
  "CustomerId": 12850,
  "Country": "United Kingdom",
  "EmployeeID": 110
 }
]

@app.route('/')

def index():
    return "Welcome to my API ."

@app.route("/sales",methods=['GET'])
def get():
    return jsonify({'sales':sales})
@app.route("/sales/<int:Quantity>",methods=['GET'])
def gets():
    return jsonify({'Quantity':sales})

if __name__ =="__main__":
    app.run(debug=True)