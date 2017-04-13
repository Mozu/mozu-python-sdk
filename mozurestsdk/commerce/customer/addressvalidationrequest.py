
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class AddressValidationRequest(object):
	def __init__(self, apiContext: ApiContext = None, mozuClient = None):
		self.client = mozuClient or default_client();
		if (apiContext is not None):
			self.client.withApiContext(apiContext);
		else:
			self.client.withApiContext(ApiContext());
	
	def validateAddress(self,addressValidationRequest, responseFields = None):
		""" Validates the customer address supplied in the request.
		
		Args:
			| addressValidationRequest(addressValidationRequest) - Properties of the address used for validation of the account's full address. This content may include multiple lines of an address, city, state/province, zip/postal code, and country.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| AddressValidationResponse 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/customer/addressvalidation/?responseFields={responseFields}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(addressValidationRequest).execute();
		return self.client.result();

	
	
	