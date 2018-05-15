
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation

class Package(object):
	def __init__(self, mozuClient = None):
		self.client = mozuClient or default_client();
	
	def getFile(self,applicationKey, fileName):
		""" 
		
		Args:
			| applicationKey (string) - The application key uniquely identifies the developer namespace, application ID, version, and package in Dev Center. The format is {Dev Account namespace}.{Application ID}.{Application Version}.{Package name}. 
			| fileName (string) - 
		
		Returns:
			| Stream 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/platform/appdev/filebasedpackage/packages/{applicationKey}?fileName={fileName}", "GET", UrlLocation.HomePod, False);
		url.formatUrl("applicationKey", applicationKey);
		url.formatUrl("fileName", fileName);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
	
	