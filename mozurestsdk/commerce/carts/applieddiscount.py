
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
	
	def applyCoupon(self,cartId, couponCode, responseFields = None):
		""" 
		
		Args:
			| cartId (string) - Unique identifier of the cart to which to apply the coupon.
			| couponCode (string) - Code associated with the coupon to apply to the cart.
			| responseFields (string) - 
		
		Returns:
			| Cart 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/carts/{cartId}/coupons/{couponCode}?responseFields={responseFields}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("cartId", cartId);
		url.formatUrl("couponCode", couponCode);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def removeCoupons(self,cartId):
		""" 
		
		Args:
			| cartId (string) - Unique identifier of the cart.
		
		Returns:
			| Cart 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/carts/{cartId}/coupons", "DELETE", UrlLocation.TenantPod, False);
		url.formatUrl("cartId", cartId);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def removeCoupon(self,cartId, couponCode):
		""" 
		
		Args:
			| cartId (string) - Unique identifier of the cart.
			| couponCode (string) - Code associated with the coupon to remove from the cart.
		
		Returns:
			| Cart 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/carts/{cartId}/coupons/{couponcode}", "DELETE", UrlLocation.TenantPod, False);
		url.formatUrl("cartId", cartId);
		url.formatUrl("couponCode", couponCode);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
	
	