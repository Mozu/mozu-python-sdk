
"""
    This code was generated by Codezu.     

    Changes to this file may cause incorrect behavior and will be lost if
    the code is regenerated.
"""


from mozurestsdk.mozuclient import default as default_client
from mozurestsdk.mozuurl import MozuUrl;
from mozurestsdk.urllocation import UrlLocation
from mozurestsdk.apicontext import ApiContext;

class WishlistItem(object):
	def __init__(self, apiContext: ApiContext = None, mozuClient = None):
		self.client = mozuClient or default_client();
		if (apiContext is not None):
			self.client.withApiContext(apiContext);
		else:
			self.client.withApiContext(ApiContext());
	
	def getWishlistItem(self,wishlistId, wishlistItemId, responseFields = None):
		""" 
		
		Args:
			| wishlistId (string) - Unique identifier of the wish list item to retrieve.
			| wishlistItemId (string) - Unique identifier of the wish list associated with the item to retrieve.
			| responseFields (string) - 
		
		Returns:
			| WishlistItem 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/wishlists/{wishlistId}/items/{wishlistItemId}?responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("wishlistId", wishlistId);
		url.formatUrl("wishlistItemId", wishlistItemId);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getWishlistItems(self,wishlistId, startIndex = None, pageSize = None, sortBy = None, filter = None, responseFields = None):
		""" 
		
		Args:
			| wishlistId (string) - Unique identifier of the wish list associated with the items to retrieve.
			| startIndex (int) - 
			| pageSize (int) - 
			| sortBy (string) - 
			| filter (string) - 
			| responseFields (string) - 
		
		Returns:
			| WishlistItemCollection 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/wishlists/{wishlistId}/items?startIndex={startIndex}&pageSize={pageSize}&sortBy={sortBy}&filter={filter}&responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("filter", filter);
		url.formatUrl("pageSize", pageSize);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("sortBy", sortBy);
		url.formatUrl("startIndex", startIndex);
		url.formatUrl("wishlistId", wishlistId);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def getWishlistItemsByWishlistName(self,customerAccountId, wishlistName, startIndex = None, pageSize = None, sortBy = None, filter = None, responseFields = None):
		""" 
		
		Args:
			| customerAccountId (int) - The unique identifier of the customer account associated with the wish list.
			| wishlistName (string) - The name of the wish list that contains the items to retrieve.
			| startIndex (int) - 
			| pageSize (int) - 
			| sortBy (string) - 
			| filter (string) - 
			| responseFields (string) - 
		
		Returns:
			| WishlistItemCollection 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/wishlists/customers/{customerAccountId}/{wishlistName}/items?startIndex={startIndex}&pageSize={pageSize}&sortBy={sortBy}&filter={filter}&responseFields={responseFields}", "GET", UrlLocation.TenantPod, False);
		url.formatUrl("customerAccountId", customerAccountId);
		url.formatUrl("filter", filter);
		url.formatUrl("pageSize", pageSize);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("sortBy", sortBy);
		url.formatUrl("startIndex", startIndex);
		url.formatUrl("wishlistName", wishlistName);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def addItemToWishlist(self,wishlistItem, wishlistId, responseFields = None):
		""" 
		
		Args:
			| wishlistItem(wishlistItem) - Properties of the item to add to the wish list.
			| wishlistId (string) - Unique identifier of the wish list associated with the item to add.
			| responseFields (string) - 
		
		Returns:
			| WishlistItem 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/wishlists/{wishlistId}/items?responseFields={responseFields}", "POST", UrlLocation.TenantPod, False);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("wishlistId", wishlistId);
		self.client.withResourceUrl(url).withBody(wishlistItem).execute();
		return self.client.result();

	
		
	def updateWishlistItemQuantity(self,wishlistId, wishlistItemId, quantity, responseFields = None):
		""" 
		
		Args:
			| wishlistId (string) - Unique identifier of the wish list associated with the item quantity to update.
			| wishlistItemId (string) - Unique identifier of the item in the wish list to update quantity.
			| quantity (int) - The quantity of the item in the wish list.
			| responseFields (string) - 
		
		Returns:
			| WishlistItem 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/wishlists/{wishlistId}/items/{wishlistItemId}/{quantity}?responseFields={responseFields}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("quantity", quantity);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("wishlistId", wishlistId);
		url.formatUrl("wishlistItemId", wishlistItemId);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def updateWishlistItem(self,wishlistItem, wishlistId, wishlistItemId, responseFields = None):
		""" 
		
		Args:
			| wishlistItem(wishlistItem) - Properties of the shopper wish list item to update.
			| wishlistId (string) - Unique identifier of the wish list associated with the item to update.
			| wishlistItemId (string) - Unique identifier of the item in the shopper wish list to update.
			| responseFields (string) - 
		
		Returns:
			| WishlistItem 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/wishlists/{wishlistId}/items/{wishlistItemId}?responseFields={responseFields}", "PUT", UrlLocation.TenantPod, False);
		url.formatUrl("responseFields", responseFields);
		url.formatUrl("wishlistId", wishlistId);
		url.formatUrl("wishlistItemId", wishlistItemId);
		self.client.withResourceUrl(url).withBody(wishlistItem).execute();
		return self.client.result();

	
		
	def removeAllWishlistItems(self,wishlistId):
		""" 
		
		Args:
			| wishlistId (string) - Unique identifier of the wish list associated with the items to remove.
		
		Returns:
			| Wishlist 
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/wishlists/{wishlistId}/items", "DELETE", UrlLocation.TenantPod, False);
		url.formatUrl("wishlistId", wishlistId);
		self.client.withResourceUrl(url).execute();
		return self.client.result();

	
		
	def deleteWishlistItem(self,wishlistId, wishlistItemId):
		""" 
		
		Args:
			| wishlistId (string) - Unique identifier of the wish list associated with the item to remove.
			| wishlistItemId (string) - Unique identifier of the item to remove from the shopper wish list.
		
		Raises:
			| ApiException
		
		"""

		url = MozuUrl("/api/commerce/wishlists/{wishlistId}/items/{wishlistItemId}", "DELETE", UrlLocation.TenantPod, False);
		url.formatUrl("wishlistId", wishlistId);
		url.formatUrl("wishlistItemId", wishlistItemId);
		self.client.withResourceUrl(url).execute();

	
	
	