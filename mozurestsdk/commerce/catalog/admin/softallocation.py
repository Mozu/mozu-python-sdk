
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class SoftAllocation(object):
	def __init__(self, apiContext: ApiContext = None, mozuClient = None):
		self.client = mozuClient or default_client();
		if (apiContext is not None):
			self.client.withApiContext(apiContext);
		else:
			self.client.withApiContext(ApiContext());
	
	def getSoftAllocations(self,startIndex = None, pageSize = None, sortBy = None, filter = None, responseFields = None):
		""" Retrieves a list of sof allocations according to any specified filter criteria and sort options.
		
		Args:
			| startIndex (int) - When creating paged results from a query, this value indicates the zero-based offset in the complete result set where the returned entities begin. For example, with pageSize set to 25, to get the 51st through the 75th items, set this parameter to 50.
			| pageSize (int) - When creating paged results from a query, this value indicates the zero-based offset in the complete result set where the returned entities begin. For example, with this parameter set to 25, to get the 51st through the 75th items, set startIndex to 50.
			| sortBy (string) - The element to sort the results by and the channel in which the results appear. Either ascending (a-z) or descending (z-a) channel. Optional. Refer to [Sorting and Filtering](../../../../Developer/api-guides/sorting-filtering.htm) for more information.
			| filter (string) - A set of filter expressions representing the search parameters for a query. This parameter is optional. Refer to [Sorting and Filtering](../../../../Developer/api-guides/sorting-filtering.htm) for a list of supported filters.
			| responseFields (string) - Filtering syntax appended to an API call to increase or decrease the amount of data returned inside a JSON object. This parameter should only be used to retrieve data. Attempting to update data using this parameter may cause data loss.
		
		Returns:
			| SoftAllocationCollection 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/softallocations/?startIndex={startIndex}&pageSize={pageSize}&sortBy={sortBy}&filter={filter}&responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("filter", filter);
		url.formatUrl("pageSize", pageSize);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("sortBy", sortBy);
		url.formatUrl("startIndex", startIndex);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getSoftAllocation(self,softAllocationId, responseFields = None):
		""" Retrieves the details of a soft allocation.
		
		Args:
			| softAllocationId (int) - The unique identifier of the soft allocation.
			| responseFields (string) - Filtering syntax appended to an API call to increase or decrease the amount of data returned inside a JSON object. This parameter should only be used to retrieve data. Attempting to update data using this parameter may cause data loss.
		
		Returns:
			| SoftAllocation 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/softallocations/{softAllocationId}?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("softAllocationId", softAllocationId);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def addSoftAllocations(self,softAllocationsIn):
		""" Creates a new soft allocation for a product. This places a hold on the product inventory for the quantity specified during the ordering process.
		
		Args:
			| softAllocationsIn(array|softAllocationsIn) - The details of the new soft allocation.
		
		Returns:
			| array of SoftAllocation 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/softallocations/", "POST", UrlLocation.TenantPod, False);
		self.client.withResourceUrl(url).withBody(softAllocationsIn).execute();
		return self.client.result();

	
		
	def convertToProductReservation(self,softAllocations):
		""" Converts a set of existing soft product allocations into product reservations.
		
		Args:
			| softAllocations(array|softAllocations) - The details of the soft allocation which you want to convert into product reservations.
		
		Returns:
			| array of ProductReservation 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/softallocations/convert", "POST", UrlLocation.TenantPod, False);
		self.client.withResourceUrl(url).withBody(softAllocations).execute();
		return self.client.result();

	
		
	def renewSoftAllocations(self,softAllocationRenew):
		""" Updates the expiration time for a set of soft allocations in a non-transactional batch.
		
		Args:
			| softAllocationRenew(softAllocationRenew) - The details of the soft allocation that you want to renew.
		
		Returns:
			| array of SoftAllocation 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/softallocations/renew", "POST", UrlLocation.TenantPod, False);
		self.client.withResourceUrl(url).withBody(softAllocationRenew).execute();
		return self.client.result();

	
		
	def updateSoftAllocations(self,softAllocations):
		""" Updates a soft allocation. This updates a hold on the product inventory for the quantity specified during the ordering process.
		
		Args:
			| softAllocations(array|softAllocations) - The details of the updated soft allocations.
		
		Returns:
			| array of SoftAllocation 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/softallocations/", "PUT", UrlLocation.TenantPod, False);
		self.client.withResourceUrl(url).withBody(softAllocations).execute();
		return self.client.result();

	
		
	def deleteSoftAllocation(self,softAllocationId):
		""" Deletes a soft allocation. You might delete a soft allocation when an order or cart is not processed in order to return the product quantity back to inventory.
		
		Args:
			| softAllocationId (int) - The unique identifier of the soft allocation.
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/catalog/admin/softallocations/{softAllocationId}", "DELETE", UrlLocation.TenantPod, False);
		url.formatUrl("softAllocationId", softAllocationId);
		self.client.withResourceUrl(url).execute();

	
	
	