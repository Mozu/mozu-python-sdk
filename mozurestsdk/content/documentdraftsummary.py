
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class DocumentDraftSummary(object):
	def __init__(self, apiContext: ApiContext = None, mozuClient = None):
		self.client = mozuClient or default_client();
		if (apiContext is not None):
			self.client.withApiContext(apiContext);
		else:
			self.client.withApiContext(ApiContext());
	
	def listDocumentDraftSummaries(self,pageSize = None, startIndex = None, documentLists = None, responseFields = None):
		""" 
		
		Args:
			| pageSize (int) - 
			| startIndex (int) - 
			| documentLists (string) - Lists that contain the document drafts.
			| responseFields (string) - 
		
		Returns:
			| DocumentDraftSummaryPagedCollection 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/content/documentpublishing/draft?pageSize={pageSize}&startIndex={startIndex}&documentLists={documentLists}&responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("documentLists", documentLists);
		url.formatUrl("pageSize", pageSize);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("startIndex", startIndex);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def deleteDocumentDrafts(self,documentIds, documentLists = None):
		""" 
		
		Args:
			| documentIds(array|documentIds) - Unique identifiers of the documents to delete.
			| documentLists (string) - List of document lists that contain documents to delete.
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/content/documentpublishing/draft?documentLists={documentLists}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("documentLists", documentLists);
		self.client.withResourceUrl(url).withBody(documentIds).execute();

	
		
	def publishDocuments(self,documentIds, documentLists = None):
		""" 
		
		Args:
			| documentIds(array|documentIds) - List of unique identifiers of the document drafts to publish.
			| documentLists (string) - List of document lists that contain documents to publish.
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/content/documentpublishing/active?documentLists={documentLists}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("documentLists", documentLists);
		self.client.withResourceUrl(url).withBody(documentIds).execute();

	
	
	