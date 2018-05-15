
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class CustomerAttribute(object):
	def __init__(self, apiContext: ApiContext = None, mozuClient = None):
		self.client = mozuClient or default_client();
		if (apiContext is not None):
			self.client.withApiContext(apiContext);
		else:
			self.client.withApiContext(ApiContext());
	
	def getAccountAttribute(self,accountId, attributeFQN, responseFields = None):
		""" 
		
		Args:
			| accountId (int) - Identifier of the customer account associated with the attribute to retrieve.
			| attributeFQN (string) - 
			| responseFields (string) - 
		
		Returns:
			| CustomerAttribute 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/customer/accounts/{accountId}/attributes/{attributeFQN}?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("accountId", accountId);
		url.formatUrl("attributeFQN", attributeFQN);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getAccountAttributes(self,accountId, startIndex = None, pageSize = None, sortBy = None, filter = None, responseFields = None):
		""" 
		
		Args:
			| accountId (int) - Identifier of the customer account associated with the attributes to retrieve.
			| startIndex (int) - 
			| pageSize (int) - 
			| sortBy (string) - 
			| filter (string) - 
			| responseFields (string) - 
		
		Returns:
			| CustomerAttributeCollection 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/customer/accounts/{accountId}/attributes?startIndex={startIndex}&pageSize={pageSize}&sortBy={sortBy}&filter={filter}&responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("accountId", accountId);
		url.formatUrl("filter", filter);
		url.formatUrl("pageSize", pageSize);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("sortBy", sortBy);
		url.formatUrl("startIndex", startIndex);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def addAccountAttribute(self,attribute, accountId, responseFields = None):
		""" 
		
		Args:
			| attribute(attribute) - The attribute to add to the customer account.
			| accountId (int) - Unique identifier of the customer account.
			| responseFields (string) - 
		
		Returns:
			| CustomerAttribute 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/customer/accounts/{accountId}/attributes?responseFields={responseFields}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("accountId", accountId);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(attribute).execute();
		return self.client.result();

	
		
	def updateAccountAttribute(self,attribute, accountId, attributeFQN, responseFields = None):
		""" 
		
		Args:
			| attribute(attribute) - Properties of the customer account attribute to update.
			| accountId (int) - Identifier of the customer account associated with the attribute.
			| attributeFQN (string) - 
			| responseFields (string) - 
		
		Returns:
			| CustomerAttribute 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/customer/accounts/{accountId}/attributes/{attributeFQN}?responseFields={responseFields}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("accountId", accountId);
		url.formatUrl("attributeFQN", attributeFQN);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(attribute).execute();
		return self.client.result();

	
		
	def deleteAccountAttribute(self,accountId, attributeFQN):
		""" 
		
		Args:
			| accountId (int) - Unique identifier of the customer account.
			| attributeFQN (string) - 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/customer/accounts/{accountId}/attributes/{attributeFQN}", "DELETE", UrlLocation.TenantPod, False);
		url.formatUrl("accountId", accountId);
		url.formatUrl("attributeFQN", attributeFQN);
		self.client.withResourceUrl(url).execute();

	
	
	