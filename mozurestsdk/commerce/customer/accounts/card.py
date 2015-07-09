
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class Card(object):
	def __init__(self, apiContext: ApiContext = None, mozuClient = None):
		self.client = mozuClient or default_client();
		if (apiContext is not None):
			self.client.withApiContext(apiContext);
		else:
			self.client.withApiContext(ApiContext());
	
	def getAccountCard(self,accountId, cardId, responseFields = None):
		""" Retrieves the details of a credit card stored with a customer account billing contact.
		
		Args:
			| accountId (int) - Unique identifier of the customer account.
			| cardId (string) - Unique identifier of the card associated with the customer account billing contact.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| Card 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/customer/accounts/{accountId}/cards/{cardId}?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("accountId", accountId);
		url.formatUrl("cardId", cardId);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getAccountCards(self,accountId, responseFields = None):
		""" Retrieves all stored credit cards for the customer account.
		
		Args:
			| accountId (int) - Unique identifier of the customer account.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| CardCollection 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/customer/accounts/{accountId}/cards?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("accountId", accountId);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def addAccountCard(self,card, accountId, responseFields = None):
		""" Creates a new credit card record and stores it for the customer account.
		
		Args:
			| card(card) - Properties of a credit card used to submit payment for an order.
			| accountId (int) - Unique identifier of the customer account.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| Card 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/customer/accounts/{accountId}/cards?responseFields={responseFields}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("accountId", accountId);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(card).execute();
		return self.client.result();

	
		
	def updateAccountCard(self,card, accountId, cardId, responseFields = None):
		""" Update one or more properties of a credit card defined for a customer account.
		
		Args:
			| card(card) - Properties of a credit card used to submit payment for an order.
			| accountId (int) - Unique identifier of the customer account.
			| cardId (string) - Unique identifier of the card associated with the customer account billing contact.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| Card 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/customer/accounts/{accountId}/cards/{cardId}?responseFields={responseFields}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("accountId", accountId);
		url.formatUrl("cardId", cardId);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(card).execute();
		return self.client.result();

	
		
	def deleteAccountCard(self,accountId, cardId):
		""" Removes a stored credit card from a customer account.
		
		Args:
			| accountId (int) - Unique identifier of the customer account.
			| cardId (string) - Unique identifier of the card associated with the customer account billing contact.
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/customer/accounts/{accountId}/cards/{cardId}", "DELETE", UrlLocation.TenantPod, False);
		url.formatUrl("accountId", accountId);
		url.formatUrl("cardId", cardId);
		self.client.withResourceUrl(url).execute();

	
	
	