
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class OrderNote(object):
	def __init__(self, apiContext: ApiContext = None, mozuClient = None):
		self.client = mozuClient or default_client();
		if (apiContext is not None):
			self.client.withApiContext(apiContext);
		else:
			self.client.withApiContext(ApiContext());
	
	def getReturnNotes(self,returnId):
		""" Retrieves all internal notes associated with a return.
		
		Args:
			| returnId (string) - Unique identifier of the return whose items you want to get.
		
		Returns:
			| array of OrderNote 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/returns/{returnId}/notes", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("returnId", returnId);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getReturnNote(self,returnId, noteId, responseFields = None):
		""" Retrieves a specific internal note from a return.
		
		Args:
			| returnId (string) - Unique identifier of the return whose items you want to get.
			| noteId (string) - Unique identifier of a particular note to retrieve.
			| responseFields (string) - Filtering syntax appended to an API call to increase or decrease the amount of data returned inside a JSON object. This parameter should only be used to retrieve data. Attempting to update data using this parameter may cause data loss.
		
		Returns:
			| OrderNote 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/returns/{returnId}/notes/{noteId}?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("noteId", noteId);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("returnId", returnId);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def createReturnNote(self,returnNote, returnId, responseFields = None):
		""" Creates an internal note on a given return. This note is visible in  for customer service representatives to see.
		
		Args:
			| returnNote(returnNote) - 
			| returnId (string) - Unique identifier of the return whose items you want to get.
			| responseFields (string) - Filtering syntax appended to an API call to increase or decrease the amount of data returned inside a JSON object. This parameter should only be used to retrieve data. Attempting to update data using this parameter may cause data loss.
		
		Returns:
			| OrderNote 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/returns/{returnId}/notes?responseFields={responseFields}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("returnId", returnId);
		self.client.withResourceUrl(url).withBody(returnNote).execute();
		return self.client.result();

	
		
	def updateReturnNote(self,returnNote, returnId, noteId, responseFields = None):
		""" Updates an internal note on a given return. This note is visible in  for customer service representatives to see.
		
		Args:
			| returnNote(returnNote) - 
			| returnId (string) - Unique identifier of the return whose items you want to get.
			| noteId (string) - Unique identifier of a particular note to retrieve.
			| responseFields (string) - Filtering syntax appended to an API call to increase or decrease the amount of data returned inside a JSON object. This parameter should only be used to retrieve data. Attempting to update data using this parameter may cause data loss.
		
		Returns:
			| OrderNote 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/returns/{returnId}/notes/{noteId}?responseFields={responseFields}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("noteId", noteId);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("returnId", returnId);
		self.client.withResourceUrl(url).withBody(returnNote).execute();
		return self.client.result();

	
		
	def deleteReturnNote(self,returnId, noteId):
		""" Deletes an internal note from a given return.
		
		Args:
			| returnId (string) - Unique identifier of the return whose items you want to get.
			| noteId (string) - Unique identifier of a particular note to retrieve.
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/returns/{returnId}/notes/{noteId}", "DELETE", UrlLocation.TenantPod, False);
		url.formatUrl("noteId", noteId);
		url.formatUrl("returnId", returnId);
		self.client.withResourceUrl(url).execute();

	
	
	