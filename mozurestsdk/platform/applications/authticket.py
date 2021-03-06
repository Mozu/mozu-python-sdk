
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation

class AuthTicket(object):
	def __init__(self, mozuClient = None):
		self.client = mozuClient or default_client();
	
	def authenticateApp(self,appAuthInfo, responseFields = None):
		""" Generate an authentication ticket for an application.
		
		Args:
			| appAuthInfo(appAuthInfo) - The information required to authenticate third party applications against the  API.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| AuthTicket 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/platform/applications/authtickets/?responseFields={responseFields}", "POST", UrlLocation.HomePod, False);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(appAuthInfo).execute();
		return self.client.result();

	
		
	def refreshAppAuthTicket(self,authTicketRequest, responseFields = None):
		""" Refreshes the application's authentication ticket and generates a new access token by providing the refresh token string.
		
		Args:
			| authTicketRequest(authTicketRequest) - Properties of the authentication ticket refresh requests, which includes the refresh token string.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| AuthTicket 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/platform/applications/authtickets/refresh-ticket?responseFields={responseFields}", "PUT", UrlLocation.HomePod, False);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(authTicketRequest).execute();
		return self.client.result();

	
		
	def deleteAppAuthTicket(self,refreshToken):
		""" Deletes an authentication for an application based on the specified refresh token.
		
		Args:
			| refreshToken (string) - Alphanumeric string used for access tokens. This token refreshes access for accounts by generating a new developer or application account authentication ticket after an access token expires.
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/platform/applications/authtickets/{refreshToken}", "DELETE", UrlLocation.HomePod, False);
		url.formatUrl("refreshToken", refreshToken);
		self.client.withResourceUrl(url).execute();

	
	
	