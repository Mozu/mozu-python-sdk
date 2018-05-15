
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class ProductProperty(object):
	def __init__(self, apiContext: ApiContext = None, dataViewMode="Live", mozuClient = None):
		if (apiContext is not None and apiContext.dataViewMode is None):
			apiContext.dataViewMode = dataViewMode;
		else:
			apiContext = ApiContext(dataViewMode = dataViewMode);
		self.client = mozuClient or default_client();
		self.client.withApiContext(apiContext);
	
	def getProperties(self,productCode):
		""" 
		
		Args:
			| productCode (string) - 
		
		Returns:
			| array of ProductProperty 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/products/{productCode}/Properties", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("productCode", productCode);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getPropertyValueLocalizedContents(self,productCode, attributeFQN, value):
		""" 
		
		Args:
			| productCode (string) - 
			| attributeFQN (string) - 
			| value (string) - 
		
		Returns:
			| array of ProductPropertyValueLocalizedContent 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/products/{productCode}/Properties/{attributeFQN}/values/{value}/LocalizedContent", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("attributeFQN", attributeFQN);
		url.formatUrl("productCode", productCode);
		url.formatUrl("value", value);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getPropertyValueLocalizedContent(self,productCode, attributeFQN, value, localeCode, responseFields = None):
		""" 
		
		Args:
			| productCode (string) - 
			| attributeFQN (string) - 
			| value (string) - 
			| localeCode (string) - 
			| responseFields (string) - 
		
		Returns:
			| ProductPropertyValueLocalizedContent 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/products/{productCode}/Properties/{attributeFQN}/values/{value}/LocalizedContent/{localeCode}?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("attributeFQN", attributeFQN);
		url.formatUrl("localeCode", localeCode);
		url.formatUrl("productCode", productCode);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("value", value);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getProperty(self,productCode, attributeFQN, responseFields = None):
		""" 
		
		Args:
			| productCode (string) - 
			| attributeFQN (string) - 
			| responseFields (string) - 
		
		Returns:
			| ProductProperty 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/products/{productCode}/Properties/{attributeFQN}?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("attributeFQN", attributeFQN);
		url.formatUrl("productCode", productCode);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def addPropertyValueLocalizedContent(self,localizedContent, productCode, attributeFQN, value, responseFields = None):
		""" 
		
		Args:
			| localizedContent(localizedContent) - 
			| productCode (string) - 
			| attributeFQN (string) - 
			| value (string) - 
			| responseFields (string) - 
		
		Returns:
			| ProductPropertyValueLocalizedContent 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/products/{productCode}/Properties/{attributeFQN}/values/{value}/LocalizedContent?responseFields={responseFields}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("attributeFQN", attributeFQN);
		url.formatUrl("productCode", productCode);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("value", value);
		self.client.withResourceUrl(url).withBody(localizedContent).execute();
		return self.client.result();

	
		
	def addProperty(self,productProperty, productCode, responseFields = None):
		""" 
		
		Args:
			| productProperty(productProperty) - Properties of the property attribute to configure for a product.
			| productCode (string) - 
			| responseFields (string) - 
		
		Returns:
			| ProductProperty 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/products/{productCode}/Properties?responseFields={responseFields}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("productCode", productCode);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(productProperty).execute();
		return self.client.result();

	
		
	def updatePropertyValueLocalizedContents(self,localizedContent, productCode, attributeFQN, value):
		""" 
		
		Args:
			| localizedContent(array|localizedContent) - 
			| productCode (string) - 
			| attributeFQN (string) - 
			| value (string) - 
		
		Returns:
			| array of ProductPropertyValueLocalizedContent 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/products/{productCode}/Properties/{attributeFQN}/values/{value}/LocalizedContent", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("attributeFQN", attributeFQN);
		url.formatUrl("productCode", productCode);
		url.formatUrl("value", value);
		self.client.withResourceUrl(url).withBody(localizedContent).execute();
		return self.client.result();

	
		
	def updatePropertyValueLocalizedContent(self,localizedContent, productCode, attributeFQN, value, localeCode, responseFields = None):
		""" 
		
		Args:
			| localizedContent(localizedContent) - 
			| productCode (string) - 
			| attributeFQN (string) - 
			| value (string) - 
			| localeCode (string) - 
			| responseFields (string) - 
		
		Returns:
			| ProductPropertyValueLocalizedContent 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/products/{productCode}/Properties/{attributeFQN}/values/{value}/LocalizedContent/{localeCode}?responseFields={responseFields}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("attributeFQN", attributeFQN);
		url.formatUrl("localeCode", localeCode);
		url.formatUrl("productCode", productCode);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("value", value);
		self.client.withResourceUrl(url).withBody(localizedContent).execute();
		return self.client.result();

	
		
	def updateProperty(self,productProperty, productCode, attributeFQN, responseFields = None):
		""" 
		
		Args:
			| productProperty(productProperty) - Details of the property attribute to update for the product configuration.
			| productCode (string) - 
			| attributeFQN (string) - 
			| responseFields (string) - 
		
		Returns:
			| ProductProperty 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/products/{productCode}/Properties/{attributeFQN}?responseFields={responseFields}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("attributeFQN", attributeFQN);
		url.formatUrl("productCode", productCode);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(productProperty).execute();
		return self.client.result();

	
		
	def deleteProperty(self,productCode, attributeFQN):
		""" 
		
		Args:
			| productCode (string) - 
			| attributeFQN (string) - 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/products/{productCode}/Properties/{attributeFQN}", "DELETE", UrlLocation.TenantPod, False);
		url.formatUrl("attributeFQN", attributeFQN);
		url.formatUrl("productCode", productCode);
		self.client.withResourceUrl(url).execute();

	
		
	def deletePropertyValueLocalizedContent(self,productCode, attributeFQN, value, localeCode):
		""" 
		
		Args:
			| productCode (string) - 
			| attributeFQN (string) - 
			| value (string) - 
			| localeCode (string) - 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/products/{productCode}/Properties/{attributeFQN}/values/{value}/LocalizedContent/{localeCode}", "DELETE", UrlLocation.TenantPod, False);
		url.formatUrl("attributeFQN", attributeFQN);
		url.formatUrl("localeCode", localeCode);
		url.formatUrl("productCode", productCode);
		url.formatUrl("value", value);
		self.client.withResourceUrl(url).execute();

	
	
	