
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation

class TenantAdminUserAuthTicket(object):
	def __init__(self, mozuClient = None):
		self.client = mozuClient or default_client();
	
	def createUserAuthTicket(self,userAuthInfo, tenantId = None, responseFields = None):
		"""
			Creates an authentication ticket for the supplied user to specify in API requests associated with the supplied tenant.
			Request Params
				string responseFields Use this field to include those fields which are not included by default.
				int tenantId Unique identifier of the development or production tenant for which to generate the user authentication ticket.
				userAuthInfo Information required to authenticate a user.
			Response
				TenantAdminUserAuthTicket 
		"""

		url = MozuUrl("/api/platform/adminuser/authtickets/tenants?tenantId={tenantId}&responseFields={responseFields}", "POST", UrlLocation.HomePod, False);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("tenantId", tenantId);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def refreshAuthTicket(self,existingAuthTicket, tenantId = None, responseFields = None):
		"""
			Generates a new user authentication ticket for the specified tenant by supplying the user's existing refresh token information.
			Request Params
				string responseFields Use this field to include those fields which are not included by default.
				int tenantId 
				existingAuthTicket Properties of the authentication ticket to be used in user claims with the Mozu API.
			Response
				TenantAdminUserAuthTicket 
		"""

		url = MozuUrl("/api/platform/adminuser/authtickets/tenants?tenantId={tenantId}&responseFields={responseFields}", "PUT", UrlLocation.HomePod, False);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("tenantId", tenantId);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def deleteUserAuthTicket(self,refreshToken):
		"""
			Deletes the authentication ticket for the user by supplying the refresh token.
			Request Params
				string refreshToken Alphanumeric string used for access tokens. This token refreshes access for accounts by generating a new developer or application account authentication ticket after an access token expires.
			Response
		"""

		url = MozuUrl("/api/platform/adminuser/authtickets/?refreshToken={refreshToken}", "DELETE", UrlLocation.HomePod, False);
		url.formatUrl("refreshToken", refreshToken);
		self.client.withResourceUrl(url).execute();

	
	
	