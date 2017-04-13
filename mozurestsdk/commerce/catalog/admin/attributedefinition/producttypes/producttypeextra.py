
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class ProductTypeExtra(object):
	def __init__(self, apiContext: ApiContext = None, dataViewMode="Live", mozuClient = None):
		if (apiContext is not None and apiContext.dataViewMode is None):
			apiContext.dataViewMode = dataViewMode;
		else:
			apiContext = ApiContext(dataViewMode = dataViewMode);
		self.client = mozuClient or default_client();
		self.client.withApiContext(apiContext);
	
	def getExtras(self,productTypeId):
		""" Retrieves a list of extra attributes defined for the specified product type.
		
		Args:
			| productTypeId (int) - Identifier of the product type.
		
		Returns:
			| array of AttributeInProductType 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/attributedefinition/producttypes/{productTypeId}/Extras", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("productTypeId", productTypeId);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getExtra(self,productTypeId, attributeFQN, responseFields = None):
		""" Retrieves the details of an extra attribute definition for the specified product type.
		
		Args:
			| productTypeId (int) - Identifier of the product type.
			| attributeFQN (string) - The fully qualified name of the attribute, which is a user defined attribute identifier.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| AttributeInProductType 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/attributedefinition/producttypes/{productTypeId}/Extras/{attributeFQN}?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("attributeFQN", attributeFQN);
		url.formatUrl("productTypeId", productTypeId);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def addExtra(self,attributeInProductType, productTypeId, responseFields = None):
		""" Assigns a defined extra attribute to the product type based on the information supplied in the request.
		
		Args:
			| attributeInProductType(attributeInProductType) - Properties of an attribute definition associated with a specific product type. When an attribute is applied to a product type, each product of that type maintains the same set of attributes.
			| productTypeId (int) - Identifier of the product type.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| AttributeInProductType 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/attributedefinition/producttypes/{productTypeId}/Extras?responseFields={responseFields}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("productTypeId", productTypeId);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(attributeInProductType).execute();
		return self.client.result();

	
		
	def updateExtra(self,attributeInProductType, productTypeId, attributeFQN, responseFields = None):
		""" Update the definition of an extra attribute for the specified product type.
		
		Args:
			| attributeInProductType(attributeInProductType) - Properties of an attribute definition associated with a specific product type. When an attribute is applied to a product type, each product of that type maintains the same set of attributes.
			| productTypeId (int) - Identifier of the product type.
			| attributeFQN (string) - The fully qualified name of the attribute, which is a user defined attribute identifier.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| AttributeInProductType 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/attributedefinition/producttypes/{productTypeId}/Extras/{attributeFQN}?responseFields={responseFields}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("attributeFQN", attributeFQN);
		url.formatUrl("productTypeId", productTypeId);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(attributeInProductType).execute();
		return self.client.result();

	
		
	def deleteExtra(self,productTypeId, attributeFQN):
		""" Removes an extra attribute definition from the specified product type.
		
		Args:
			| productTypeId (int) - Identifier of the product type.
			| attributeFQN (string) - The fully qualified name of the attribute, which is a user defined attribute identifier.
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/attributedefinition/producttypes/{productTypeId}/Extras/{attributeFQN}", "DELETE", UrlLocation.TenantPod, False);
		url.formatUrl("attributeFQN", attributeFQN);
		url.formatUrl("productTypeId", productTypeId);
		self.client.withResourceUrl(url).execute();

	
	
	