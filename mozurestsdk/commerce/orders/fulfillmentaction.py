
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class FulfillmentAction(object):
	def __init__(self, apiContext: ApiContext = None, mozuClient = None):
		self.client = mozuClient or default_client();
		if (apiContext is not None):
			self.client.withApiContext(apiContext);
		else:
			self.client.withApiContext(ApiContext());
	
	def performFulfillmentAction(self,action, orderId, responseFields = None):
		""" Sets the fulfillment action to "Ship" or "PickUp". To ship an order or prepare it for in-store pickup, the order must have a customer name, the "Open" or "OpenAndProcessing" status. To ship the order, it must also have the full shipping address and shipping method. Shipping all packages or picking up all pickups for an order will complete a paid order.
		
		Args:
			| action(action) - Properties of an action to perform when fulfilling an item in an order, whether through in-store pickup or direct shipping.
			| orderId (string) - Unique identifier of the order.
			| responseFields (string) - A list or array of fields returned for a call. These fields may be customized and may be used for various types of data calls in Mozu. For example, responseFields are returned for retrieving or updating attributes, carts, and messages in Mozu.
		
		Returns:
			| Order 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/orders/{orderId}/fulfillment/actions/?responseFields={responseFields}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("orderId", orderId);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(action).execute();
		return self.client.result();

	
		
	def resendPackageFulfillmentEmail(self,action, orderId, responseFields = None):
		""" orders-fulfillment Post ResendPackageFulfillmentEmail description DOCUMENT_HERE 
		
		Args:
			| action(action) - Properties of an action to perform when fulfilling an item in an order, whether through in-store pickup or direct shipping.
			| orderId (string) - Unique identifier of the order.
			| responseFields (string) - A list or array of fields returned for a call. These fields may be customized and may be used for various types of data calls in Mozu. For example, responseFields are returned for retrieving or updating attributes, carts, and messages in Mozu.
		
		Returns:
			| Order 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/orders/{orderId}/fulfillment/email/resend?responseFields={responseFields}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("orderId", orderId);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(action).execute();
		return self.client.result();

	
	
	