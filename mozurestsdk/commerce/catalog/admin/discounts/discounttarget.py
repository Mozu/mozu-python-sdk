
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class DiscountTarget(object):
	def __init__(self, apiContext: ApiContext = None, dataViewMode="Live", mozuClient = None):
		if (apiContext is not None and apiContext.dataViewMode is None):
			apiContext.dataViewMode = dataViewMode;
		else:
			apiContext = ApiContext(dataViewMode = dataViewMode);
		self.client = mozuClient or default_client();
		self.client.withApiContext(apiContext);
	
	def getDiscountTarget(self,discountId, responseFields = None):
		""" 
		
		Args:
			| discountId (int) - discountId parameter description DOCUMENT_HERE 
			| responseFields (string) - Filtering syntax appended to an API call to increase or decrease the amount of data returned inside a JSON object. This parameter should only be used to retrieve data. Attempting to update data using this parameter may cause data loss.
		
		Returns:
			| DiscountTarget 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/discounts/{discountId}/target?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("discountId", discountId);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def updateDiscountTarget(self,discountTarget, discountId, responseFields = None):
		""" 
		
		Args:
			| discountTarget(discountTarget) - Properties of the target to which the discount applies, such as the type of discount and which products, categories, or shipping methods are eligible for the discount and the properties of this discount target.
			| discountId (int) - discountId parameter description DOCUMENT_HERE 
			| responseFields (string) - Filtering syntax appended to an API call to increase or decrease the amount of data returned inside a JSON object. This parameter should only be used to retrieve data. Attempting to update data using this parameter may cause data loss.
		
		Returns:
			| DiscountTarget 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/discounts/{discountId}/target?responseFields={responseFields}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("discountId", discountId);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(discountTarget).execute();
		return self.client.result();

	
	
	