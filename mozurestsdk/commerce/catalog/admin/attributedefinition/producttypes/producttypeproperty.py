
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class ProductTypeProperty(object):
	def __init__(self, apiContext: ApiContext = None, dataViewMode="Live", mozuClient = None):
		if (apiContext.dataViewMode is None):
			apiContext.dataViewMode = dataViewMode;
		self.client = mozuClient or default_client();
		self.client.withApiContext(apiContext);
	
	def getProperties(self,productTypeId):
		""" Retrieves a list of product property attributes defined for a product type.
		
		Args:
			| productTypeId (int) - Identifier of the product type.
		
		Returns:
			| array of AttributeInProductType 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/attributedefinition/producttypes/{productTypeId}/Properties", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("productTypeId", productTypeId);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getProperty(self,productTypeId, attributeFQN, responseFields = None):
		""" Retrieves a product property attribute definition for the specified product type.
		
		Args:
			| productTypeId (int) - Identifier of the product type.
			| attributeFQN (string) - The fully qualified name of the attribute, which is a user defined attribute identifier.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| AttributeInProductType 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/attributedefinition/producttypes/{productTypeId}/Properties/{attributeFQN}?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("attributeFQN", attributeFQN);
		url.formatUrl("productTypeId", productTypeId);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def addProperty(self,attributeInProductType, productTypeId, responseFields = None):
		""" Assigns a property attribute to the specified product type, according to the information defined in the request.
		
		Args:
			| attributeInProductType(attributeInProductType) - Properties of an attribute definition associated with a specific product type. When an attribute is applied to a product type, each product of that type maintains the same set of attributes.
			| productTypeId (int) - Identifier of the product type.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| AttributeInProductType 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/attributedefinition/producttypes/{productTypeId}/Properties?responseFields={responseFields}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("productTypeId", productTypeId);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(attributeInProductType).execute();
		return self.client.result();

	
		
	def updateProperty(self,attributeInProductType, productTypeId, attributeFQN, responseFields = None):
		""" Updates the definition of a property attribute for the specified product type.
		
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

		url = MozuUrl("/api/commerce/catalog/admin/attributedefinition/producttypes/{productTypeId}/Properties/{attributeFQN}?responseFields={responseFields}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("attributeFQN", attributeFQN);
		url.formatUrl("productTypeId", productTypeId);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(attributeInProductType).execute();
		return self.client.result();

	
		
	def deleteProperty(self,productTypeId, attributeFQN):
		""" Removes a property attribute previously defined for the specified product type.
		
		Args:
			| productTypeId (int) - Identifier of the product type.
			| attributeFQN (string) - The fully qualified name of the attribute, which is a user defined attribute identifier.
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/attributedefinition/producttypes/{productTypeId}/Properties/{attributeFQN}", "DELETE", UrlLocation.TenantPod, False);
		url.formatUrl("attributeFQN", attributeFQN);
		url.formatUrl("productTypeId", productTypeId);
		self.client.withResourceUrl(url).execute();

	
	
	