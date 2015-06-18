
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class LocationInventory(object):
	def __init__(self, apiContext: ApiContext = None, dataViewMode="Live", mozuClient = None):
		if (apiContext.dataViewMode is None):
			apiContext.dataViewMode = dataViewMode;
		self.client = mozuClient or default_client();
		self.client.withApiContext(apiContext);
	
	def getLocationInventory(self,locationCode, productCode, responseFields = None):
		"""
			Retrieves the details of a product's active inventory at the location specified in the request.
			Request Params
				string locationCode The unique, user-defined code that identifies a location. 
				string productCode Merchant-created code that uniquely identifies the product such as a SKU or item number. Once created, the product code is read-only.
				string responseFields Use this field to include those fields which are not included by default.
			Response
				LocationInventory 
		"""

		url = MozuUrl("/api/commerce/catalog/admin/locationinventory/{locationCode}/{productCode}?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("locationCode", locationCode);
		url.formatUrl("productCode", productCode);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getLocationInventories(self,locationCode, startIndex = None, pageSize = None, sortBy = None, filter = None, responseFields = None):
		"""
			Retrieves a list of all product inventory definitions for the location code specified in the request.
			Request Params
				string filter A set of expressions that consist of a field, operator, and value and represent search parameter syntax when filtering results of a query. Valid operators include equals (eq), does not equal (ne), greater than (gt), less than (lt), greater than or equal to (ge), less than or equal to (le), starts with (sw), or contains (cont). For example - "filter=IsDisplayed+eq+true"
				string locationCode The unique, user-defined code that identifies a location. 
				int pageSize The number of results to display on each page when creating paged results from a query. The maximum value is 200.
				string responseFields Use this field to include those fields which are not included by default.
				string sortBy The property by which to sort results and whether the results appear in ascending (a-z) order, represented by ASC or in descending (z-a) order, represented by DESC. The sortBy parameter follows an available property. For example: "sortBy=productCode+asc"
				int startIndex When creating paged results from a query, this value indicates the zero-based offset in the complete result set where the returned entities begin. For example, with a PageSize of 25, to get the 51st through the 75th items, use startIndex=3.
			Response
				LocationInventoryCollection 
		"""

		url = MozuUrl("/api/commerce/catalog/admin/locationinventory/{locationCode}?startIndex={startIndex}&pageSize={pageSize}&sortBy={sortBy}&filter={filter}&responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("filter", filter);
		url.formatUrl("locationCode", locationCode);
		url.formatUrl("pageSize", pageSize);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("sortBy", sortBy);
		url.formatUrl("startIndex", startIndex);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def addLocationInventory(self,locationInventoryList, locationCode, performUpserts = False):
		"""
			Creates an array of product inventory definitions for the location specified in the request. When adding a new inventory definition, you must specify the productCode and stockOnHand value in each array you define. All other properties are system-supplied and read only.
			Request Params
				string locationCode The unique, user-defined code that identifies a location. 
				bool performUpserts Query string parameter lets the service perform an update for a new or existing record. When run, the update occurs without throwing a conflict exception that the record exists. If true, the updates completes regardless of the record currently existing. By default, if no value is specified, the service assumes this value is false.
				array|locationInventoryList Properties of an inventory definition that defines the level of inventory for a specific product at a given location.
			Response
				array|LocationInventory 
		"""

		url = MozuUrl("/api/commerce/catalog/admin/locationinventory/{locationCode}?performUpserts={performUpserts}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("locationCode", locationCode);
		url.formatUrl("performUpserts", performUpserts);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def updateLocationInventory(self,locationInventoryAdjustments, locationCode):
		"""
			Updates the active stock on hand inventory of products for the location code specified in the request.
			Request Params
				string locationCode The unique, user-defined code that identifies a location. 
				array|locationInventoryAdjustments Properties of an adjustment to the active product inventory of a specific location.
			Response
				array|LocationInventory 
		"""

		url = MozuUrl("/api/commerce/catalog/admin/locationinventory/{locationCode}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("locationCode", locationCode);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def deleteLocationInventory(self,locationCode, productCode):
		"""
			Deletes the product code inventory definition for the location specified in the request.
			Request Params
				string locationCode The unique, user-defined code that identifies a location. 
				string productCode Merchant-created code that uniquely identifies the product such as a SKU or item number. Once created, the product code is read-only.
			Response
		"""

		url = MozuUrl("/api/commerce/catalog/admin/locationinventory/{locationCode}/{productCode}", "DELETE", UrlLocation.TenantPod, False);
		url.formatUrl("locationCode", locationCode);
		url.formatUrl("productCode", productCode);
		self.client.withResourceUrl(url).execute();

	
	
	