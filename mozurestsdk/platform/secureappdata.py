
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class SecureAppData(object):
	def __init__(self, apiContext: ApiContext = None, mozuClient = None):
		self.client = mozuClient or default_client();
		if (apiContext is not None):
			self.client.withApiContext(apiContext);
		else:
			self.client.withApiContext(ApiContext());
	
	def getDBValue(self,appKeyId, dbEntryQuery, responseFields = None):
		""" 
		
		Args:
			| appKeyId (string) - 
			| dbEntryQuery (string) - The database entry string to create.
			| responseFields (string) - Filtering syntax appended to an API call to increase or decrease the amount of data returned inside a JSON object. This parameter should only be used to retrieve data. Attempting to update data using this parameter may cause data loss.
		
		Returns:
			| JObject 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/platform/secureappdata/{appKeyId}/{*dbEntryQuery}?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("appKeyId", appKeyId);
		url.formatUrl("dbEntryQuery", dbEntryQuery);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def createDBValue(self,value, appKeyId, dbEntryQuery):
		""" 
		
		Args:
			| value(value) - The value string to create.
			| appKeyId (string) - 
			| dbEntryQuery (string) - The database entry string to create.
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/platform/secureappdata/{appKeyId}/{*dbEntryQuery}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("appKeyId", appKeyId);
		url.formatUrl("dbEntryQuery", dbEntryQuery);
		self.client.withResourceUrl(url).withBody(value).execute();

	
		
	def updateDBValue(self,value, appKeyId, dbEntryQuery):
		""" 
		
		Args:
			| value(value) - The value string to create.
			| appKeyId (string) - 
			| dbEntryQuery (string) - The database entry string to create.
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/platform/secureappdata/{appKeyId}/{*dbEntryQuery}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("appKeyId", appKeyId);
		url.formatUrl("dbEntryQuery", dbEntryQuery);
		self.client.withResourceUrl(url).withBody(value).execute();

	
		
	def deleteDBValue(self,appKeyId, dbEntryQuery):
		""" 
		
		Args:
			| appKeyId (string) - 
			| dbEntryQuery (string) - The database entry string to create.
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/platform/secureappdata/{appKeyId}/{*dbEntryQuery}", "DELETE", UrlLocation.TenantPod, False);
		url.formatUrl("appKeyId", appKeyId);
		url.formatUrl("dbEntryQuery", dbEntryQuery);
		self.client.withResourceUrl(url).execute();

	
	
	