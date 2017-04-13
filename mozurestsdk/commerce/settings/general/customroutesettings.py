
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class CustomRouteSettings(object):
	def __init__(self, apiContext: ApiContext = None, mozuClient = None):
		self.client = mozuClient or default_client();
		if (apiContext is not None):
			self.client.withApiContext(apiContext);
		else:
			self.client.withApiContext(ApiContext());
	
	def getCustomRouteSettings(self,responseFields = None):
		""" Retrieves the custom route settings configured for a site. These are the same settings configured through  in the Custom Routing JSON Editor.
		
		Args:
			| responseFields (string) - Filtering syntax appended to an API call to increase or decrease the amount of data returned inside a JSON object. This parameter should only be used to retrieve data. Attempting to update data using this parameter may cause data loss.
		
		Returns:
			| CustomRouteSettings 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/settings/general/customroutes?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def createCustomRouteSettings(self,settings, responseFields = None):
		""" Create new custom route settings.
		
		Args:
			| settings(settings) - The details of the new custom route setting.
			| responseFields (string) - Filtering syntax appended to an API call to increase or decrease the amount of data returned inside a JSON object. This parameter should only be used to retrieve data. Attempting to update data using this parameter may cause data loss.
		
		Returns:
			| CustomRouteSettings 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/settings/general/customroutes?responseFields={responseFields}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(settings).execute();
		return self.client.result();

	
		
	def updateCustomRouteSettings(self,settings, responseFields = None):
		""" Updates custom route settings.
		
		Args:
			| settings(settings) - The updated details of the custom route settings.
			| responseFields (string) - Filtering syntax appended to an API call to increase or decrease the amount of data returned inside a JSON object. This parameter should only be used to retrieve data. Attempting to update data using this parameter may cause data loss.
		
		Returns:
			| CustomRouteSettings 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/settings/general/customroutes?responseFields={responseFields}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(settings).execute();
		return self.client.result();

	
		
	def deleteCustomRouteSettings(self,):
		""" Deletes all the custom route settings for a site, returning all routes to their  defaults.
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/settings/general/customroutes", "DELETE", UrlLocation.TenantPod, False);
		self.client.withResourceUrl(url).execute();

	
	
	