
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class UserData(object):
	def __init__(self, apiContext: ApiContext = None, mozuClient = None):
		self.client = mozuClient or default_client();
		client.withApiContext(apiContext);
	
	def getDBValue(self,dbEntryQuery, responseFields = None):
		""" Retrieves the value of a record in the Mozu database.
		
		Args:
			| dbEntryQuery (string) - The database entry string to create.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| string 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/platform/userdata/{*dbEntryQuery}?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("dbEntryQuery", dbEntryQuery);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def createDBValue(self,value, dbEntryQuery):
		""" Creates a new record in the Mozu database based on the information supplied in the request.
		
		Args:
			| value(value) - The value string to create.
			| dbEntryQuery (string) - The database entry string to create.
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/platform/userdata/{*dbEntryQuery}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("dbEntryQuery", dbEntryQuery);
		self.client.withResourceUrl(url).withBody(value).execute();

	
		
	def updateDBValue(self,value, dbEntryQuery):
		""" Updates a record in the Mozu database based on the information supplied in the request.
		
		Args:
			| value(value) - The value string to create.
			| dbEntryQuery (string) - The database entry string to create.
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/platform/userdata/{*dbEntryQuery}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("dbEntryQuery", dbEntryQuery);
		self.client.withResourceUrl(url).withBody(value).execute();

	
		
	def deleteDBValue(self,dbEntryQuery):
		""" Removes a previously defined record in the Mozu database.
		
		Args:
			| dbEntryQuery (string) - The database entry string to create.
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/platform/userdata/{*dbEntryQuery}", "DELETE", UrlLocation.TenantPod, False);
		url.formatUrl("dbEntryQuery", dbEntryQuery);
		self.client.withResourceUrl(url).execute();

	
	
	