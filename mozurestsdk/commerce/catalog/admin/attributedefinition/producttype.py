
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class ProductType(object):
	def __init__(self, apiContext: ApiContext = None, dataViewMode="Live", mozuClient = None):
		if (apiContext is not None and apiContext.dataViewMode is None):
			apiContext.dataViewMode = dataViewMode;
		else:
			apiContext = ApiContext(dataViewMode = dataViewMode);
		self.client = mozuClient or default_client();
		self.client.withApiContext(apiContext);
	
	def getProductTypes(self,startIndex = None, pageSize = None, sortBy = None, filter = None, responseFields = None):
		""" 
		
		Args:
			| startIndex (int) - 
			| pageSize (int) - 
			| sortBy (string) - 
			| filter (string) - A set of expressions that consist of a field, operator, and value and represent search parameter syntax when filtering results of a query. You can filter product type search results by any of its properties. Valid operators include equals (eq), does not equal (ne), greater than (gt), less than (lt), greater than or equal to (ge), less than or equal to (le), starts with (sw), or contains (cont). For example - "filter=Name+cont+shoes"
			| responseFields (string) - 
		
		Returns:
			| ProductTypeCollection 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/attributedefinition/producttypes/?startIndex={startIndex}&pageSize={pageSize}&sortBy={sortBy}&filter={filter}&responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("filter", filter);
		url.formatUrl("pageSize", pageSize);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("sortBy", sortBy);
		url.formatUrl("startIndex", startIndex);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getProductType(self,productTypeId, responseFields = None):
		""" 
		
		Args:
			| productTypeId (int) - Identifier of the product type to retrieve.
			| responseFields (string) - 
		
		Returns:
			| ProductType 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/attributedefinition/producttypes/{productTypeId}?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("productTypeId", productTypeId);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def addProductType(self,productType, responseFields = None):
		""" 
		
		Args:
			| productType(productType) - Properties of the product type to create.
			| responseFields (string) - 
		
		Returns:
			| ProductType 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/attributedefinition/producttypes/?responseFields={responseFields}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(productType).execute();
		return self.client.result();

	
		
	def updateProductType(self,productType, productTypeId, responseFields = None):
		""" 
		
		Args:
			| productType(productType) - The details of the product type to update.
			| productTypeId (int) - Identifier of the product type to update.
			| responseFields (string) - 
		
		Returns:
			| ProductType 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/attributedefinition/producttypes/{productTypeId}?responseFields={responseFields}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("productTypeId", productTypeId);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(productType).execute();
		return self.client.result();

	
		
	def deleteProductType(self,productTypeId):
		""" 
		
		Args:
			| productTypeId (int) - Identifier of the product type to delete.
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/attributedefinition/producttypes/{productTypeId}", "DELETE", UrlLocation.TenantPod, False);
		url.formatUrl("productTypeId", productTypeId);
		self.client.withResourceUrl(url).execute();

	
	
	