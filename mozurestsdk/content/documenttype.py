
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class DocumentType(object):
	def __init__(self, apiContext: ApiContext = None, dataViewMode="Live", mozuClient = None):
		if (apiContext is not None and apiContext.dataViewMode is None):
			apiContext.dataViewMode = dataViewMode;
		else:
			apiContext = ApiContext(dataViewMode = dataViewMode);
		self.client = mozuClient or default_client();
		self.client.withApiContext(apiContext);
	
	def getDocumentTypes(self,pageSize = None, startIndex = None, responseFields = None):
		""" 
		
		Args:
			| pageSize (int) - 
			| startIndex (int) - 
			| responseFields (string) - 
		
		Returns:
			| DocumentTypeCollection 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/content/documenttypes/?pageSize={pageSize}&startIndex={startIndex}&responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("pageSize", pageSize);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("startIndex", startIndex);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getDocumentType(self,documentTypeName, responseFields = None):
		""" 
		
		Args:
			| documentTypeName (string) - The name of the document type to retrieve.
			| responseFields (string) - 
		
		Returns:
			| DocumentType 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/content/documenttypes/{documentTypeName}?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("documentTypeName", documentTypeName);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def createDocumentType(self,documentType, responseFields = None):
		""" 
		
		Args:
			| documentType(documentType) - 
			| responseFields (string) - 
		
		Returns:
			| DocumentType 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/content/documenttypes/?responseFields={responseFields}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(documentType).execute();
		return self.client.result();

	
		
	def updateDocumentType(self,documentType, documentTypeName, responseFields = None):
		""" 
		
		Args:
			| documentType(documentType) - 
			| documentTypeName (string) - 
			| responseFields (string) - 
		
		Returns:
			| DocumentType 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/content/documenttypes/{documentTypeName}?responseFields={responseFields}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("documentTypeName", documentTypeName);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(documentType).execute();
		return self.client.result();

	
	
	