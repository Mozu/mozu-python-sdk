
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
		""" Applies a defined coupon to the cart specified in the request.
		
		Args:
			| cartId (string) - Identifier of the cart to delete.
			| couponCode (string) - Code associated with the coupon to remove from the cart.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
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
		""" Removes all coupons from the cart specified in the request.
		
		Args:
			| cartId (string) - Identifier of the cart to delete.
		
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
		""" Removes an applied coupon from the cart specified in the request.
		
		Args:
			| cartId (string) - Identifier of the cart to delete.
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

	
	
	