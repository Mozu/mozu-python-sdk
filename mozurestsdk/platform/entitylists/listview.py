
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class ListView(object):
	def __init__(self, apiContext: ApiContext = None, mozuClient = None):
		self.client = mozuClient or default_client();
		if (apiContext is not None):
			self.client.withApiContext(apiContext);
		else:
			self.client.withApiContext(ApiContext());
	
	def getViewEntity(self,entityListFullName, viewName, entityId, responseFields = None):
		""" Retrieves a view for associated entities. A view provides display context levels (site, tenant, catalog, master catalog) and settings.
		
		Args:
			| entityListFullName (string) - The full name of the EntityList including namespace in name@nameSpace format
			| viewName (string) - The name for a view. Views are used to render data in , such as document and entity lists. Each view includes a schema, format, name, ID, and associated data types to render.
			| entityId (string) - Unique identifier for an entity, which defines the schema, rules, and formats for JSON entities within the MZDB ( Mongo DB).
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| JObject 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/platform/entitylists/{entityListFullName}/views/{viewName}/entities/{entityId}?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("entityId", entityId);
		url.formatUrl("entityListFullName", entityListFullName);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("viewName", viewName);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getViewEntities(self,entityListFullName, viewName, pageSize = None, startIndex = None, filter = None, responseFields = None):
		""" Retrieves a collection of views for associated entities. Each view provides display context levels (site, tenant, catalog, master catalog) and settings.
		
		Args:
			| entityListFullName (string) - The full name of the EntityList including namespace in name@nameSpace format
			| viewName (string) - The name for a view. Views are used to render data in , such as document and entity lists. Each view includes a schema, format, name, ID, and associated data types to render.
			| pageSize (int) - When creating paged results from a query, this value indicates the zero-based offset in the complete result set where the returned entities begin. For example, with this parameter set to 25, to get the 51st through the 75th items, set startIndex to 50.
			| startIndex (int) - When creating paged results from a query, this value indicates the zero-based offset in the complete result set where the returned entities begin. For example, with pageSize set to 25, to get the 51st through the 75th items, set this parameter to 50.
			| filter (string) - A set of expressions that consist of a field, operator, and value and represent search parameter syntax when filtering results of a query. Valid operators include equals (eq), does not equal (ne), greater than (gt), less than (lt), greater than or equal to (ge), less than or equal to (le), starts with (sw), or contains (cont). For example - "filter=IsDisplayed+eq+true"
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| EntityCollection 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/platform/entitylists/{entityListFullName}/views/{viewName}/entities?pageSize={pageSize}&startIndex={startIndex}&filter={filter}&responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("entityListFullName", entityListFullName);
		url.formatUrl("filter", filter);
		url.formatUrl("pageSize", pageSize);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("startIndex", startIndex);
		url.formatUrl("viewName", viewName);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getViewEntityContainer(self,entityListFullName, viewName, entityId, responseFields = None):
		""" Retrieves a collection of container data for creating and displaying a view of entities. 
		
		Args:
			| entityListFullName (string) - The full name of the EntityList including namespace in name@nameSpace format
			| viewName (string) - The name for a view. Views are used to render data in , such as document and entity lists. Each view includes a schema, format, name, ID, and associated data types to render.
			| entityId (string) - Unique identifier for an entity, which defines the schema, rules, and formats for JSON entities within the MZDB ( Mongo DB).
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| EntityContainer 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/platform/entitylists/{entityListFullName}/views/{viewName}/entityContainers/{entityId}?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("entityId", entityId);
		url.formatUrl("entityListFullName", entityListFullName);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("viewName", viewName);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getViewEntityContainers(self,entityListFullName, viewName, pageSize = None, startIndex = None, filter = None, responseFields = None):
		""" Retrieves a collection of container data for creating and displaying a view of entities. 
		
		Args:
			| entityListFullName (string) - The full name of the EntityList including namespace in name@nameSpace format
			| viewName (string) - The name for a view. Views are used to render data in , such as document and entity lists. Each view includes a schema, format, name, ID, and associated data types to render.
			| pageSize (int) - When creating paged results from a query, this value indicates the zero-based offset in the complete result set where the returned entities begin. For example, with this parameter set to 25, to get the 51st through the 75th items, set startIndex to 50.
			| startIndex (int) - When creating paged results from a query, this value indicates the zero-based offset in the complete result set where the returned entities begin. For example, with pageSize set to 25, to get the 51st through the 75th items, set this parameter to 50.
			| filter (string) - A set of expressions that consist of a field, operator, and value and represent search parameter syntax when filtering results of a query. Valid operators include equals (eq), does not equal (ne), greater than (gt), less than (lt), greater than or equal to (ge), less than or equal to (le), starts with (sw), or contains (cont). For example - "filter=IsDisplayed+eq+true"
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| EntityContainerCollection 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/platform/entitylists/{entityListFullName}/views/{viewName}/entityContainers?pageSize={pageSize}&startIndex={startIndex}&filter={filter}&responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("entityListFullName", entityListFullName);
		url.formatUrl("filter", filter);
		url.formatUrl("pageSize", pageSize);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("startIndex", startIndex);
		url.formatUrl("viewName", viewName);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getEntityListView(self,entityListFullName, viewName, responseFields = None):
		""" Retrieves a specific  EntityListView . These views provide schema, rules, and formatting for all associated entities. 
		
		Args:
			| entityListFullName (string) - The full name of the EntityList including namespace in name@nameSpace format
			| viewName (string) - The name for a view. Views are used to render data in , such as document and entity lists. Each view includes a schema, format, name, ID, and associated data types to render.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| ListView 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/platform/entitylists/{entityListFullName}/views/{viewName}?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("entityListFullName", entityListFullName);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("viewName", viewName);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getEntityListViews(self,entityListFullName, responseFields = None):
		""" Retrieves a collection of  EntityListViews . These views provide schema, rules, and formatting for all associated entities. 
		
		Args:
			| entityListFullName (string) - The full name of the EntityList including namespace in name@nameSpace format
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| ListViewCollection 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/platform/entitylists/{entityListFullName}/views?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("entityListFullName", entityListFullName);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def createEntityListView(self,listView, entityListFullName, responseFields = None):
		""" Creates an entity list view. Each view provides display context levels (site, tenant, catalog, master catalog) and settings for the list of entities.
		
		Args:
			| listView(listView) - Properties for the list view that specifies what fields and content display per page load. All associated fields in the list view correspond with object data.
			| entityListFullName (string) - The full name of the EntityList including namespace in name@nameSpace format
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| ListView 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/platform/entitylists/{entityListFullName}/views/?responseFields={responseFields}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("entityListFullName", entityListFullName);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(listView).execute();
		return self.client.result();

	
		
	def updateEntityListView(self,listView, entityListFullName, viewName, responseFields = None):
		""" Updates an existing entity list view. Each view provides display context levels (site, tenant, catalog, master catalog) and settings for the list of entities.
		
		Args:
			| listView(listView) - Properties for the list view that specifies what fields and content display per page load. All associated fields in the list view correspond with object data.
			| entityListFullName (string) - The full name of the EntityList including namespace in name@nameSpace format
			| viewName (string) - The name for a view. Views are used to render data in , such as document and entity lists. Each view includes a schema, format, name, ID, and associated data types to render.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| ListView 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/platform/entitylists/{entityListFullName}/views/{viewName}?responseFields={responseFields}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("entityListFullName", entityListFullName);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("viewName", viewName);
		self.client.withResourceUrl(url).withBody(listView).execute();
		return self.client.result();

	
		
	def deleteEntityListView(self,entityListFullName, viewName):
		""" Deletes an entity list view. Any associated entities have the association removed.
		
		Args:
			| entityListFullName (string) - The full name of the EntityList including namespace in name@nameSpace format
			| viewName (string) - The name for a view. Views are used to render data in , such as document and entity lists. Each view includes a schema, format, name, ID, and associated data types to render.
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/platform/entitylists/{entityListFullName}/views/{viewName}", "DELETE", UrlLocation.TenantPod, False);
		url.formatUrl("entityListFullName", entityListFullName);
		url.formatUrl("viewName", viewName);
		self.client.withResourceUrl(url).execute();

	
	
	