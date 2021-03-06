
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class Refund(object):
	def __init__(self, apiContext: ApiContext = None, mozuClient = None):
		self.client = mozuClient or default_client();
		if (apiContext is not None):
			self.client.withApiContext(apiContext);
		else:
			self.client.withApiContext(ApiContext());
	
	def createRefund(self,refund, orderId, responseFields = None):
		""" Creates a refund based on the information supplied in the request.  
		
		Args:
			| refund(refund) - The details of the refund.
			| orderId (string) - Unique identifier of the order.
			| responseFields (string) - Filtering syntax appended to an API call to increase or decrease the amount of data returned inside a JSON object. This parameter should only be used to retrieve data. Attempting to update data using this parameter may cause data loss.
		
		Returns:
			| Refund 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/orders/{orderId}/refunds?responseFields={responseFields}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("orderId", orderId);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(refund).execute();
		return self.client.result();

	
		
	def resendRefundEmail(self,orderId, refundId):
		""" Resends the order refund email previously sent to the shopper. 
		
		Args:
			| orderId (string) - Unique identifier of the order.
			| refundId (string) - Unique ID of the refund.
        
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/orders/{orderId}/refunds/{refundId}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("orderId", orderId);
		url.formatUrl("refundId", refundId);
		self.client.withResourceUrl(url).execute();

	
	
	