
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class OrderReturnableItem(object):
	def __init__(self, apiContext: ApiContext = None, mozuClient = None):
		self.client = mozuClient or default_client();
		if (apiContext is not None):
			self.client.withApiContext(apiContext);
		else:
			self.client.withApiContext(ApiContext());
	
	def getOrderReturnableItems(self,orderId, responseFields = None):
		""" Retrieves information about which items are eligible for return on an order.Each item displays the following information:
* One entry that represents the entire order item, whether this is a single product, a bundle, or a product or bundle with extras. (ParentProductCode == null, ExcludeProductExtras == false)

* (If the item contains product extras) 
* One entry that represents the parent product without product extras (ParentProductCode == null, ExcludeProductExtras == true)

* One entry for each extra (ParentProductCode != null, OrderItemOptionAttributeFQN != null)


* (If the parent item is a bundle)
* One entry for each item within the bundle (ParentProductCode != null, OrderItemOptionAttributeFQN == null)


		
		Args:
			| orderId (string) - Unique identifier of the order.
			| responseFields (string) - Filtering syntax appended to an API call to increase or decrease the amount of data returned inside a JSON object. This parameter should only be used to retrieve data. Attempting to update data using this parameter may cause data loss.
		
		Returns:
			| OrderReturnableItemCollection 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/orders/{orderId}/returnableitems?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("orderId", orderId);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
	
	