
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class ProductHandlingFeeRules(object):
	def __init__(self, apiContext: ApiContext = None, dataViewMode="Live", mozuClient = None):
		if (apiContext is not None and apiContext.dataViewMode is None):
			apiContext.dataViewMode = dataViewMode;
		else:
			apiContext = ApiContext(dataViewMode = dataViewMode);
		self.client = mozuClient or default_client();
		self.client.withApiContext(apiContext);
	
	def getProductHandlingFeeRule(self,profilecode, id, responseFields = None):
		""" 
		
		Args:
			| profilecode (string) - 
			| id (string) - 
			| responseFields (string) - 
		
		Returns:
			| HandlingFeeRule 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/shipping/admin/profiles/{profilecode}/rules/producthandlingfees/{id}?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("id", id);
		url.formatUrl("profilecode", profilecode);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getProductHandlingFeeRules(self,profilecode, responseFields = None):
		""" 
		
		Args:
			| profilecode (string) - 
			| responseFields (string) - 
		
		Returns:
			| HandlingFeeRuleCollection 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/shipping/admin/profiles/{profilecode}/rules/producthandlingfees?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("profilecode", profilecode);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def createProductHandlingFeeRule(self,rule, profilecode, responseFields = None):
		""" 
		
		Args:
			| rule(rule) - 
			| profilecode (string) - 
			| responseFields (string) - 
		
		Returns:
			| HandlingFeeRule 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/shipping/admin/profiles/{profilecode}/rules/producthandlingfees?responseFields={responseFields}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("profilecode", profilecode);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(rule).execute();
		return self.client.result();

	
		
	def updateProductHandlingFeeRule(self,rule, profilecode, id, responseFields = None):
		""" 
		
		Args:
			| rule(rule) - 
			| profilecode (string) - 
			| id (string) - 
			| responseFields (string) - 
		
		Returns:
			| HandlingFeeRule 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/shipping/admin/profiles/{profilecode}/rules/producthandlingfees/{id}?responseFields={responseFields}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("id", id);
		url.formatUrl("profilecode", profilecode);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(rule).execute();
		return self.client.result();

	
		
	def deleteProductHandlingFeeRule(self,profilecode, id):
		""" 
		
		Args:
			| profilecode (string) - 
			| id (string) - 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/shipping/admin/profiles/{profilecode}/rules/producthandlingfees/{id}", "DELETE", UrlLocation.TenantPod, False);
		url.formatUrl("id", id);
		url.formatUrl("profilecode", profilecode);
		self.client.withResourceUrl(url).execute();

	
	
	