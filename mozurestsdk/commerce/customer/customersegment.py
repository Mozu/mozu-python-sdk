
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class CustomerSegment(object):
	def __init__(self, apiContext: ApiContext = None, mozuClient = None):
		self.client = mozuClient or default_client();
		client.withApiContext(apiContext);
	
	def getSegments(self,startIndex = None, pageSize = None, sortBy = None, filter = None, responseFields = None):
		"""
			Retrieves a list of defined customer segments according to any filter and sort criteria.
			Request Params
				string filter A set of expressions that consist of a field, operator, and value and represent search parameter syntax when filtering results of a query. Valid operators include equals (eq), does not equal (ne), greater than (gt), less than (lt), greater than or equal to (ge), less than or equal to (le), starts with (sw), or contains (cont). For example - "filter=IsDisplayed+eq+true"
				int pageSize The number of results to display on each page when creating paged results from a query. The maximum value is 200.
				string responseFields Use this field to include those fields which are not included by default.
				string sortBy The property by which to sort results and whether the results appear in ascending (a-z) order, represented by ASC or in descending (z-a) order, represented by DESC. The sortBy parameter follows an available property. For example: "sortBy=productCode+asc"
				int startIndex When creating paged results from a query, this value indicates the zero-based offset in the complete result set where the returned entities begin. For example, with a PageSize of 25, to get the 51st through the 75th items, use startIndex=3.
			Response
				CustomerSegmentCollection 
		"""

		url = MozuUrl("/api/commerce/customer/segments/?startIndex={startIndex}&pageSize={pageSize}&sortBy={sortBy}&filter={filter}&responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("filter", filter);
		url.formatUrl("pageSize", pageSize);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("sortBy", sortBy);
		url.formatUrl("startIndex", startIndex);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getSegment(self,id, responseFields = None):
		"""
			Retrieves the details of the customer segment specified in the request. This operation does not return a list of the customer accounts associated with the segment.
			Request Params
				int id Unique identifier of the customer segment to retrieve.
				string responseFields Use this field to include those fields which are not included by default.
			Response
				CustomerSegment 
		"""

		url = MozuUrl("/api/commerce/customer/segments/{id}?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("id", id);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def addSegment(self,segment, responseFields = None):
		"""
			Creates a new customer segments. New customer segments do not have any associated customer accounts.
			Request Params
				string responseFields Use this field to include those fields which are not included by default.
				segment The Customer Segment object includes properties of a defined customer segment used to group customer accounts.
			Response
				CustomerSegment 
		"""

		url = MozuUrl("/api/commerce/customer/segments/?responseFields={responseFields}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def addSegmentAccounts(self,accountIds, id):
		"""
			Adds one or more customer accounts to a defined customer segment.
			Request Params
				int id Unique identifier of the customer segment to retrieve.
				array|accountIds List of customer account IDs to add to the customer segment specified in the request.
			Response
		"""

		url = MozuUrl("/api/commerce/customer/segments/{id}/accounts", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("id", id);
		self.client.withResourceUrl(url).execute();

	
		
	def updateSegment(self,segment, id, responseFields = None):
		"""
			Updates the details of the customer segment specified in the request.
			Request Params
				int id Unique identifier of the customer segment to retrieve.
				string responseFields Use this field to include those fields which are not included by default.
				segment The Customer Segment object includes properties of a defined customer segment used to group customer accounts.
			Response
				CustomerSegment 
		"""

		url = MozuUrl("/api/commerce/customer/segments/{id}?responseFields={responseFields}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("id", id);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def deleteSegment(self,id):
		"""
			Deletes a customer segment specified by its unique identifier. Deleting a segment removes any customer account associations, but does not delete the customer account itself.
			Request Params
				int id Unique identifier of the customer segment to retrieve.
			Response
		"""

		url = MozuUrl("/api/commerce/customer/segments/{id}", "DELETE", UrlLocation.TenantPod, False);
		url.formatUrl("id", id);
		self.client.withResourceUrl(url).execute();

	
		
	def removeSegmentAccount(self,id, accountId):
		"""
			Removes single account from a segment.
			Request Params
				int accountId Unique identifier of the customer account.
				int id Unique identifier of the customer segment to retrieve.
			Response
		"""

		url = MozuUrl("/api/commerce/customer/segments/{id}/accounts/{accountId}", "DELETE", UrlLocation.TenantPod, False);
		url.formatUrl("accountId", accountId);
		url.formatUrl("id", id);
		self.client.withResourceUrl(url).execute();

	
	
	