# SQL Testing 

## Products  
**Table Name:** prod_table  
**Table Description:** Stores information about products available for purchase  

- prod_name: STRING, name of the product  
- img_link: STRING, URL to the product image  
- prod_price: FLOAT, price of a single unit of the product  
- product_inv: INT, number of items available in inventory  
- id_product: INT, unique identifier for the product (primary key)  

**Primary Key:** id_product  
**Foreign Keys:** None  

---

### Test: Retrieve Product Information  
**Description:** Ensure product details are retrieved from the database  
**Pre-conditions:** Products are already populated in the database  
**Test steps:**  
1. Navigate to the product listing page  
2. View the list of products  
3. Click on a product to see its detailed info  

**Expected result:** User should see accurate product details with name, image, price, and inventory  
**Actual result:** N/A  
**Status:** N/A  
**Notes:** N/A  
**Post-conditions:** Product data is read-only; no modification to the table occurs  

---

### Test: Display Product Image and Price  
**Description:** Confirm that product images and prices display correctly on product listing and details pages  
**Pre-conditions:** Products have valid image URLs and price values stored in the table  
**Test steps:**  
1. Navigate to the product listing page  
2. Observe image and price fields  

**Expected result:** Product image renders from the img_link URL and price is formatted properly  
**Actual result:** N/A  
**Status:** N/A  
**Notes:** N/A  
**Post-conditions:** Product display reflects the accurate img_link and prod_price values  

---
## Authorization
**Table Name:** auth_table  
**Table Description:** Stores information about customers and clients including login and auth 

- id_login: INT, unique identifier for the client or customer (primary key)  
- atho_level: STRING, client or customer, decides which landing page to show.
- autho: Boolean, Confirms authorization true or false.  
- customer_id: INT, unique identifier for the customer (foreign key)
- products_owned: STRING,  CSV format STRING of owned product ids.

**Primary Key:** id_login  
**Foreign Keys:** customer_id 

**Test: Verify login** <br>
Description: check login for bugs <br>
Pre-conditions: customer or client exist in database <br>
Test steps: <br>
  1. client or customer clicks login <br>
  2. they are redirected to login page <br>
  3. they provided their login id <br>
  4. if auth_level = customer last id_order for customer_id is search and populated to cart <br>
  5. id_login is displayed in profile button in place of login button <br>
 
 Expected result: User should be able to see their id_login and cart <br>
Actual result: User is able to see their id_login and cart <br>
Status: N/A <br>
Notes: N/A <br>
Post-conditions: The autho boolean is set to TRUE, autho_level is loaded succesfully  <br>

**Test: Verify profile loaded** <br>
Description: populate profile page for id_login for correct authorization level <br>
Pre-conditions: customer or client exist in database, customer or client is logged-in  <br>
Test steps: <br>
  1. client or customer clicks profile button <br>
  2. they are redirected to profile page <br>
  3. if customer, load customer page, last 5 orders, allows loading previous orders to cart <br>
  4. if client load client page, load owned products, allow inventory updates. <br>
 
Expected result: User should be able to see their profile and previous orders, clients should see their profile and update inventory <br>
Actual result: User is able to see their profile and previous orders, clients can see their profile and update inventory <br>
Status: N/A <br>
Notes: N/A <br>
Post-conditions: Cart is updated for customers, inventory is updated for clients <br>

---

 ## Orders <br>
**Table Name:** Orders <br>
**Table Description:** Shows the contents for each order 
<br>
- order_id: INT, foreign key linking to Order_history table which identifies each order <br>
- product_id: INT, foreign key linking to prod_table which identifies each product <br>
- quantity: INT, how many were ordered <br>
- total_price: DEC, the total amount charged for this line item = quantity x prod_table.prod_price <br>

composite primary key = order_id, product_id

**Test: Compute Order Total** <br>
Description: Populate the Order_history table with the order total <br>
Pre-conditions: Customer adds items to their cart <br>
Test steps: <br>
  1. Fill cart with 1 or more products <br>
  2. Navigate to cart <br>
  3. See item total <br>
  
Expected result: User should be able to see their total price at checkout <br>
Actual result: User is navigated to cart and can see the total price <br>
Status: N/A <br>
Notes: N/A <br>
Post-conditions: The Order_history table has a valid order_total when in-cart status is true  <br>

**Test: View Itemized Order History** <br>
Description: View an order history that includes itemized list of products in the order <br>
Pre-conditions: Customer placed an order <br>
Test steps: <br>
  1. Fill cart with 1 or more products <br>
  2. Navigate to cart <br>
  3. Place order <br>
  4. Navigate to user profile page showing order history <br>
  
Expected result: User should be able to see their past orders including items/quantities in each order <br>
Actual result: User is navigated to user profile and can see itemized receipt of past order <br>
Status: N/A <br>
Notes: N/A <br>
Post-conditions: The Order_history table has a valid order_total that persists after the order is placed <br>
