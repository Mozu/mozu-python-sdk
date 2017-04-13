
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class PriceList(object):
	def __init__(self, apiContext: ApiContext = None, mozuClient = None):
		self.client = mozuClient or default_client();
		if (apiContext is not None):
			self.client.withApiContext(apiContext);
		else:
			self.client.withApiContext(ApiContext());
	
	def getPriceList(self,priceListCode, responseFields = None):
		""" Retrieves the details of the specified price list.
		
		Args:
			| priceListCode (string) - The unique code of the price list for which you want to retrieve the details.
			| responseFields (string) - Filtering syntax appended to an API call to increase or decrease the amount of data returned inside a JSON object. This parameter should only be used to retrieve data. Attempting to update data using this parameter may cause data loss.
		
		Returns:
			| PriceList 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/storefront/pricelists/{priceListCode}?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("priceListCode", priceListCode);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getResolvedPriceList(self,customerAccountId = None, responseFields = None):
		""" Retrieves the details of a price list to which the specified customer resolves. This is primarly used when creating an offline order for a shopper.You can use this operation alongside custom Arc.js actions to alter the price list to which a shopper resolves.
		
		Args:
			| customerAccountId (int) - The unique identifier of the customer account for which to retrieve wish lists.
			| responseFields (string) - Filtering syntax appended to an API call to increase or decrease the amount of data returned inside a JSON object. This parameter should only be used to retrieve data. Attempting to update data using this parameter may cause data loss.
		
		Returns:
			| ResolvedPriceList 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/storefront/pricelists/resolved?customerAccountId={customerAccountId}&responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("customerAccountId", customerAccountId);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
	
	