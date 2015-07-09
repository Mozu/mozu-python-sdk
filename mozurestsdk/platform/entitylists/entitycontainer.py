
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class EntityContainer(object):
	def __init__(self, apiContext: ApiContext = None, mozuClient = None):
		self.client = mozuClient or default_client();
		if (apiContext is not None):
			self.client.withApiContext(apiContext);
		else:
			self.client.withApiContext(ApiContext());
	
	def getEntityContainer(self,entityListFullName, id, responseFields = None):
		""" Retrieves an entity container, providing all schema and rules and associated IDs for entities.
		
		Args:
			| entityListFullName (string) - The full name of the EntityList including namespace in name@nameSpace format
			| id (string) - Unique identifier of the customer segment to retrieve.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| EntityContainer 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/platform/entitylists/{entityListFullName}/entityContainers/{id}?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("entityListFullName", entityListFullName);
		url.formatUrl("id", id);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getEntityContainers(self,entityListFullName, pageSize = None, startIndex = None, filter = None, sortBy = None, responseFields = None):
		""" Retrieves a collection of entity containers. Each container holds a set of entities per ID. 
		
		Args:
			| entityListFullName (string) - The full name of the EntityList including namespace in name@nameSpace format
			| pageSize (int) - The number of results to display on each page when creating paged results from a query. The amount is divided and displayed on the  pageCount  amount of pages. The default is 20 and maximum value is 200 per page.
			| startIndex (int) - When creating paged results from a query, this value indicates the zero-based offset in the complete result set where the returned entities begin. For example, with a  pageSize  of 25, to get the 51st through the 75th items, use  startIndex=3 .
			| filter (string) - A set of expressions that consist of a field, operator, and value and represent search parameter syntax when filtering results of a query. Valid operators include equals (eq), does not equal (ne), greater than (gt), less than (lt), greater than or equal to (ge), less than or equal to (le), starts with (sw), or contains (cont). For example - "filter=IsDisplayed+eq+true"
			| sortBy (string) - The element to sort the results by and the channel in which the results appear. Either ascending (a-z) or descending (z-a) channel. Optional.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| EntityContainerCollection 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/platform/entitylists/{entityListFullName}/entityContainers?pageSize={pageSize}&startIndex={startIndex}&filter={filter}&sortBy={sortBy}&responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("entityListFullName", entityListFullName);
		url.formatUrl("filter", filter);
		url.formatUrl("pageSize", pageSize);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("sortBy", sortBy);
		url.formatUrl("startIndex", startIndex);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
	
	