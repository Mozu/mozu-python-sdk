
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class CheckoutSettings(object):
	def __init__(self, apiContext: ApiContext = None, mozuClient = None):
		self.client = mozuClient or default_client();
		if (apiContext is not None):
			self.client.withApiContext(apiContext);
		else:
			self.client.withApiContext(ApiContext());
	
	def getCheckoutSettings(self,responseFields = None):
		""" Retrieves all checkout settings defined for the site including payment settings (payment gateway ID and credentials), shopper checkout settings (login requirement or guest mode and custom attributes), and order processing settings (when payment is authorized and captured plus any custom attributes).
		
		Args:
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| CheckoutSettings 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/settings/checkout/?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
	
	