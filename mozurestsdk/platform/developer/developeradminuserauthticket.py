
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation

class DeveloperAdminUserAuthTicket(object):
	def __init__(self, mozuClient = None):
		self.client = mozuClient or default_client();
	
	def createDeveloperUserAuthTicket(self,userAuthInfo, developerAccountId = None, responseFields = None):
		""" Generate an authentication ticket for a developer account.
		
		Args:
			| userAuthInfo(userAuthInfo) - Information required to authenticate a user.
			| developerAccountId (int) - Unique identifier of the developer account.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| DeveloperAdminUserAuthTicket 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/platform/developer/authtickets/?developerAccountId={developerAccountId}&responseFields={responseFields}", "POST", UrlLocation.HomePod, False);
		url.formatUrl("developerAccountId", developerAccountId);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(userAuthInfo).execute();
		return self.client.result();

	
		
	def refreshDeveloperAuthTicket(self,existingAuthTicket, developerAccountId = None, responseFields = None):
		""" Generates a new developer account authentication ticket for the specified tenant by supplying the defined refresh token information.
		
		Args:
			| existingAuthTicket(existingAuthTicket) - Properties of the authentication ticket to be used in developer account claims with the  API.
			| developerAccountId (int) - Unique identifier of the developer account.
			| responseFields (string) - Use this field to include those fields which are not included by default.
		
		Returns:
			| DeveloperAdminUserAuthTicket 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/platform/developer/authtickets/?developerAccountId={developerAccountId}&responseFields={responseFields}", "PUT", UrlLocation.HomePod, False);
		url.formatUrl("developerAccountId", developerAccountId);
		url.formatUrl("responseFields", responseFields);
		self.client.withResourceUrl(url).withBody(existingAuthTicket).execute();
		return self.client.result();

	
		
	def deleteUserAuthTicket(self,refreshToken):
		""" Deletes the authentication ticket for the developer account by supplying the refresh token.
		
		Args:
			| refreshToken (string) - Alphanumeric string used for access tokens. This token refreshes access for accounts by generating a new developer or application account authentication ticket after an access token expires.
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/platform/developer/authtickets/?refreshToken={refreshToken}", "DELETE", UrlLocation.HomePod, False);
		url.formatUrl("refreshToken", refreshToken);
		self.client.withResourceUrl(url).execute();

	
	
	