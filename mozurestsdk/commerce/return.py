
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
		client.withApiContext(apiContext);
	
	def getReturns(self,startIndex = None, pageSize = None, sortBy = None, filter = None, responseFields = None):
		"""
			Retrieves a list of all returns according to any filter and sort criteria.
			Request Params
				string filter A set of expressions that consist of a field, operator, and value and represent search parameter syntax when filtering results of a query. Valid operators include equals (eq), does not equal (ne), greater than (gt), less than (lt), greater than or equal to (ge), less than or equal to (le), starts with (sw), or contains (cont). For example - "filter=IsDisplayed+eq+true"
				int pageSize The number of results to display on each page when creating paged results from a query. The maximum value is 200.
				string responseFields Use this field to include those fields which are not included by default.
				string sortBy The property by which to sort results and whether the results appear in ascending (a-z) order, represented by ASC or in descending (z-a) order, represented by DESC. The sortBy parameter follows an available property. For example: "sortBy=productCode+asc"
				int startIndex When creating paged results from a query, this value indicates the zero-based offset in the complete result set where the returned entities begin. For example, with a PageSize of 25, to get the 51st through the 75th items, use startIndex=3.
			Response
				ReturnCollection 
		"""

		url = MozuUrl("/api/commerce/returns/?startIndex={startIndex}&pageSize={pageSize}&sortBy={sortBy}&filter={filter}&responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("filter", filter);
		url.formatUrl("pageSize", pageSize);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("sortBy", sortBy);
		url.formatUrl("startIndex", startIndex);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getAvailableReturnActions(self,returnId):
		"""
			Retrieves a list of the actions available to perform for the specified return based on its current state.
			Request Params
				string returnId Unique identifier of the return whose items you want to get.
			Response
				array|string 
		"""

		url = MozuUrl("/api/commerce/returns/{returnId}/actions", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("returnId", returnId);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getReturnItem(self,returnId, returnItemId, responseFields = None):
		"""
			Retrieves the details of a single return item.
			Request Params
				string responseFields Use this field to include those fields which are not included by default.
				string returnId Unique identifier of the return whose items you want to get.
				string returnItemId Unique identifier of the return item whose details you want to get.
			Response
				ReturnItem 
		"""

		url = MozuUrl("/api/commerce/returns/{returnId}/items/{returnItemId}?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("returnId", returnId);
		url.formatUrl("returnItemId", returnItemId);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getReturnItems(self,returnId, responseFields = None):
		"""
			Retrieves the details of all return items in an order.
			Request Params
				string responseFields Use this field to include those fields which are not included by default.
				string returnId Unique identifier of the return whose items you want to get.
			Response
				ReturnItemCollection 
		"""

		url = MozuUrl("/api/commerce/returns/{returnId}/items?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("returnId", returnId);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getAvailablePaymentActionsForReturn(self,returnId, paymentId):
		"""
			Retrieves a list of the payment actions available to perform for the specified return when a return results in a refund to the customer.
			Request Params
				string paymentId Unique identifier of the payment for which to perform the action.
				string returnId Unique identifier of the return whose items you want to get.
			Response
				array|string 
		"""

		url = MozuUrl("/api/commerce/returns/{returnId}/payments/{paymentId}/actions", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("paymentId", paymentId);
		url.formatUrl("returnId", returnId);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getPayment(self,returnId, paymentId, responseFields = None):
		"""
			Retrieves the details of a payment submitted as part of a refund associated with a customer return.
			Request Params
				string paymentId Unique identifier of the payment for which to perform the action.
				string responseFields Use this field to include those fields which are not included by default.
				string returnId Unique identifier of the return whose items you want to get.
			Response
				Payment 
		"""

		url = MozuUrl("/api/commerce/returns/{returnId}/payments/{paymentId}?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("paymentId", paymentId);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("returnId", returnId);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getPayments(self,returnId, responseFields = None):
		"""
			Retrieves a list of all payments submitted as part of a refund associated with a customer return.
			Request Params
				string responseFields Use this field to include those fields which are not included by default.
				string returnId Unique identifier of the return whose items you want to get.
			Response
				PaymentCollection 
		"""

		url = MozuUrl("/api/commerce/returns/{returnId}/payments?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("returnId", returnId);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getReturn(self,returnId, responseFields = None):
		"""
			Retrieves a list of properties for the specified return.
			Request Params
				string responseFields Use this field to include those fields which are not included by default.
				string returnId Unique identifier of the return whose items you want to get.
			Response
				Return 
		"""

		url = MozuUrl("/api/commerce/returns/{returnId}?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("returnId", returnId);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def createReturn(self,ret, responseFields = None):
		"""
			Creates a return for previously fulfilled items. Each return must either be associated with an original order or a product definition to represent each returned item.
			Request Params
				string responseFields Use this field to include those fields which are not included by default.
				ret Properties of a return of one or more previously fulfilled items.
			Response
				Return 
		"""

		url = MozuUrl("/api/commerce/returns/?responseFields={responseFields}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def createReturnItem(self,returnItem, returnId, responseFields = None):
		"""
			Adds a return item to the return.
			Request Params
				string responseFields Use this field to include those fields which are not included by default.
				string returnId Unique identifier of the return whose items you want to get.
				returnItem Properties of a previously fulfilled item associated with a return.
			Response
				Return 
		"""

		url = MozuUrl("/api/commerce/returns/{returnId}/items?responseFields={responseFields}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("returnId", returnId);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def performPaymentActionForReturn(self,action, returnId, paymentId, responseFields = None):
		"""
			Updates a refund payment associated with a customer return by performing the specified action.
			Request Params
				string paymentId Unique identifier of the payment for which to perform the action.
				string responseFields Use this field to include those fields which are not included by default.
				string returnId Unique identifier of the return whose items you want to get.
				action Properties of the payment action performed for an order.
			Response
				Return 
		"""

		url = MozuUrl("/api/commerce/returns/{returnId}/payments/{paymentId}/actions?responseFields={responseFields}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("paymentId", paymentId);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("returnId", returnId);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def createPaymentActionForReturn(self,action, returnId, responseFields = None):
		"""
			Creates a new payment for a return that results in a refund to the customer.
			Request Params
				string responseFields Use this field to include those fields which are not included by default.
				string returnId Unique identifier of the return whose items you want to get.
				action Properties of the payment action performed for an order.
			Response
				Return 
		"""

		url = MozuUrl("/api/commerce/returns/{returnId}/payments/actions?responseFields={responseFields}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("returnId", returnId);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def performReturnActions(self,action, responseFields = None):
		"""
			Updates the return by performing the action specified in the request.
			Request Params
				string responseFields Use this field to include those fields which are not included by default.
				action Properties of an action a user can perform for a return.
			Response
				ReturnCollection 
		"""

		url = MozuUrl("/api/commerce/returns/actions?responseFields={responseFields}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def updateReturn(self,ret, returnId, responseFields = None):
		"""
			Updates one or more properties of a return for items previously shipped in a completed order.
			Request Params
				string responseFields Use this field to include those fields which are not included by default.
				string returnId Unique identifier of the return whose items you want to get.
				ret Properties of a return of one or more previously fulfilled items.
			Response
				Return 
		"""

		url = MozuUrl("/api/commerce/returns/{returnId}?responseFields={responseFields}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("returnId", returnId);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def resendReturnEmail(self,action):
		"""
			commerce-returns Put ResendReturnEmail description DOCUMENT_HERE 
			Request Params
				action Properties of an action a user can perform for a return.
			Response
		"""

		url = MozuUrl("/api/commerce/returns/email/resend", "PUT", UrlLocation.TenantPod, False);
		self.client.withResourceUrl(url).execute();

	
		
	def deleteOrderItem(self,returnId, returnItemId):
		"""
			Removes a particular order item from the order of the current shopper.
			Request Params
				string returnId Unique identifier of the return whose items you want to get.
				string returnItemId Unique identifier of the return item whose details you want to get.
			Response
				Return 
		"""

		url = MozuUrl("/api/commerce/returns/{orderId}/items/{orderItemId}?updatemode={updateMode}&version={version}", "DELETE", UrlLocation.TenantPod, False);
		url.formatUrl("returnId", returnId);
		url.formatUrl("returnItemId", returnItemId);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def deleteReturn(self,returnId):
		"""
			Deletes the return specified in the request.
			Request Params
				string returnId Unique identifier of the return whose items you want to get.
			Response
		"""

		url = MozuUrl("/api/commerce/returns/{returnId}", "DELETE", UrlLocation.TenantPod, False);
		url.formatUrl("returnId", returnId);
		self.client.withResourceUrl(url).execute();

	
	
	