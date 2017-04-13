
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class TargetRule(object):
	def __init__(self, apiContext: ApiContext = None, mozuClient = None):
		self.client = mozuClient or default_client();
		if (apiContext is not None):
			self.client.withApiContext(apiContext);
		else:
			self.client.withApiContext(ApiContext());
	
	def getTargetRules(self,startIndex = None, pageSize = None, sortBy = None, filter = None, responseFields = None):
		""" Retrieves a list of target rules and their details according to any specified facets, filter criteria, and sort options.
		
		Args:
			| startIndex (int) - When creating paged results from a query, this value indicates the zero-based offset in the complete result set where the returned entities begin. For example, with pageSize set to 25, to get the 51st through the 75th items, set this parameter to 50.
			| pageSize (int) - When creating paged results from a query, this value indicates the zero-based offset in the complete result set where the returned entities begin. For example, with this parameter set to 25, to get the 51st through the 75th items, set startIndex to 50.
			| sortBy (string) - The element to sort the results by and the channel in which the results appear. Either ascending (a-z) or descending (z-a) channel. Optional. Refer to [Sorting and Filtering](../../../../Developer/api-guides/sorting-filtering.htm) for more information.
			| filter (string) - A set of filter expressions representing the search parameters for a query. This parameter is optional. Refer to [Sorting and Filtering](../../../../Developer/api-guides/sorting-filtering.htm) for a list of supported filters.
			| responseFields (string) - Filtering syntax appended to an API call to increase or decrease the amount of data returned inside a JSON object. This parameter should only be used to retrieve data. Attempting to update data using this parameter may cause data loss.
		
		Returns:
			| TargetRuleCollection 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/targetrules/?startIndex={startIndex}&pageSize={pageSize}&sortBy={sortBy}&filter={filter}&responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("filter", filter);
		url.formatUrl("pageSize", pageSize);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("sortBy", sortBy);
		url.formatUrl("startIndex", startIndex);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getTargetRule(self,code, responseFields = None):
		""" Retrieves the details of the specified target rule.
		
		Args:
			| code (string) - User-defined code that uniqely identifies the channel group.
			| responseFields (string) - Filtering syntax appended to an API call to increase or decrease the amount of data returned inside a JSON object. This parameter should only be used to retrieve data. Attempting to update data using this parameter may cause data loss.
		
		Returns:
			| TargetRule 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/targetrules/{code}?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("code", code);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def createTargetRule(self,targetRule, responseFields = None):
		""" Creates a new target rule.
		
		Args:
			| targetRule(targetRule) - The details of the new target rule.
			| responseFields (string) - Filtering syntax appended to an API call to increase or decrease the amount of data returned inside a JSON object. This parameter should only be used to retrieve data. Attempting to update data using this parameter may cause data loss.
		
		Returns:
			| TargetRule 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/targetrules/?responseFields={responseFields}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(targetRule).execute();
		return self.client.result();

	
		
	def validateTargetRule(self,targetRule):
		""" Validates the details of a target rule.
		
		Args:
			| targetRule(targetRule) - The details of the target rule you want to validate.
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/targetrules/validate", "POST", UrlLocation.TenantPod, False);
		self.client.withResourceUrl(url).withBody(targetRule).execute();

	
		
	def updateTargetRule(self,targetRule, code, responseFields = None):
		""" Updates the details of the specified target rule.
		
		Args:
			| targetRule(targetRule) - The details of the updated target rule.
			| code (string) - User-defined code that uniqely identifies the channel group.
			| responseFields (string) - Filtering syntax appended to an API call to increase or decrease the amount of data returned inside a JSON object. This parameter should only be used to retrieve data. Attempting to update data using this parameter may cause data loss.
		
		Returns:
			| TargetRule 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/targetrules/{code}?responseFields={responseFields}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("code", code);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(targetRule).execute();
		return self.client.result();

	
		
	def deleteTargetRule(self,code):
		""" Deletes the specified target rule.
		
		Args:
			| code (string) - User-defined code that uniqely identifies the channel group.
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/targetrules/{code}", "DELETE", UrlLocation.TenantPod, False);
		url.formatUrl("code", code);
		self.client.withResourceUrl(url).execute();

	
	
	