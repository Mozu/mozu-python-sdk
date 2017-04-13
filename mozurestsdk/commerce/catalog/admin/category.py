
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class Category(object):
	def __init__(self, apiContext: ApiContext = None, dataViewMode="Live", mozuClient = None):
		if (apiContext is not None and apiContext.dataViewMode is None):
			apiContext.dataViewMode = dataViewMode;
		else:
			apiContext = ApiContext(dataViewMode = dataViewMode);
		self.client = mozuClient or default_client();
		self.client.withApiContext(apiContext);
	
	def getCategories(self,startIndex = None, pageSize = None, sortBy = None, filter = None, responseFields = None):
		""" Retrieves a list of categories according to any specified filter criteria and sort options.
		
		Args:
			| startIndex (int) - 
			| pageSize (int) - The number of results to display on each page when creating paged results from a query. The maximum value is 200.
			| sortBy (string) - 
			| filter (string) - A set of filter expressions representing the search parameters for a query. This parameter is optional. Refer to [Sorting and Filtering](../../../../Developer/api-guides/sorting-filtering.htm) for a list of supported filters.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| CategoryPagedCollection 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/categories/?startIndex={startIndex}&pageSize={pageSize}&sortBy={sortBy}&filter={filter}&responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("filter", filter);
		url.formatUrl("pageSize", pageSize);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("sortBy", sortBy);
		url.formatUrl("startIndex", startIndex);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getChildCategories(self,categoryId, responseFields = None):
		""" Retrieves the list of subcategories within a category.
		
		Args:
			| categoryId (int) - Unique identifier of the category to modify.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| CategoryCollection 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/categories/{categoryId}/children?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("categoryId", categoryId);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getCategory(self,categoryId, responseFields = None):
		""" Retrieves the details of a single category.
		
		Args:
			| categoryId (int) - Unique identifier of the category to modify.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| Category 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/categories/{categoryId}?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("categoryId", categoryId);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def addCategory(self,category, incrementSequence = False, useProvidedId = False, responseFields = None):
		""" Adds a new category to the site's category hierarchy.Specify a  to determine where to place the category in the hierarchy. If no  is specified, the new category is a top-level category.
		
		Args:
			| category(category) - A descriptive container that groups products. A category is merchant defined with associated products and discounts as configured. GThe storefront displays products in a hierarchy of categories. As such, categories can include a nesting of sub-categories to organize products and product options per set guidelines such as color, brand, material, and size.
			| incrementSequence (bool) - If true, when adding a new product category, set the sequence number of the new category to an increment of one integer greater than the maximum available sequence number across all product categories. If false, set the sequence number to zero.
			| useProvidedId (bool) - Optional. If ,  uses the  you specify in the request as the category's id. If ,  generates an  for the category regardless if you specify an id in the request.If you specify an id already in use and set this parameter to ,  returns an error.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| Category 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/categories/?incrementSequence={incrementSequence}&useProvidedId={useProvidedId}&responseFields={responseFields}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("incrementSequence", incrementSequence);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("useProvidedId", useProvidedId);
		self.client.withResourceUrl(url).withBody(category).execute();
		return self.client.result();

	
		
	def validateDynamicExpression(self,dynamicExpressionIn, responseFields = None):
		""" Validate the precomputed dynamic category expression for correctness.
		
		Args:
			| dynamicExpressionIn(dynamicExpressionIn) - The details of the dynamic expression that you want to validate.
			| responseFields (string) - Filtering syntax appended to an API call to increase or decrease the amount of data returned inside a JSON object. This parameter should only be used to retrieve data. Attempting to update data using this parameter may cause data loss.
		
		Returns:
			| DynamicExpression 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/categories/ValidateDynamicExpression?responseFields={responseFields}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(dynamicExpressionIn).execute();
		return self.client.result();

	
		
	def validateRealTimeDynamicExpression(self,dynamicExpressionIn, responseFields = None):
		""" Validates the readltime dynamic category expression for correctness.
		
		Args:
			| dynamicExpressionIn(dynamicExpressionIn) - The details of the dynamic expression that you want to validate.
			| responseFields (string) - Filtering syntax appended to an API call to increase or decrease the amount of data returned inside a JSON object. This parameter should only be used to retrieve data. Attempting to update data using this parameter may cause data loss.
		
		Returns:
			| DynamicExpression 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/categories/ValidateRealTimeDynamicExpression?responseFields={responseFields}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(dynamicExpressionIn).execute();
		return self.client.result();

	
		
	def updateCategory(self,category, categoryId, cascadeVisibility = False, responseFields = None):
		""" Update the properties of a defined category or move it to another location in the category hierarchy. Because this operation replaces the defined resource,include all the information to maintain for the category in the request.
		
		Args:
			| category(category) - A descriptive container that groups products. A category is merchant defined with associated products and discounts as configured. GThe storefront displays products in a hierarchy of categories. As such, categories can include a nesting of sub-categories to organize products and product options per set guidelines such as color, brand, material, and size.
			| categoryId (int) - Unique identifier of the category to modify.
			| cascadeVisibility (bool) - If true, when changing the display option for the category, change it for all subcategories also. The default value is false.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| Category 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/categories/{categoryId}?cascadeVisibility={cascadeVisibility}&responseFields={responseFields}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("cascadeVisibility", cascadeVisibility);
		url.formatUrl("categoryId", categoryId);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(category).execute();
		return self.client.result();

	
		
	def deleteCategoryById(self,categoryId, cascadeDelete = False, forceDelete = False, reassignToParent = False):
		""" Deletes the specified category. Use the categoryId parameter to specify the category.
		
		Args:
			| categoryId (int) - Unique identifier of the category to modify.
			| cascadeDelete (bool) - Specifies whether to also delete all subcategories associated with the specified category.If you set this value is false, only the specified category is deleted.The default value is false.
			| forceDelete (bool) - Specifies whether the category, and any associated subcategories, are deleted even if there are products that reference them. The default value is false.
			| reassignToParent (bool) - Specifies whether any subcategories of the specified category are reassigned to the parent of the specified category.This field only applies if the cascadeDelete parameter is false.The default value is false.
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/categories/{categoryId}/?cascadeDelete={cascadeDelete}&forceDelete={forceDelete}&reassignToParent={reassignToParent}", "DELETE", UrlLocation.TenantPod, False);
		url.formatUrl("cascadeDelete", cascadeDelete);
		url.formatUrl("categoryId", categoryId);
		url.formatUrl("forceDelete", forceDelete);
		url.formatUrl("reassignToParent", reassignToParent);
		self.client.withResourceUrl(url).execute();

	
	
	