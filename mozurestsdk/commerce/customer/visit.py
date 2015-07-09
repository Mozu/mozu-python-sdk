
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class Visit(object):
	def __init__(self, apiContext: ApiContext = None, mozuClient = None):
		self.client = mozuClient or default_client();
		if (apiContext is not None):
			self.client.withApiContext(apiContext);
		else:
			self.client.withApiContext(ApiContext());
	
	def getVisits(self,startIndex = None, pageSize = None, sortBy = None, filter = None, responseFields = None):
		""" Retrieves a list of customer visits according to any filter or sort criteria specified in the request.
		
		Args:
			| startIndex (int) - When creating paged results from a query, this value indicates the zero-based offset in the complete result set where the returned entities begin. For example, with a PageSize of 25, to get the 51st through the 75th items, use startIndex=3.
			| pageSize (int) - The number of results to display on each page when creating paged results from a query. The maximum value is 200.
			| sortBy (string) - The property by which to sort results and whether the results appear in ascending (a-z) order, represented by ASC or in descending (z-a) order, represented by DESC. The sortBy parameter follows an available property. For example: "sortBy=productCode+asc"
			| filter (string) - A set of expressions that consist of a field, operator, and value and represent search parameter syntax when filtering results of a query. Valid operators include equals (eq), does not equal (ne), greater than (gt), less than (lt), greater than or equal to (ge), less than or equal to (le), starts with (sw), or contains (cont). For example - "filter=IsDisplayed+eq+true"
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| VisitCollection 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/customer/visits/?startIndex={startIndex}&pageSize={pageSize}&sortBy={sortBy}&filter={filter}&responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("filter", filter);
		url.formatUrl("pageSize", pageSize);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("sortBy", sortBy);
		url.formatUrl("startIndex", startIndex);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getVisit(self,visitId, responseFields = None):
		""" Retrieves the details of the customer visit specified in the request.
		
		Args:
			| visitId (string) - Unique identifier of the customer visit to update.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| Visit 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/customer/visits/{visitId}?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("visitId", visitId);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def addVisit(self,visit, responseFields = None):
		""" Creates a new visit for the customer account specified in the request.
		
		Args:
			| visit(visit) - Properties of a customer visit to one of a company's sites.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| Visit 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/customer/visits/?responseFields={responseFields}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(visit).execute();
		return self.client.result();

	
		
	def updateVisit(self,visit, visitId, responseFields = None):
		""" Updates one or more properties of a defined customer visit.
		
		Args:
			| visit(visit) - Properties of a customer visit to one of a company's sites.
			| visitId (string) - Unique identifier of the customer visit to update.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| Visit 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/customer/visits/{visitId}?responseFields={responseFields}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("visitId", visitId);
		self.client.withResourceUrl(url).withBody(visit).execute();
		return self.client.result();

	
	
	