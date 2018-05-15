
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
		""" 
		
		Args:
			| appAuthInfo(appAuthInfo) - The information required to authenticate third party applications against the  API.
			| responseFields (string) - Filtering syntax appended to an API call to increase or decrease the amount of data returned inside a JSON object. This parameter should only be used to retrieve data. Attempting to update data using this parameter may cause data loss.
		
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
		""" 
		
		Args:
			| authTicketRequest(authTicketRequest) - Properties of the authentication ticket refresh requests, which includes the refresh token string.
			| responseFields (string) - Filtering syntax appended to an API call to increase or decrease the amount of data returned inside a JSON object. This parameter should only be used to retrieve data. Attempting to update data using this parameter may cause data loss.
		
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
		""" 
		
		Args:
			| refreshToken (string) - Alphanumeric string used for access tokens. This token refreshes access for accounts by generating a new developer or application account authentication ticket after an access token expires.
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/platform/applications/authtickets/{refreshToken}", "DELETE", UrlLocation.HomePod, False);
		url.formatUrl("refreshToken", refreshToken);
		self.client.withResourceUrl(url).execute();

	
	
	