
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class DocumentListType(object):
	def __init__(self, apiContext: ApiContext = None, dataViewMode="Live", mozuClient = None):
		if (apiContext is not None and apiContext.dataViewMode is None):
			apiContext.dataViewMode = dataViewMode;
		else:
			apiContext = ApiContext(dataViewMode = dataViewMode);
		self.client = mozuClient or default_client();
		self.client.withApiContext(apiContext);
	
	def getDocumentListTypes(self,pageSize = None, startIndex = None, responseFields = None):
		""" 
		
		Args:
			| pageSize (int) - When creating paged results from a query, this value indicates the zero-based offset in the complete result set where the returned entities begin. For example, with this parameter set to 25, to get the 51st through the 75th items, set startIndex to 50.
			| startIndex (int) - When creating paged results from a query, this value indicates the zero-based offset in the complete result set where the returned entities begin. For example, with pageSize set to 25, to get the 51st through the 75th items, set this parameter to 50.
			| responseFields (string) - Filtering syntax appended to an API call to increase or decrease the amount of data returned inside a JSON object. This parameter should only be used to retrieve data. Attempting to update data using this parameter may cause data loss.
		
		Returns:
			| DocumentListTypeCollection 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/content/documentlistTypes/{documentListTypeFQN}?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("pageSize", pageSize);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("startIndex", startIndex);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getDocumentListType(self,documentListTypeFQN, responseFields = None):
		""" 
		
		Args:
			| documentListTypeFQN (string) - 
			| responseFields (string) - Filtering syntax appended to an API call to increase or decrease the amount of data returned inside a JSON object. This parameter should only be used to retrieve data. Attempting to update data using this parameter may cause data loss.
		
		Returns:
			| DocumentListType 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/content/documentlistTypes/{documentListTypeFQN}?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("documentListTypeFQN", documentListTypeFQN);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def createDocumentListType(self,list, responseFields = None):
		""" 
		
		Args:
			| list(list) - Properties for the document list type. Document lists contain documents with an associated document type, such as web pages.
			| responseFields (string) - Filtering syntax appended to an API call to increase or decrease the amount of data returned inside a JSON object. This parameter should only be used to retrieve data. Attempting to update data using this parameter may cause data loss.
		
		Returns:
			| DocumentListType 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/content/documentlistTypes/?responseFields={responseFields}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(list).execute();
		return self.client.result();

	
		
	def updateDocumentListType(self,list, documentListTypeFQN, responseFields = None):
		""" 
		
		Args:
			| list(list) - Properties for the document list type. Document lists contain documents with an associated document type, such as web pages.
			| documentListTypeFQN (string) - 
			| responseFields (string) - Filtering syntax appended to an API call to increase or decrease the amount of data returned inside a JSON object. This parameter should only be used to retrieve data. Attempting to update data using this parameter may cause data loss.
		
		Returns:
			| DocumentListType 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/content/documentlistTypes/{documentListTypeFQN}?responseFields={responseFields}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("documentListTypeFQN", documentListTypeFQN);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(list).execute();
		return self.client.result();

	
	
	