
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class Package(object):
	def __init__(self, apiContext: ApiContext = None, mozuClient = None):
		self.client = mozuClient or default_client();
		if (apiContext is not None):
			self.client.withApiContext(apiContext);
		else:
			self.client.withApiContext(ApiContext());
	
	def getAvailablePackageFulfillmentActions(self,orderId, packageId):
		""" Retrieves a list of the actions available to perform for a package associated with order fulfillment.
		
		Args:
			| orderId (string) - Unique identifier of the order.
			| packageId (string) - Unique identifier of the package for which to retrieve the label.
		
		Returns:
			| array of string 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/orders/{orderId}/packages/{packageId}/actions", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("orderId", orderId);
		url.formatUrl("packageId", packageId);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getPackageLabel(self,orderId, packageId):
		""" Retrieves the package label image supplied by the carrier.
		
		Args:
			| orderId (string) - Unique identifier of the order.
			| packageId (string) - Unique identifier of the package for which to retrieve the label.
		
		Returns:
			| Stream 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/orders/{orderId}/packages/{packageId}/label", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("orderId", orderId);
		url.formatUrl("packageId", packageId);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getPackage(self,orderId, packageId, responseFields = None):
		""" Retrieves the details of a package of order items.
		
		Args:
			| orderId (string) - Unique identifier of the order.
			| packageId (string) - Unique identifier of the package for which to retrieve the label.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| Package 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/orders/{orderId}/packages/{packageId}?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("orderId", orderId);
		url.formatUrl("packageId", packageId);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def createPackage(self,package, orderId, responseFields = None):
		""" Creates a new physical package of order items.
		
		Args:
			| package(package) - Properties of a physical package shipped for an order.
			| orderId (string) - Unique identifier of the order.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| Package 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/orders/{orderId}/packages?responseFields={responseFields}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("orderId", orderId);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(package).execute();
		return self.client.result();

	
		
	def updatePackage(self,package, orderId, packageId, responseFields = None):
		""" Updates one or more properties of a physical package of order items.
		
		Args:
			| package(package) - Properties of a physical package shipped for an order.
			| orderId (string) - Unique identifier of the order.
			| packageId (string) - Unique identifier of the package for which to retrieve the label.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| Package 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/orders/{orderId}/packages/{packageId}?responseFields={responseFields}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("orderId", orderId);
		url.formatUrl("packageId", packageId);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(package).execute();
		return self.client.result();

	
		
	def deletePackage(self,orderId, packageId):
		""" Removes a physical package of items from the specified order.
		
		Args:
			| orderId (string) - Unique identifier of the order.
			| packageId (string) - Unique identifier of the package for which to retrieve the label.
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/orders/{orderId}/packages/{packageId}", "DELETE", UrlLocation.TenantPod, False);
		url.formatUrl("orderId", orderId);
		url.formatUrl("packageId", packageId);
		self.client.withResourceUrl(url).execute();

	
	
	