
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class AssignedDiscount(object):
	def __init__(self, apiContext: ApiContext = None, mozuClient = None):
		self.client = mozuClient or default_client();
		if (apiContext is not None):
			self.client.withApiContext(apiContext);
		else:
			self.client.withApiContext(ApiContext());
	
	def getAssignedDiscounts(self,couponSetCode):
		""" Retrieves the discountIds of any assigned discounts for the specified coupon set.
		
		Args:
			| couponSetCode (string) - The unique identifier of the coupon set.
		
		Returns:
			| array of AssignedDiscount 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/couponsets/{couponSetCode}/assigneddiscounts", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("couponSetCode", couponSetCode);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def assignDiscount(self,assignedDiscount, couponSetCode):
		""" Assigns or associates an existing discount to a specified coupon set. Use the couponSetCode parameter to specify the coupon set.
		
		Args:
			| assignedDiscount(assignedDiscount) - The details of the discount assigned to the coupon set.
			| couponSetCode (string) - The unique identifier of the coupon set.
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/couponsets/{couponSetCode}/assigneddiscounts", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("couponSetCode", couponSetCode);
		self.client.withResourceUrl(url).withBody(assignedDiscount).execute();

	
		
	def unAssignDiscount(self,couponSetCode, discountId):
		""" Unassigns or disassociates the specified discount with the specified coupon set.
		
		Args:
			| couponSetCode (string) - The unique identifier of the coupon set.
			| discountId (int) - discountId parameter description DOCUMENT_HERE 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/couponsets/{couponSetCode}/assigneddiscounts/{discountId}", "DELETE", UrlLocation.TenantPod, False);
		url.formatUrl("couponSetCode", couponSetCode);
		url.formatUrl("discountId", discountId);
		self.client.withResourceUrl(url).execute();

	
	
	