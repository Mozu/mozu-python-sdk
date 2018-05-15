
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class Facet(object):
	def __init__(self, apiContext: ApiContext = None, mozuClient = None):
		self.client = mozuClient or default_client();
		if (apiContext is not None):
			self.client.withApiContext(apiContext);
		else:
			self.client.withApiContext(ApiContext());
	
	def getFacets(self,documentListName, propertyName):
		""" 
		
		Args:
			| documentListName (string) - The document list associated with the facets to retrieve.
			| propertyName (string) - The property name associated with the facets to retrieve.
		
		Returns:
			| array of Facet 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/content/documentlists/{documentListName}/facets/{propertyName}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("documentListName", documentListName);
		url.formatUrl("propertyName", propertyName);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
	
	