
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class OrderAttribute(object):
	def __init__(self, apiContext: ApiContext = None, mozuClient = None):
		self.client = mozuClient or default_client();
		if (apiContext is not None):
			self.client.withApiContext(apiContext);
		else:
			self.client.withApiContext(ApiContext());
	
	def getCheckoutAttributes(self,checkoutId):
		""" 
		
		Args:
			| checkoutId (string) - 
		
		Returns:
			| array of OrderAttribute 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/checkouts/{checkoutId}/attributes", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("checkoutId", checkoutId);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def createCheckoutAttributes(self,checkoutAttributes, checkoutId):
		""" 
		
		Args:
			| checkoutAttributes(array|checkoutAttributes) - 
			| checkoutId (string) - 
		
		Returns:
			| array of OrderAttribute 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/checkouts/{checkoutId}/attributes", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("checkoutId", checkoutId);
		self.client.withResourceUrl(url).withBody(checkoutAttributes).execute();
		return self.client.result();

	
		
	def updateCheckoutAttribute(self,checkoutAttributes, checkoutId, removeMissing = False):
		""" 
		
		Args:
			| checkoutAttributes(array|checkoutAttributes) - 
			| checkoutId (string) - 
			| removeMissing (bool) - 
		
		Returns:
			| array of OrderAttribute 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/checkouts/{checkoutId}/attributes?removeMissing={removeMissing}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("checkoutId", checkoutId);
		url.formatUrl("removeMissing", removeMissing);
		self.client.withResourceUrl(url).withBody(checkoutAttributes).execute();
		return self.client.result();

	
	
	