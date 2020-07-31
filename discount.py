import webapp2

def calculate_discounted_price(discount_percentage, sales_price, payment, cash_discount_percentage):
    ''' convert Celsius temperature to Fahrenheit temperature '''
    if discount_percentage == "":
        return ""
    try:
        fCost = float(sales_price)
        fPercent = float(discount_percentage)
        fDiscount = fCost * fPercent / 100 # Calculate Discount
        calculated_price = str(fCost - fDiscount) # Calculate discounted price
        if payment == "cash": # Calculate with more disclunt if cash payment option selected
        	fCalculatedPrice = float(calculated_price) 
        	fPercentOnCash = float(cash_discount_percentage)
        	fDiscountOnCash = fCalculatedPrice * fPercentOnCash / 100 # Calculate Discount
        	calculate_price_final = str(fCalculatedPrice - fDiscountOnCash)
        	return str(calculate_price_final)
        else:
        	return str(calculated_price)
    except ValueError:  # user entered non-numeric input
        return "invalid input"

class MainPage(webapp2.RequestHandler):
    def get(self):
        sales_price = self.request.get("sales_price")
        quantity = int(self.request.get("quantity"))
        min_num = int(self.request.get("min_num"))
        max_num = int(self.request.get("max_num"))
        myDict = range(min_num, max_num + 1)
        payment = self.request.get("payment")
        cash_discount_percentage = self.request.get("cash_discount_percentage")
    	if quantity in myDict:
        	discount_percentage = 50
        else:
        	discount_percentage = self.request.get("discount_percentage")	

        calculated_price = calculate_discounted_price(discount_percentage, sales_price, payment, cash_discount_percentage)

        self.response.headers["Content-Type"] = "text/html"
        self.response.write("""
          <html>
            <head><title>Discount Price Calculator</title></head>
            <body>
              <form action="/" method="get">
                Sales Price: <input type="number"
                                        name="sales_price" value={}><br />
                Quantity: <input type="number"
                                        name="quantity" value={}><br />
                Min: <input type="number"
                                        name="min_num" value={}>
                Max: <input type="number"
                                        name="max_num" value={}><br />
                Discount: <input type="text"
                                        name="discount_percentage" value={}><br />
                Discount On Cash: <input type="number"
                                        name="cash_discount_percentage" value={}><br />
              
                <p>Select a payment option:</p>

				<div>
  					<input type="radio" id="credit" name="payment" value="credit">
  					<label for="credit">Credit</label>
				</div>

				<div>
  					<input type="radio" id="cash" name="payment" value="cash">
 					<label for="cash">Cash</label>
				</div>
				<br />
 				<input type="submit" value="Calculate"><br><br />
                
                Price: {}<br />
                Dictionary: {}<br />
                Payment Option: {} <br />
              </form>
            </body>
          </html>""".format(sales_price, quantity, min_num, max_num, discount_percentage, cash_discount_percentage, calculated_price, myDict, payment))

routes = [('/', MainPage)]

my_app = webapp2.WSGIApplication(routes, debug=True)