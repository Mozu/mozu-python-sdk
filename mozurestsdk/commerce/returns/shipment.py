
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class Shipment(object):
	def __init__(self, apiContext: ApiContext = None, mozuClient = None):
		self.client = mozuClient or default_client();
		client.withApiContext(apiContext);
	
	def getShipment(self,returnId, shipmentId, responseFields = None):
		""" Retrieves the details of the specified return replacement shipment.
		
		Args:
			| returnId (string) - Unique identifier of the return whose items you want to get.
			| shipmentId (string) - Unique identifier of the shipment to retrieve.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| Shipment 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/returns/{returnId}/shipments/{shipmentId}?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("returnId", returnId);
		url.formatUrl("shipmentId", shipmentId);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def createPackageShipments(self,packageIds, returnId):
		""" Creates a shipment from one or more packages associated with a return replacement.
		
		Args:
			| packageIds(array|packageIds) - List of unique identifiers for each package associated with this shipment. Not all packages must belong to the same shipment.
			| returnId (string) - Unique identifier of the return whose items you want to get.
		
		Returns:
			| array of Package 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/returns/{returnId}/shipments", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("returnId", returnId);
		self.client.withResourceUrl(url).withBody(packageIds).execute();
		return self.client.result();

	
		
	def deleteShipment(self,returnId, shipmentId):
		""" Deletes a shipment for a return replacement.
		
		Args:
			| returnId (string) - Unique identifier of the return whose items you want to get.
			| shipmentId (string) - Unique identifier of the shipment to retrieve.
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/returns/{returnId}/shipments/{shipmentId}", "DELETE", UrlLocation.TenantPod, False);
		url.formatUrl("returnId", returnId);
		url.formatUrl("shipmentId", shipmentId);
		self.client.withResourceUrl(url).execute();

	
	
	