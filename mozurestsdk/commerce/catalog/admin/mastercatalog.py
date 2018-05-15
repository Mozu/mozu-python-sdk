
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class MasterCatalog(object):
	def __init__(self, apiContext: ApiContext = None, mozuClient = None):
		self.client = mozuClient or default_client();
		if (apiContext is not None):
			self.client.withApiContext(apiContext);
		else:
			self.client.withApiContext(ApiContext());
	
	def getMasterCatalogs(self,responseFields = None):
		""" 
		
		Args:
			| responseFields (string) - Filtering syntax appended to an API call to increase or decrease the amount of data returned inside a JSON object. This parameter should only be used to retrieve data. Attempting to update data using this parameter may cause data loss.
		
		Returns:
			| MasterCatalogCollection 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/mastercatalogs/?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getMasterCatalog(self,masterCatalogId, responseFields = None):
		""" 
		
		Args:
			| masterCatalogId (int) - Unique identifier for the master catalog. The master catalog contains all products accessible per catalogs and the site/tenant.
			| responseFields (string) - Filtering syntax appended to an API call to increase or decrease the amount of data returned inside a JSON object. This parameter should only be used to retrieve data. Attempting to update data using this parameter may cause data loss.
		
		Returns:
			| MasterCatalog 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/mastercatalogs/{masterCatalogId}?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("masterCatalogId", masterCatalogId);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def updateMasterCatalog(self,masterCatalog, masterCatalogId, responseFields = None):
		""" 
		
		Args:
			| masterCatalog(masterCatalog) - Properties of a master product catalog defined for a tenant. All catalogs and sites associated with a master catalog share product definitions.
			| masterCatalogId (int) - Unique identifier for the master catalog. The master catalog contains all products accessible per catalogs and the site/tenant.
			| responseFields (string) - Filtering syntax appended to an API call to increase or decrease the amount of data returned inside a JSON object. This parameter should only be used to retrieve data. Attempting to update data using this parameter may cause data loss.
		
		Returns:
			| MasterCatalog 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/mastercatalogs/{masterCatalogId}?responseFields={responseFields}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("masterCatalogId", masterCatalogId);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(masterCatalog).execute();
		return self.client.result();

	
	
	