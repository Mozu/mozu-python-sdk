
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class ExtendedProperty(object):
	def __init__(self, apiContext: ApiContext = None, mozuClient = None):
		self.client = mozuClient or default_client();
		if (apiContext is not None):
			self.client.withApiContext(apiContext);
		else:
			self.client.withApiContext(ApiContext());
	
	def getExtendedProperties(self,):
		""" 
		
		Returns:
			| array of ExtendedProperty 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/carts/current/extendedproperties", "GET", UrlLocation.TenantPod, False);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def addExtendedProperties(self,extendedProperties):
		""" 
		
		Args:
			| extendedProperties(array|extendedProperties) - The details of the new extended property.
		
		Returns:
			| array of ExtendedProperty 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/carts/current/extendedproperties", "POST", UrlLocation.TenantPod, False);
		self.client.withResourceUrl(url).withBody(extendedProperties).execute();
		return self.client.result();

	
		
	def updateExtendedProperty(self,extendedProperty, key, upsert = False, responseFields = None):
		""" 
		
		Args:
			| extendedProperty(extendedProperty) - The details of the updated extended property.
			| key (string) - Key used for metadata defined for objects, including extensible attributes, custom attributes associated with a shipping provider, and search synonyms definitions. This content may be user-defined depending on the object and usage.
			| upsert (bool) - Any set of key value pairs to be stored in the extended properties of a cart.
			| responseFields (string) - Filtering syntax appended to an API call to increase or decrease the amount of data returned inside a JSON object. This parameter should only be used to retrieve data. Attempting to update data using this parameter may cause data loss.
		
		Returns:
			| ExtendedProperty 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/carts/current/extendedproperties/{key}?upsert={upsert}&responseFields={responseFields}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("key", key);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("upsert", upsert);
		self.client.withResourceUrl(url).withBody(extendedProperty).execute();
		return self.client.result();

	
		
	def updateExtendedProperties(self,extendedProperties, upsert = False):
		""" 
		
		Args:
			| extendedProperties(array|extendedProperties) - The details of the updated extended properties.
			| upsert (bool) - Any set of key value pairs to be stored in the extended properties of a cart.
		
		Returns:
			| array of ExtendedProperty 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/carts/current/extendedproperties?upsert={upsert}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("upsert", upsert);
		self.client.withResourceUrl(url).withBody(extendedProperties).execute();
		return self.client.result();

	
		
	def deleteExtendedProperties(self,keys):
		""" 
		
		Args:
			| keys(array|keys) - 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/carts/current/extendedproperties", "DELETE", UrlLocation.TenantPod, False);
		self.client.withResourceUrl(url).withBody(keys).execute();

	
		
	def deleteExtendedProperty(self,key):
		""" 
		
		Args:
			| key (string) - 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/carts/current/extendedproperties/{key}", "DELETE", UrlLocation.TenantPod, False);
		url.formatUrl("key", key);
		self.client.withResourceUrl(url).execute();

	
	
	