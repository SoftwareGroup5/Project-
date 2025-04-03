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
### Function: Retrieve All Products for Listing Page
- Purpose: Display all products available for purchase on the product listing page.
- Query:
  sql
  SELECT id_product, prod_name, img_link, prod_price, product_inv 
  FROM prod_table;

#### Function: Retrieve One Product by ID
- Purpose: Fetch detailed information for a specific product using its unique ID.
- Query:
  sql
  SELECT prod_name, img_link, prod_price, product_inv
  FROM prod_table
  WHERE id_product = (product id for selected single product);
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
- auth_level: STRING, client or customer, decides which landing page to show.
- auth: Boolean, Confirms authorization true or false.  
- customer_id: INT, unique identifier for the customer (foreign key)
- products_owned: STRING,  CSV format STRING of owned product ids.

**Primary Key:** id_login  
**Foreign Keys:** customer_id 

**Function: Authorization Login** <br>

Purpose:<br>
check for valid login<br>

check Login info against Authentication from auth_table (decide if employee or customer) <br>

Behavior:<br>
Check user inputted login again login data in auth_table<br>
Return customer details: auth_level, auth, customer_id, products_owned <br>
swap login button for profile, directing to either customer or employee portal <br>
redirect to previous page. <br>


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

Function to do this: sum all total prices in rows (of this table) for the order_id where customer_id matches current customer and order_status is "in cart" (of the order_history table)

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

Function to do this: show rows in orders where customer_id matches current customer, status is "ordered", and group by order_id

## Order_History
**Table Name:** Order_History <br>
**Table Description:** Shows order history by customer ID
<br>
- customer_id: INT, foreign key linking to customer_table which identifies each customer <br>
- id_order: INT, primary key linking to orders which is a unque key for ever order <br>
- order_status: STRING, tracks current status of order, such as (processing, approved, design accepted) <br>
- date: DATETIME, date showing change in status of order. <br>
- order_total: Float, decimal value for total price of order <br>
- order_status: STRING, value that states from a list of options current order status (shipped, recieved, pending) <br>

Expected result: Employee can update order_status and shipping_status <br>
Actual result: Employee will have full view of order_history <br>

**Test: View order history as an employee** <br>
Descripttion: Employee can see history of orders <br>
Pre-condition: Employee is logged into system <br>
Test steps: <br>
  1. Employee can navigate to web page
  2. Employee can view order and shipping status by customer
  3. Employee can update order or shipping status


Expected result: Customer can see overall order price of there order
Actual result: Customer can see their own order

Expected result: Customer can see updated order_status and shipping_status of there order
Actual result: Customer can see their own order status

**Test: View order history as an customer** <br>
Descripttion: Customer can see history of only there order <br>
Pre-condition: Customer is logged into system <br>
Test steps: <br>
  1. Customer can navigate to web page
  2. Customer can view order and shipping status or there order
  3. Customer can see total cost of there order, along with address, etc
**API: Customer/Employee Portal - INVENTORY** <br>

Purpose:<br>
Display current inventory<br>

Authentication from auth_table (decide if employee or customer) <br>

Behavior:<br>
If user is an Employee:<br>
<li><strong> API displays store_inventory </strong></li>
    <li>API pulls all records from order_history</li>
    <li>API joins order_history with product_table to include:</li>
    <ul>
    <li>Product Name</li>
    <li>theme</li>
    <li>Image Link (to display image</li>
    </ul>
If user is an Customer:<br>
Does nothing, displays nothing<br>
<br>
**API: Customer/Employee Portal - SHIPPING STATUS** <br>

Purpose:<br>
To track order and shipping status.<br>

Authentication from auth_table (decide if employee or customer) <br>

If user is an Employee:<br>
<li><strong> API displays order_status </strong></li>
    <li>API pulls all records from order_history</li>
    <li>API joins order_history with product_table to include:</li>
    <ul>
    <li>Product Name</li>
    </ul>
    <li>API joins order_history with customer_table to include:</li>
    <ul>
    <li>Customer Name (first and last)</li>
    <li>Customer Address</li>
    </ul>
    <li>API allows to adjust shipping and order status
<br>
      
## Customer Table  
**Table Name:** customer_table <br> 
**Table Description:** Stores customer information for orders, login, and profile display  <br>

- id_customer: INT, unique identifier for the customer (primary key)  <br>
- first_name: STRING, customer’s first name  <br>
- last_name: STRING, customer’s last name  <br>
- address: STRING, customer’s address  <br>

**Primary Key:** id_customer  <br>
**Foreign Keys:**  <br>
- customer_id in auth_table  <br>
- customer_id in Order_History  <br>

**Function: Retrieve All Customers** <br>
Purpose: Display all customers for an employee/administrator <br>
Query: `SELECT id_customer, first_name, last_name, address FROM customer_table;` <br>

**Function: Retrieve One Customer by ID** <br>
Purpose: Fetch detailed information for a specific customer on their profile page <br>
Query: `SELECT id_customer, first_name, last_name, address FROM customer_table WHERE id_customer = (customer's ID);` <br>

**Test: Retrieve Customer Information** <br>
Description: Ensure customer details are retrieved from the database <br>
Pre-conditions: Customers already exist in the database <br>
Test steps: <br>
1. Navigate to the profile or lookup page <br>
2. Search by customer ID <br>
3. View the customer information <br>

Expected result: User should see correct name and address for the customer <br>
Actual result: User is able to see customer details <br>

Post-conditions: No change to the customer_table <br>

**Test: Verify Order History Link** <br>
Description: Ensure the customer ID links correctly with the Order_History table <br>
Pre-conditions: Customer has past orders in Order_History <br>
Test steps: <br>
1. Navigate to the profile page <br>
2. Load the last 5 orders for the logged-in customer <br>
3. Confirm orders are correctly linked to the customer <br>

Expected result: Orders appear under the correct customer profile <br>
Actual result: Orders load correctly for the customer <br>

Post-conditions: Orders remain view-only <br>

**Test: Load Profile After Login** <br>
Description: Load customer profile information after login <br>
Pre-conditions: Customer is logged in through auth_table <br>
Test steps: <br>
1. Customer clicks profile button <br>
2. System loads customer_table using customer_id <br>
3. Profile shows name, address, and recent orders <br>

Expected result: Profile page shows accurate customer info and last 5 orders 
Actual result: Profile is loaded with correct details <br>

Post-conditions: Profile is read-only, no updates to customer_table <br> 


