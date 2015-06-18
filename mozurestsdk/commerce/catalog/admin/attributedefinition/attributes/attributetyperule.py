
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class AttributeTypeRule(object):
	def __init__(self, apiContext: ApiContext = None, mozuClient = None):
		self.client = mozuClient or default_client();
		client.withApiContext(apiContext);
	
	def getAttributeTypeRules(self,startIndex = None, pageSize = None, sortBy = None, filter = None, responseFields = None):
		"""
			Retrieves a list of attribute type rules according to optional filter criteria and sort options. Attribute type rules help drive the behavior of attributes on a storefront page.
			Request Params
				string filter A set of expressions that consist of a field, operator, and value and represent search parameter syntax when filtering results of a query. Valid operators include equals (eq), does not equal (ne), greater than (gt), less than (lt), greater than or equal to (ge), less than or equal to (le), starts with (sw), or contains (cont). For example - "filter=IsDisplayed+eq+true"
				int pageSize The number of results to display on each page when creating paged results from a query. The maximum value is 200.
				string responseFields Use this field to include those fields which are not included by default.
				string sortBy 
				int startIndex 
			Response
				AttributeTypeRuleCollection 
		"""

		url = MozuUrl("/api/commerce/catalog/admin/attributedefinition/attributes/typerules/?startIndex={startIndex}&pageSize={pageSize}&sortBy={sortBy}&filter={filter}&responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("filter", filter);
		url.formatUrl("pageSize", pageSize);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("sortBy", sortBy);
		url.formatUrl("startIndex", startIndex);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
	
	