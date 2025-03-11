# Web Pages Design - Milestone 4

Lucid chart showing the flow of our webpages: <br>
<img src="webLayout.png" alt="Image description" width="500">

<h1>Homepage:</h1>
<p>
The <b>Homepage</b> serves as the main entry point for users, providing navigation to various sections of the website.
</p>
<p>
- A welcoming banner with a brief introduction.<br>
- Quick links to the <b>Customer Portal</b>, <b>Products Page</b>, and <b>Profile Page</b>.<br>
- Featured products or promotions.<br>
- Picture, Memo, Goals.
</p>

<h1>Products Page:</h1>
<p>
The <b>Products Page</b> displays a catalog of available items with detailed descriptions and purchasing options.
</p>
<h4> Features:</h4>
<p>
- <b>Product Listings:</b> Images, names, prices, and short descriptions.<br>
- <b>Filters & Sorting:</b> Allow customers to refine search results by price, category, or popularity.<br>
- <b>Add to Cart Button:</b> Enables quick purchases.<br>
- <b>Three categories</b> including pictures, links to product.
</p>
<h4> Parameters needed: </h4><p>
    - Dict? item info: price, picture location, details, etc <br>
    - Int or double? customer price level. <br>
</p>
<h4> Data needed to load page: </h4><p>
    - User Database<br>
    - Product Database<br>
    - product images <br>
    </p>
<h4> Variables needed to load page: </h4><p>
    - Product Image<br>
    - Product Name<br>
    - Product Price<br>
    - Display img<br>
    - Menu links<br>
    - Menu Destination
    </p>
    <img src="Products_Page.png" alt="checkout mockup for clients" width="500">
<h1>Cart:</h1>
<h4> Features:</h4>
<p> Items Currently in cart</p>
<p> Remove from cart </p>
<p> Update Quantity</p>
<p> Sign in bar at the top </p>
<h4> Parameters needed: </h4><p>
    - Array? items in cart <br>
    - Dict? item info <br>
    - Array? Quantity, potentially dict and combine with cart<br>
    - list? Customizations available</p>
<h4> Data Needed to load page: </h4><p>
    - product database <br>
    - images of products <br>
    - user database
</p>
<h4> Data Needed to load page: </h4><p>
    - Products in Cart<br>
    - Product Images<br>
    - Product Names<br>
    - Product Prices<br>
    - Product Customizations<br>
    - Display img<br>
    - Menu links<br>
    - Menu Destination
</p>
    
<img src="Cart.png" alt="checkout mockup for clients" width="500">
    
<h1>Customer Portal Page:</h1>
<p>  
The Charts will pull from the database to populate
    </p>
    <p>
Customer Can adjust Inventory and Shipping status.
    </p>
<img src="Customer_Portal.png" alt="Image description" width="500">

<h1>Profile Page:</h1>
<p>
This page allows users (customers/vendors) to view and manage:
</p>
<p>
- Current Orders: A list of active orders with status and delivery details.<br>
- Past Orders: Completed or canceled orders with dates, totals, and receipts.<br>
- Account Info: Editable personal data (name, email, address).<br>
- Cart: Items pending purchase, with stock warnings if needed.
</p>

<h3>Parameters Needed:</h3>
<p>
  - User ID / Session Token to identify which profile to load.<br>
  - User Role (customer, vendor) to determine which profile links to display.
</p>

<h3>Data Needed:</h3>
<p>
  - User Profile Data (name, email, address, etc.)<br>
  - Current Orders (order ID, products, status, estimated delivery)<br>
  - Past Orders (dates, totals, status)<br>
  - Cart Items (product details, quantity, price, stock alerts)
</p>

<h3>Link Destinations:</h3>
<p>
  - Header Navigation: Home, Products, Contact, Cart.<br>
  - Sidebar: Current Orders, Past Orders, Account Info, Cart - jumps to those interal profile sections.<br>
  - Vendor Links (if user is a vendor): Manage Inventory, Price Updates, leading to the Client Portal.
    
</p>

<img src="profile_layout.png" alt="Profile Page Wireframe" width="500">

