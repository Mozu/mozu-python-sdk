
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class CredentialStoreEntry(object):
	def __init__(self, apiContext: ApiContext = None, mozuClient = None):
		self.client = mozuClient or default_client();
		if (apiContext is not None):
			self.client.withApiContext(apiContext);
		else:
			self.client.withApiContext(ApiContext());
	
	def storeCredentials(self,credentials):
		""" Encrypts and stores data contained in the  JSON object. You can decrypt and access the secured data using an Arc.js application, as described in the Arc.js [Programming Patterns](https://www.mozu.com/docs/developer/arcjs-guides/programming-patterns.htm#securely_store_and_access_sensitive_data) topic.
		
		Args:
			| credentials(credentials) - 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/platform/extensions/credentialStore/", "POST", UrlLocation.TenantPod, False);
		self.client.withResourceUrl(url).withBody(credentials).execute();

	
	
	