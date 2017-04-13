
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class CarrierConfiguration(object):
	def __init__(self, apiContext: ApiContext = None, mozuClient = None):
		self.client = mozuClient or default_client();
		if (apiContext is not None):
			self.client.withApiContext(apiContext);
		else:
			self.client.withApiContext(ApiContext());
	
	def getConfigurations(self,startIndex = None, pageSize = None, sortBy = None, filter = None, responseFields = None):
		""" Retrieves a list of carrier configurations and their details according to any specified facets, filter criteria, and sort options.
		
		Args:
			| startIndex (int) - When creating paged results from a query, this value indicates the zero-based offset in the complete result set where the returned entities begin. For example, with pageSize set to 25, to get the 51st through the 75th items, set this parameter to 50.
			| pageSize (int) - When creating paged results from a query, this value indicates the zero-based offset in the complete result set where the returned entities begin. For example, with this parameter set to 25, to get the 51st through the 75th items, set startIndex to 50.
			| sortBy (string) - The element to sort the results by and the channel in which the results appear. Either ascending (a-z) or descending (z-a) channel. Optional. Refer to [Sorting and Filtering](../../../../Developer/api-guides/sorting-filtering.htm) for more information.
			| filter (string) - A set of filter expressions representing the search parameters for a query. This parameter is optional. Refer to [Sorting and Filtering](../../../../Developer/api-guides/sorting-filtering.htm) for a list of supported filters.
			| responseFields (string) - Filtering syntax appended to an API call to increase or decrease the amount of data returned inside a JSON object. This parameter should only be used to retrieve data. Attempting to update data using this parameter may cause data loss.
		
		Returns:
			| CarrierConfigurationCollection 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/shipping/admin/carriers/?startIndex={startIndex}&pageSize={pageSize}&sortBy={sortBy}&filter={filter}&responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("filter", filter);
		url.formatUrl("pageSize", pageSize);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("sortBy", sortBy);
		url.formatUrl("startIndex", startIndex);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getConfiguration(self,carrierId, responseFields = None):
		""" Retrieves the details of the specified carrier configuration.
		
		Args:
			| carrierId (string) - The unique identifier of the carrier.
			| responseFields (string) - Filtering syntax appended to an API call to increase or decrease the amount of data returned inside a JSON object. This parameter should only be used to retrieve data. Attempting to update data using this parameter may cause data loss.
		
		Returns:
			| CarrierConfiguration 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/shipping/admin/carriers/{carrierId}?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("carrierId", carrierId);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def createConfiguration(self,carrierConfiguration, carrierId, responseFields = None):
		""" Creates a new carrier configuration.
		
		Args:
			| carrierConfiguration(carrierConfiguration) - Properties of a carrier configured in the shipping admin.
			| carrierId (string) - The unique identifier of the carrier.
			| responseFields (string) - Filtering syntax appended to an API call to increase or decrease the amount of data returned inside a JSON object. This parameter should only be used to retrieve data. Attempting to update data using this parameter may cause data loss.
		
		Returns:
			| CarrierConfiguration 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/shipping/admin/carriers/{carrierId}?responseFields={responseFields}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("carrierId", carrierId);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(carrierConfiguration).execute();
		return self.client.result();

	
		
	def updateConfiguration(self,carrierConfiguration, carrierId, responseFields = None):
		""" Updates the details of the specified carrier configuration.
		
		Args:
			| carrierConfiguration(carrierConfiguration) - Properties of a carrier configured in the shipping admin.
			| carrierId (string) - The unique identifier of the carrier.
			| responseFields (string) - Filtering syntax appended to an API call to increase or decrease the amount of data returned inside a JSON object. This parameter should only be used to retrieve data. Attempting to update data using this parameter may cause data loss.
		
		Returns:
			| CarrierConfiguration 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/shipping/admin/carriers/{carrierId}?responseFields={responseFields}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("carrierId", carrierId);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(carrierConfiguration).execute();
		return self.client.result();

	
		
	def deleteConfiguration(self,carrierId):
		""" Deletes the specified carrier configuration.
		
		Args:
			| carrierId (string) - The unique identifier of the carrier configuration.
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/shipping/admin/carriers/{carrierId}", "DELETE", UrlLocation.TenantPod, False);
		url.formatUrl("carrierId", carrierId);
		self.client.withResourceUrl(url).execute();

	
	
	