
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class Attribute(object):
	def __init__(self, apiContext: ApiContext = None, mozuClient = None):
		self.client = mozuClient or default_client();
		if (apiContext is not None):
			self.client.withApiContext(apiContext);
		else:
			self.client.withApiContext(ApiContext());
	
	def getAttributes(self,startIndex = None, pageSize = None, sortBy = None, filter = None, responseFields = None):
		""" 
		
		Args:
			| startIndex (int) - 
			| pageSize (int) - 
			| sortBy (string) - 
			| filter (string) - 
			| responseFields (string) - 
		
		Returns:
			| AttributeCollection 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/admin/locations/attributedefinition/attributes/?startIndex={startIndex}&pageSize={pageSize}&sortBy={sortBy}&filter={filter}&responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("filter", filter);
		url.formatUrl("pageSize", pageSize);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("sortBy", sortBy);
		url.formatUrl("startIndex", startIndex);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getAttributeVocabularyValues(self,attributeFQN):
		""" 
		
		Args:
			| attributeFQN (string) - 
		
		Returns:
			| array of AttributeVocabularyValue 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/admin/locations/attributedefinition/attributes/{attributeFQN}/VocabularyValues", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("attributeFQN", attributeFQN);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getAttribute(self,attributeFQN, responseFields = None):
		""" 
		
		Args:
			| attributeFQN (string) - 
			| responseFields (string) - 
		
		Returns:
			| Attribute 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/admin/locations/attributedefinition/attributes/{attributeFQN}?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("attributeFQN", attributeFQN);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def createAttribute(self,attribute, responseFields = None):
		""" 
		
		Args:
			| attribute(attribute) - 
			| responseFields (string) - 
		
		Returns:
			| Attribute 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/admin/locations/attributedefinition/attributes/?responseFields={responseFields}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(attribute).execute();
		return self.client.result();

	
		
	def updateAttribute(self,attribute, attributeFQN, responseFields = None):
		""" 
		
		Args:
			| attribute(attribute) - 
			| attributeFQN (string) - 
			| responseFields (string) - 
		
		Returns:
			| Attribute 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/admin/locations/attributedefinition/attributes/{attributeFQN}?responseFields={responseFields}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("attributeFQN", attributeFQN);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(attribute).execute();
		return self.client.result();

	
	
	