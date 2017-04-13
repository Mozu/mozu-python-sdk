
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class Product(object):
	def __init__(self, apiContext: ApiContext = None, dataViewMode="Live", mozuClient = None):
		if (apiContext is not None and apiContext.dataViewMode is None):
			apiContext.dataViewMode = dataViewMode;
		else:
			apiContext = ApiContext(dataViewMode = dataViewMode);
		self.client = mozuClient or default_client();
		self.client.withApiContext(apiContext);
	
	def getProducts(self,startIndex = None, pageSize = None, sortBy = None, filter = None, q = None, qLimit = None, noCount = False, responseFields = None):
		""" Retrieves a list of products according to any specified facets, filter criteria, and sort options.
		
		Args:
			| startIndex (int) - 
			| pageSize (int) - The number of results to display on each page when creating paged results from a query. The maximum value is 200.
			| sortBy (string) - 
			| filter (string) - A set of expressions that consist of a field, operator, and value and represent search parameter syntax when filtering results of a query. Valid operators include equals (eq), does not equal (ne), greater than (gt), less than (lt), greater than or equal to (ge), less than or equal to (le), starts with (sw), or contains (cont). For example - "filter=IsDisplayed+eq+true"
			| q (string) - A list of order search terms (not phrases) to use in the query when searching across order number and the name or email of the billing contact. When entering, separate multiple search terms with a space character.
			| qLimit (int) - The maximum number of search results to return in the response. You can limit any range between 1-100.
			| noCount (bool) - If true, the operation does not return the TotalCount number of results.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| ProductCollection 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/products/?startIndex={startIndex}&pageSize={pageSize}&sortBy={sortBy}&filter={filter}&q={q}&qLimit={qLimit}&noCount={noCount}&responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("filter", filter);
		url.formatUrl("noCount", noCount);
		url.formatUrl("pageSize", pageSize);
		url.formatUrl("q", q);
		url.formatUrl("qLimit", qLimit);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("sortBy", sortBy);
		url.formatUrl("startIndex", startIndex);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getProductInCatalogs(self,productCode):
		""" Retrieves a product that is associated with one or more specific catalogs.
		
		Args:
			| productCode (string) - Merchant-created code that uniquely identifies the product such as a SKU or item number. Once created, the product code is read-only.
		
		Returns:
			| array of ProductInCatalogInfo 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/products/{productCode}/ProductInCatalogs", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("productCode", productCode);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getProductInCatalog(self,productCode, catalogId, responseFields = None):
		""" Retrieves the details of a product associated with a specific catalog.
		
		Args:
			| productCode (string) - Merchant-created code that uniquely identifies the product such as a SKU or item number. Once created, the product code is read-only.
			| catalogId (int) - The unique identifier of the catalog of products used by a site.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| ProductInCatalogInfo 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/products/{productCode}/ProductInCatalogs/{catalogId}?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("catalogId", catalogId);
		url.formatUrl("productCode", productCode);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getProduct(self,productCode, responseFields = None):
		""" Retrieves the details of a product definition.
		
		Args:
			| productCode (string) - Merchant-created code that uniquely identifies the product such as a SKU or item number. Once created, the product code is read-only.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| Product 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/products/{productCode}?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("productCode", productCode);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def addProduct(self,product, responseFields = None):
		""" Creates a new product definition in the specified master catalog.
		
		Args:
			| product(product) - The properties of a product, referenced and used by carts, orders, wish lists, and returns.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| Product 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/products/?responseFields={responseFields}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(product).execute();
		return self.client.result();

	
		
	def addProductInCatalog(self,productInCatalogInfoIn, productCode, responseFields = None):
		""" Associates a new product defined in the master catalog with a specific catalog.
		
		Args:
			| productInCatalogInfoIn(productInCatalogInfoIn) - Properties of a product associated with a specific catalog.
			| productCode (string) - Merchant-created code that uniquely identifies the product such as a SKU or item number. Once created, the product code is read-only.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| ProductInCatalogInfo 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/products/{productCode}/ProductInCatalogs?responseFields={responseFields}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("productCode", productCode);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(productInCatalogInfoIn).execute();
		return self.client.result();

	
		
	def renameProductCodes(self,productCodeRenames):
		""" Performs an update to a product code by renaming or replacing the current product code with a new one.
		
		Args:
			| productCodeRenames(array|productCodeRenames) - Properties for a product code current and changed content.
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/products/Actions/RenameProductCodes", "POST", UrlLocation.TenantPod, False);
		self.client.withResourceUrl(url).withBody(productCodeRenames).execute();

	
		
	def updateProductInCatalogs(self,productInCatalogsIn, productCode):
		""" Updates the properties of a product specific to each catalog associated with the product.
		
		Args:
			| productInCatalogsIn(array|productInCatalogsIn) - Properties of a product associated with a specific catalog.
			| productCode (string) - Merchant-created code that uniquely identifies the product such as a SKU or item number. Once created, the product code is read-only.
		
		Returns:
			| array of ProductInCatalogInfo 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/products/{productCode}/ProductInCatalogs", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("productCode", productCode);
		self.client.withResourceUrl(url).withBody(productInCatalogsIn).execute();
		return self.client.result();

	
		
	def updateProductInCatalog(self,productInCatalogInfoIn, productCode, catalogId, responseFields = None):
		""" Updates one or more properties of a product associated with a specific catalog.
		
		Args:
			| productInCatalogInfoIn(productInCatalogInfoIn) - Properties of a product associated with a specific catalog.
			| productCode (string) - Merchant-created code that uniquely identifies the product such as a SKU or item number. Once created, the product code is read-only.
			| catalogId (int) - The unique identifier of the catalog of products used by a site.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| ProductInCatalogInfo 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/products/{productCode}/ProductInCatalogs/{catalogId}?responseFields={responseFields}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("catalogId", catalogId);
		url.formatUrl("productCode", productCode);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(productInCatalogInfoIn).execute();
		return self.client.result();

	
		
	def updateProduct(self,product, productCode, responseFields = None):
		""" Updates one or more properties of a product definition in a master catalog.
		
		Args:
			| product(product) - The properties of a product, referenced and used by carts, orders, wish lists, and returns.
			| productCode (string) - Merchant-created code that uniquely identifies the product such as a SKU or item number. Once created, the product code is read-only.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| Product 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/products/{productCode}?responseFields={responseFields}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("productCode", productCode);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(product).execute();
		return self.client.result();

	
		
	def deleteProduct(self,productCode):
		""" Deletes the specified product from a master catalog.
		
		Args:
			| productCode (string) - The unique, user-defined product code of a product, used throughout  to reference and associate to a product.
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/products/{productCode}", "DELETE", UrlLocation.TenantPod, False);
		url.formatUrl("productCode", productCode);
		self.client.withResourceUrl(url).execute();

	
		
	def deleteProductInCatalog(self,productCode, catalogId):
		""" Removes the product association defined for a specific catalog.
		
		Args:
			| productCode (string) - Merchant-created code that uniquely identifies the product such as a SKU or item number. Once created, the product code is read-only.
			| catalogId (int) - The unique identifier of the catalog of products used by a site.
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/products/{productCode}/ProductInCatalogs/{catalogId}", "DELETE", UrlLocation.TenantPod, False);
		url.formatUrl("catalogId", catalogId);
		url.formatUrl("productCode", productCode);
		self.client.withResourceUrl(url).execute();

	
	
	