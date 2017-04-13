
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class Transaction(object):
	def __init__(self, apiContext: ApiContext = None, mozuClient = None):
		self.client = mozuClient or default_client();
		if (apiContext is not None):
			self.client.withApiContext(apiContext);
		else:
			self.client.withApiContext(ApiContext());
	
	def getTransactions(self,accountId):
		""" Retrieves a list of transactions associated with the customer account specified in the request.
		
		Args:
			| accountId (int) - Unique identifier of the customer account.
		
		Returns:
			| array of Transaction 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/customer/accounts/{accountId}/transactions", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("accountId", accountId);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def addTransaction(self,transaction, accountId, responseFields = None):
		""" Creates a new transaction for the customer account specified in the request.
		
		Args:
			| transaction(transaction) - Properties of a transaction performed by a customer account. The system creates a transaction each time the customer submits an order, returns an item, picks up items for an order, or manages items on a wish list.
			| accountId (int) - Unique identifier of the customer account.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| Transaction 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/customer/accounts/{accountId}/transactions?responseFields={responseFields}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("accountId", accountId);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(transaction).execute();
		return self.client.result();

	
		
	def removeTransaction(self,accountId, transactionId):
		""" Deletes a transaction from the customer account specified in the request.
		
		Args:
			| accountId (int) - Unique identifier of the customer account.
			| transactionId (string) - Unique identifier of the transaction to delete.
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/customer/accounts/{accountId}/transactions/{transactionId}", "DELETE", UrlLocation.TenantPod, False);
		url.formatUrl("accountId", accountId);
		url.formatUrl("transactionId", transactionId);
		self.client.withResourceUrl(url).execute();

	
	
	