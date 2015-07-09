
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
		""" Retrieves a list of the documents currently in draft state, according to any defined filter and sort criteria.
		
		Args:
			| pageSize (int) - The number of results to display on each page when creating paged results from a query. The maximum value is 200.
			| startIndex (int) - When creating paged results from a query, this value indicates the zero-based offset in the complete result set where the returned entities begin. For example, with a PageSize of 25, to get the 51st through the 75th items, use startIndex=3.
			| documentLists (string) - List of document lists that contain documents to delete.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
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
		""" Deletes the drafts of the specified documents. Published documents cannot be deleted.
		
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
		""" Publish one or more document drafts to live content on the site.
		
		Args:
			| documentIds(array|documentIds) - Unique identifiers of the documents to delete.
			| documentLists (string) - List of document lists that contain documents to delete.
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/content/documentpublishing/active?documentLists={documentLists}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("documentLists", documentLists);
		self.client.withResourceUrl(url).withBody(documentIds).execute();

	
	
	