# Project Title: Kitchen Countertop - Inventory Tracking


### Team members' names:


Nicole Cosmany <br>
Evan Embry <br>
Patrick Ridley <br>
Cole Akers <br>
Stephen Tynan <br>


### Links


Project tracker link: https://trello.com/b/bcz0QtdX/project


Link to 5 minute video: https://drive.google.com/file/d/1NVpiI1_hhjZEFL5l-LT_-chggTeEs0qU/view?usp=sharing


Github repo: https://github.com/SoftwareGroup5/Project-.git


Public site: https://countertops.onrender.com




### Reflection


What we completed:
  - functional login for client and customer and admin: the user can navigate the website, add items and shop.
  - product page showing available products for purchase, can be added to cart
  - profile page custom for client vs customer: client shows full inventory + shipping status, customer shows personalized information + order history
  - cart shows active cart, calculates total for line item and cart 
  - can place real order from cart
  - add to cart functionality for shopping
  - database containing all products
  - CSS styling for dark theme layout across all major pages
  


What we were in the middle of implementing:
  - Additional unit tests
  - Uniformity throughout all web pages
  - admin functionality. 




What we had planned for the future:
  - abandon cart feature to send automatic email to customer
  - shipping status can be updated from admin portal
  - update inventory amount
  - lock a product if out of stock
  - adjust price of a product
  - create account for new users
  - continued styling and uniformity across pages
  - handle negative inventory + low stock
  - remove items from cart 
  - the login could be fleshed out with additional functions such as forgot password, create account, forgot username, etc. It is a simplified version that works for the demo. For future implementation we might want to switch to using a prebuilt solution such as google's authentication.


Any known problems (bugs, issues):
  - database resets every a user navigates to the home page (this was intentional for demonstration and longevity purposes but on a production level wouldn't make sense)
  - the reset makes it challenging to see inventory update post purchase.  Opening an incognito page works around it
  - no security on login, not safe to push live: would need a more robust login handling strategy that does not currently account for potential vectors hackers might use to gain access.

