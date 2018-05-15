
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class Adjustment(object):
	def __init__(self, apiContext: ApiContext = None, mozuClient = None):
		self.client = mozuClient or default_client();
		if (apiContext is not None):
			self.client.withApiContext(apiContext);
		else:
			self.client.withApiContext(ApiContext());
	
	def applyHandlingAdjustment(self,adjustment, orderId, updateMode = None, version = None, responseFields = None):
		""" 
		
		Args:
			| adjustment(adjustment) - 
			| orderId (string) - 
			| updateMode (string) - 
			| version (string) - 
			| responseFields (string) - 
		
		Returns:
			| Order 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/orders/{orderId}/adjustment/handling?updatemode={updateMode}&version={version}&responseFields={responseFields}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("orderId", orderId);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("updateMode", updateMode);
		url.formatUrl("version", version);
		self.client.withResourceUrl(url).withBody(adjustment).execute();
		return self.client.result();

	
		
	def applyShippingAdjustment(self,adjustment, orderId, updateMode = None, version = None, responseFields = None):
		""" 
		
		Args:
			| adjustment(adjustment) - Properties of the shipping adjustment to apply to the order.
			| orderId (string) - Unique identifier of the order associated with the shipping adjustment.
			| updateMode (string) - Specifies whether to apply the shipping adjustment by updating the original order, updating the order in draft mode, or updating the order in draft mode and then committing the changes to the original. Draft mode enables users to make incremental order changes before committing the changes to the original order. Valid values are "ApplyToOriginal," "ApplyToDraft," or "ApplyAndCommit."
			| version (string) - 
			| responseFields (string) - 
		
		Returns:
			| Order 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/orders/{orderId}/adjustment/shipping?updatemode={updateMode}&version={version}&responseFields={responseFields}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("orderId", orderId);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("updateMode", updateMode);
		url.formatUrl("version", version);
		self.client.withResourceUrl(url).withBody(adjustment).execute();
		return self.client.result();

	
		
	def applyAdjustment(self,adjustment, orderId, updateMode = None, version = None, responseFields = None):
		""" 
		
		Args:
			| adjustment(adjustment) - Properties of the price adjustment to apply to the order.
			| orderId (string) - Unique identifier of the order for which to apply the adjustment.
			| updateMode (string) - Specifies whether to apply the adjustment by updating the original order, updating the order in draft mode, or updating the order in draft mode and then committing the changes to the original. Draft mode enables users to make incremental order changes before committing the changes to the original order. Valid values are "ApplyToOriginal," "ApplyToDraft," or "ApplyAndCommit."
			| version (string) - 
			| responseFields (string) - 
		
		Returns:
			| Order 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/orders/{orderId}/adjustment?updatemode={updateMode}&version={version}&responseFields={responseFields}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("orderId", orderId);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("updateMode", updateMode);
		url.formatUrl("version", version);
		self.client.withResourceUrl(url).withBody(adjustment).execute();
		return self.client.result();

	
		
	def removeHandlingAdjustment(self,orderId, updateMode = None, version = None):
		""" 
		
		Args:
			| orderId (string) - 
			| updateMode (string) - 
			| version (string) - 
		
		Returns:
			| Order 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/orders/{orderId}/adjustment/handling?updatemode={updateMode}&version={version}", "DELETE", UrlLocation.TenantPod, False);
		url.formatUrl("orderId", orderId);
		url.formatUrl("updateMode", updateMode);
		url.formatUrl("version", version);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def removeShippingAdjustment(self,orderId, updateMode = None, version = None):
		""" 
		
		Args:
			| orderId (string) - Unique identifier of the order with the applied shipping adjustment.
			| updateMode (string) - Specifies whether to remove the shipping adjustment by updating the original order, updating the order in draft mode, or updating the order in draft mode and then commit the changes to the original. Draft mode enables users to make incremental order changes before committing the changes to the original order. Valid values are "ApplyToOriginal," "ApplyToDraft," or "ApplyAndCommit."
			| version (string) - 
		
		Returns:
			| Order 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/orders/{orderId}/adjustment/shipping?updatemode={updateMode}&version={version}", "DELETE", UrlLocation.TenantPod, False);
		url.formatUrl("orderId", orderId);
		url.formatUrl("updateMode", updateMode);
		url.formatUrl("version", version);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def removeAdjustment(self,orderId, updateMode = None, version = None):
		""" 
		
		Args:
			| orderId (string) - Unique identifier of the order for which to delete the adjustment.
			| updateMode (string) - Specifies whether to remove the adjustment by updating the original order, updating the order in draft mode, or updating the order in draft mode and then committing the changes to the original. Draft mode enables users to make incremental order changes before committing the changes to the original order. Valid values are "ApplyToOriginal," "ApplyToDraft," or "ApplyAndCommit."
			| version (string) - 
		
		Returns:
			| Order 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/orders/{orderId}/adjustment?updatemode={updateMode}&version={version}", "DELETE", UrlLocation.TenantPod, False);
		url.formatUrl("orderId", orderId);
		url.formatUrl("updateMode", updateMode);
		url.formatUrl("version", version);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
	
	