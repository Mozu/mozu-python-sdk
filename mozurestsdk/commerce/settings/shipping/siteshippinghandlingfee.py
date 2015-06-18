
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class SiteShippingHandlingFee(object):
	def __init__(self, apiContext: ApiContext = None, mozuClient = None):
		self.client = mozuClient or default_client();
		client.withApiContext(apiContext);
	
	def getOrderHandlingFee(self,responseFields = None):
		"""
			Retrieves the details of the order handling fee configured for the site.
			Request Params
				string responseFields Use this field to include those fields which are not included by default.
			Response
				SiteShippingHandlingFee 
		"""

		url = MozuUrl("/api/commerce/settings/shipping/orderhandlingfee?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def createOrderHandlingFee(self,orderHandlingFee, responseFields = None):
		"""
			Creates a new order handling fee for the site.
			Request Params
				string responseFields Use this field to include those fields which are not included by default.
				orderHandlingFee Properties of the handling fee to apply to order shipments for the site.
			Response
				SiteShippingHandlingFee 
		"""

		url = MozuUrl("/api/commerce/settings/shipping/orderhandlingfee?responseFields={responseFields}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def updateOrderHandlingFee(self,orderHandlingFee, responseFields = None):
		"""
			Updates the order handling fee amount for the site.
			Request Params
				string responseFields Use this field to include those fields which are not included by default.
				orderHandlingFee Properties of the handling fee to apply to order shipments for the site.
			Response
				SiteShippingHandlingFee 
		"""

		url = MozuUrl("/api/commerce/settings/shipping/orderhandlingfee?responseFields={responseFields}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
	
	