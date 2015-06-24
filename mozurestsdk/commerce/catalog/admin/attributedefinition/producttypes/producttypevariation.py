
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class ProductTypeVariation(object):
	def __init__(self, apiContext: ApiContext = None, mozuClient = None):
		self.client = mozuClient or default_client();
		client.withApiContext(apiContext);
	
	def generateProductVariations(self,productOptionsIn, productTypeId, productCode = None, startIndex = None, pageSize = None, sortBy = None, filter = None, responseFields = None):
		""" Generates the variations possible for a product associated with the product type based on the option values supplied in the request.
		
		Args:
			| productOptionsIn(array|productOptionsIn) - Properties of the product option to create such as attribute detail, fully qualified name, and list of product option values.
			| productTypeId (int) - Identifier of the product type.
			| productCode (string) - 
			| startIndex (int) - When creating paged results from a query, this value indicates the zero-based offset in the complete result set where the returned entities begin. For example, with a PageSize of 25, to get the 51st through the 75th items, use startIndex=3.
			| pageSize (int) - The number of results to display on each page when creating paged results from a query. The maximum value is 200.
			| sortBy (string) - The property by which to sort results and whether the results appear in ascending (a-z) order, represented by ASC or in descending (z-a) order, represented by DESC. The sortBy parameter follows an available property. For example: "sortBy=productCode+asc"
			| filter (string) - A set of expressions that consist of a field, operator, and value and represent search parameter syntax when filtering results of a query. Valid operators include equals (eq), does not equal (ne), greater than (gt), less than (lt), greater than or equal to (ge), less than or equal to (le), starts with (sw), or contains (cont). For example - "filter=IsDisplayed+eq+true"
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| ProductVariationPagedCollection 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/attributedefinition/producttypes/{productTypeId}/variations?productCode={productCode}&startIndex={startIndex}&pageSize={pageSize}&sortBy={sortBy}&filter={filter}&responseFields={responseFields}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("filter", filter);
		url.formatUrl("pageSize", pageSize);
		url.formatUrl("productCode", productCode);
		url.formatUrl("productTypeId", productTypeId);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("sortBy", sortBy);
		url.formatUrl("startIndex", startIndex);
		self.client.withResourceUrl(url).withBody(productOptionsIn).execute();
		return self.client.result();

	
	
	