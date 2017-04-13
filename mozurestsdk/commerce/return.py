
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class Return(object):
	def __init__(self, apiContext: ApiContext = None, mozuClient = None):
		self.client = mozuClient or default_client();
		if (apiContext is not None):
			self.client.withApiContext(apiContext);
		else:
			self.client.withApiContext(ApiContext());
	
	def getReturns(self,startIndex = None, pageSize = None, sortBy = None, filter = None, q = None, responseFields = None):
		""" Retrieves a list of all returns according to any filter and sort criteria.
		
		Args:
			| startIndex (int) - When creating paged results from a query, this value indicates the zero-based offset in the complete result set where the returned entities begin. For example, with a PageSize of 25, to get the 51st through the 75th items, use startIndex=3.
			| pageSize (int) - The number of results to display on each page when creating paged results from a query. The maximum value is 200.
			| sortBy (string) - The property by which to sort results and whether the results appear in ascending (a-z) order, represented by ASC or in descending (z-a) order, represented by DESC. The sortBy parameter follows an available property. For example: "sortBy=productCode+asc"
			| filter (string) - A set of expressions that consist of a field, operator, and value and represent search parameter syntax when filtering results of a query. Valid operators include equals (eq), does not equal (ne), greater than (gt), less than (lt), greater than or equal to (ge), less than or equal to (le), starts with (sw), or contains (cont). For example - "filter=IsDisplayed+eq+true"
			| q (string) - A list of order search terms (not phrases) to use in the query when searching across order number and the name or email of the billing contact. When entering, separate multiple search terms with a space character.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| ReturnCollection 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/returns/?startIndex={startIndex}&pageSize={pageSize}&sortBy={sortBy}&filter={filter}&q={q}&responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("filter", filter);
		url.formatUrl("pageSize", pageSize);
		url.formatUrl("q", q);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("sortBy", sortBy);
		url.formatUrl("startIndex", startIndex);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getAvailableReturnActions(self,returnId):
		""" Retrieves a list of the actions available to perform for the specified return based on its current state.
		
		Args:
			| returnId (string) - Unique identifier of the return whose items you want to get.
		
		Returns:
			| array of string 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/returns/{returnId}/actions", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("returnId", returnId);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getReturnItem(self,returnId, returnItemId, responseFields = None):
		""" Retrieves the details of a single return item.
		
		Args:
			| returnId (string) - Unique identifier of the return whose items you want to get.
			| returnItemId (string) - Unique identifier of the return item whose details you want to get.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| ReturnItem 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/returns/{returnId}/items/{returnItemId}?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("returnId", returnId);
		url.formatUrl("returnItemId", returnItemId);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getReturnItems(self,returnId, responseFields = None):
		""" Retrieves the details of all return items in an order.
		
		Args:
			| returnId (string) - Unique identifier of the return whose items you want to get.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| ReturnItemCollection 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/returns/{returnId}/items?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("returnId", returnId);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getAvailablePaymentActionsForReturn(self,returnId, paymentId):
		""" Retrieves a list of the payment actions available to perform for the specified return when a return results in a refund to the customer.
		
		Args:
			| returnId (string) - Unique identifier of the return whose items you want to get.
			| paymentId (string) - Unique identifier of the payment for which to perform the action.
		
		Returns:
			| array of string 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/returns/{returnId}/payments/{paymentId}/actions", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("paymentId", paymentId);
		url.formatUrl("returnId", returnId);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getPayment(self,returnId, paymentId, responseFields = None):
		""" Retrieves the details of a payment submitted as part of a refund associated with a customer return.
		
		Args:
			| returnId (string) - Unique identifier of the return whose items you want to get.
			| paymentId (string) - Unique identifier of the payment for which to perform the action.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| Payment 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/returns/{returnId}/payments/{paymentId}?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("paymentId", paymentId);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("returnId", returnId);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getPayments(self,returnId, responseFields = None):
		""" Retrieves a list of all payments submitted as part of a refund associated with a customer return.
		
		Args:
			| returnId (string) - Unique identifier of the return whose items you want to get.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| PaymentCollection 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/returns/{returnId}/payments?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("returnId", returnId);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getReturn(self,returnId, responseFields = None):
		""" Retrieves a list of properties for the specified return.
		
		Args:
			| returnId (string) - Unique identifier of the return whose items you want to get.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| Return 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/returns/{returnId}?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("returnId", returnId);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getReasons(self,responseFields = None):
		""" Returns a list of reasons for a return.
		
		Args:
			| responseFields (string) - Filtering syntax appended to an API call to increase or decrease the amount of data returned inside a JSON object. This parameter should only be used to retrieve data. Attempting to update data using this parameter may cause data loss.
		
		Returns:
			| ReasonCollection 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/returns/reasons?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def createReturn(self,ret, responseFields = None):
		""" Creates a return for previously fulfilled items. Each return must either be associated with an original order or a product definition to represent each returned item.When you create a return, you must specify the following fields:
* 

* 
* 

*  (Optional, but recommended)

* 
* 

* 


*  (required for bundle items or product extras, but null for parent product or bundles)
* 

* 


*  (required for product extras, but otherwise null)

*  (set to  to target parent products or bundles without extras)


		
		Args:
			| ret(ret) - Properties of a return of one or more previously fulfilled items.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| Return 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/returns/?responseFields={responseFields}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(ret).execute();
		return self.client.result();

	
		
	def createReturnItem(self,returnItem, returnId, responseFields = None):
		""" Adds a return item to the return.
		
		Args:
			| returnItem(returnItem) - Properties of a previously fulfilled item associated with a return.
			| returnId (string) - Unique identifier of the return whose items you want to get.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| Return 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/returns/{returnId}/items?responseFields={responseFields}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("returnId", returnId);
		self.client.withResourceUrl(url).withBody(returnItem).execute();
		return self.client.result();

	
		
	def performPaymentActionForReturn(self,action, returnId, paymentId, responseFields = None):
		""" Updates a refund payment associated with a customer return by performing the specified action.
		
		Args:
			| action(action) - Properties of the payment action performed for an order.
			| returnId (string) - Unique identifier of the return whose items you want to get.
			| paymentId (string) - Unique identifier of the payment for which to perform the action.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| Return 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/returns/{returnId}/payments/{paymentId}/actions?responseFields={responseFields}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("paymentId", paymentId);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("returnId", returnId);
		self.client.withResourceUrl(url).withBody(action).execute();
		return self.client.result();

	
		
	def createPaymentActionForReturn(self,action, returnId, responseFields = None):
		""" Creates a new payment for a return that results in a refund to the customer.
		
		Args:
			| action(action) - Properties of the payment action performed for an order.
			| returnId (string) - Unique identifier of the return whose items you want to get.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| Return 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/returns/{returnId}/payments/actions?responseFields={responseFields}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("returnId", returnId);
		self.client.withResourceUrl(url).withBody(action).execute();
		return self.client.result();

	
		
	def createReturnShippingOrder(self,itemQuantities, returnId, responseFields = None):
		""" Creates a replacement order for the return.
		
		Args:
			| itemQuantities(array|itemQuantities) - 
			| returnId (string) - Unique identifier of the return whose items you want to get.
			| responseFields (string) - Filtering syntax appended to an API call to increase or decrease the amount of data returned inside a JSON object. This parameter should only be used to retrieve data. Attempting to update data using this parameter may cause data loss.
		
		Returns:
			| Order 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/returns/{returnId}/ship?responseFields={responseFields}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("returnId", returnId);
		self.client.withResourceUrl(url).withBody(itemQuantities).execute();
		return self.client.result();

	
		
	def performReturnActions(self,action, responseFields = None):
		""" Updates the return by performing the action specified in the request.
		
		Args:
			| action(action) - Properties of an action a user can perform for a return.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| ReturnCollection 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/returns/actions?responseFields={responseFields}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(action).execute();
		return self.client.result();

	
		
	def updateReturn(self,ret, returnId, responseFields = None):
		""" Updates one or more properties of a return for items previously shipped in a completed order.
		
		Args:
			| ret(ret) - Properties of a return of one or more previously fulfilled items.
			| returnId (string) - Unique identifier of the return whose items you want to get.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| Return 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/returns/{returnId}?responseFields={responseFields}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("returnId", returnId);
		self.client.withResourceUrl(url).withBody(ret).execute();
		return self.client.result();

	
		
	def resendReturnEmail(self,action):
		""" Resend the email notification to a shopper that a return has been created.
		
		Args:
			| action(action) - Properties of an action a user can perform for a return.
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/returns/email/resend", "PUT", UrlLocation.TenantPod, False);
		self.client.withResourceUrl(url).withBody(action).execute();

	
		
	def deleteOrderItem(self,returnId, returnItemId):
		""" Removes a particular order item from the order of the current shopper.
		
		Args:
			| returnId (string) - Unique identifier of the return whose items you want to get.
			| returnItemId (string) - Unique identifier of the return item whose details you want to get.
		
		Returns:
			| Return 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/returns/{orderId}/items/{orderItemId}?updatemode={updateMode}&version={version}", "DELETE", UrlLocation.TenantPod, False);
		url.formatUrl("returnId", returnId);
		url.formatUrl("returnItemId", returnItemId);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def deleteReturn(self,returnId):
		""" Deletes the return specified in the request.
		
		Args:
			| returnId (string) - Unique identifier of the return whose items you want to get.
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/returns/{returnId}", "DELETE", UrlLocation.TenantPod, False);
		url.formatUrl("returnId", returnId);
		self.client.withResourceUrl(url).execute();

	
	
	