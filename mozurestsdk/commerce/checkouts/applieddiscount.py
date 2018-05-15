
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class AppliedDiscount(object):
	def __init__(self, apiContext: ApiContext = None, mozuClient = None):
		self.client = mozuClient or default_client();
		if (apiContext is not None):
			self.client.withApiContext(apiContext);
		else:
			self.client.withApiContext(ApiContext());
	
	def applyCoupon(self,checkoutId, couponCode, responseFields = None):
		""" 
		
		Args:
			| checkoutId (string) - 
			| couponCode (string) - 
			| responseFields (string) - 
		
		Returns:
			| Checkout 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/checkouts/{checkoutId}/coupons/{couponCode}?responseFields={responseFields}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("checkoutId", checkoutId);
		url.formatUrl("couponCode", couponCode);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def removeCoupons(self,checkoutId):
		""" 
		
		Args:
			| checkoutId (string) - 
		
		Returns:
			| Checkout 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/checkouts/{checkoutId}/coupons", "DELETE", UrlLocation.TenantPod, False);
		url.formatUrl("checkoutId", checkoutId);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def removeCoupon(self,checkoutId, couponCode):
		""" 
		
		Args:
			| checkoutId (string) - 
			| couponCode (string) - 
		
		Returns:
			| Checkout 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/checkouts/{checkoutId}/coupons/{couponcode}", "DELETE", UrlLocation.TenantPod, False);
		url.formatUrl("checkoutId", checkoutId);
		url.formatUrl("couponCode", couponCode);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
	
	