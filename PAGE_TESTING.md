# Web Pages Design - Milestone 4

Lucid chart showing the flow of our webpages: <br>
<img src="webLayout.png" alt="Image description" width="500">

<h1>Homepage:</h1>
<p>

<p> The <b>Homepage</b> serves as the main entry point for users, providing a welcoming introduction and easy navigation to key sections of the website. 
</p> <h4> Features:</h4> <p> 
    - <b>Welcome Banner:</b> A visually engaging header with a brief introduction to the website and its offerings <br>
    - <b>Quick Navigation:</b> Clearly visible links directing users to the Cart, Products Page, and Profile Page.<br> 
    - <b>Featured Products & Promotions:</b> Highlighted deals, trending items, promoted items.<br> 
    - <b>User Personalization:</b> A section displaying the user’s profile picture or login ID to confirm login status.<br> </p> 

<h4> Parameters Needed: </h4> <p> 
    - User ID to personalize content (cart).<br> 
    - Featured product data (name, image, price, and promotional details).<br> 
    - User name.<br> </p> 

<h4> Data Needed to Load Page: </h4> <p> 
    - User Database (to display personalized content if logged in).<br> 
    - Product Database (to load featured products and promotions).<br> 
    - Static Assets (homepage banner image).<br> </p> 

<h4> Link Destinations: </h4> <p> 
    - <b>Cart:</b> Takes users to their current shopping cart.<br> 
    - <b>Products Page:</b> Leads customers to browse and purchase items.<br> 
    - <b>Profile Page:</b> Provides access to user-specific details, including past orders and account management.<be>
<h4>Test Cases:</h4>
<ul>
    <li>As a customer, I can access my cart from this page.</li>
    <li>As a customer, I can access my profile from this page.</li>
    <li>As a customer, I can access the products page from this page.</li>
    <li>As an employee, I can access my employee profile from this page.</li>
    <li>As a customer, this page will show images of featured products.</li>
</ul>
        <img src="Homepage.png" alt="Homepage Wireframe" width="500">



    
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
<h4> Data Needed to load page: </h4><p>
    - User Database<br>
    - Product Database<br>
    - product images <br>
    </p>
<h4> Link Destinations: </h4> <p> 
    - <b>Home</b> Takes users to Home.<br> 
    - <b>Cart:</b> Takes users to their Cart.<br> 
    - <b>login:</b> Provides access to customer or owner portal depending on login token<be>
<h4>Test Cases:</h4>
<ul>
    <li>As a customer, I can access my cart from this page.</li>
    <li>As a customer, I can access my profile from this page.</li>
    <li>As a customer, I can add Products to cart</li>
    <li>As an employee, I can access my employee profile from this page.</li>
    <li>As a customer, this page will show images prices and item info for all products.</li>
    <li>As a customer, the product pictures and info will magnify on hover.</li>
</ul>
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
<h4> Link Destinations: </h4> <p> 
    - <b>Home</b> Takes users to Home.<br> 
    - <b>Products Page:</b> Takes users to products page.<br> 
    - <b>Login:</b> Provides access to customer or owner portal depending on login token<be>
<h4>Test Cases:</h4>
<ul>
    <li>As a customer, I can access the products page from this page.</li>
    <li>As a customer, I can access my profile from this page.</li>
    <li>As a customer, I can remove products from cart</li>
    <li>As an employee, I can access my employee profile from this page.</li>
    <li>As a customer, this page will show images, prices, customization options, and item info for all products.</li>
    <li>As a customer, I can make customizations and adjust project details in cart.</li>
</ul>
<img src="Cart.png" alt="checkout mockup for clients" width="500">
    
<h1>Customer (vendor) Portal Page:</h1>
<p>  
The Charts will pull from the database to populate
    </p>
    <p>
Customer Can adjust Inventory and Shipping status.
    </p>
    </h2>
    Test Cases:
    </h2>
    <li>
    As an employee, I can log into the webpage and able to access this page
    </li>
    <li>
    As an employee, I can adjust inventory.
    </li>
    <li>
    As an employee, I can see inventory
    </li>
    <li>
    As an employee, I can adjust shipping status
    </li>
    <li>
    As an employee, I can adjust address/name
    </li>
    <li>
    As a customer, this page will not be presented to me
    </li>
    <p></p>
    </h2>
    Page Linking:
    </h2>
    <li>
    This page has a link from main page, if user is authenticated as an employee 
    </li>
    <li>
    This page has a logout option
    </li>
    <li>
    This page can return to main page
    </li>
    <p></p>
    </h2>
    Inventory Parameters:
    </h2>
    <li>
    Countertop Item Name
    </li>
    <li>
    Countertop category
    </li>
    <li>
    Countertop stock amount
    </li>
    <li>
    Open orders
    </li>
    <li>
    Adjusted amount of stock left
    </li>
    </h2>
    Shipping Parameters:
    </h2>
    <li>
    Ship Date
    </li>
    <li>
    Countertop Item Name
    </li>
    <li>
    Customer info
    </li>
    <li>
    Shipping status
    </li>
    <p></p>
    </h2>
    Inventory Data:
    </h2>
    <li>
    Countertop themes
    </li>
    <li>
    Countertop names
    </li>
    <li>
    Stock amounts
    </li>
    </h2>
    Shipping Data:
    </h2>
    <li>
    Customer info
    </li>
    <li>
    Shipping status
    </li>
    <li>
    Linking to orders
    </li>
    <p></p>
    
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

<h3>Test Cases:</h3>

<p>
As a customer, I can log into the webpage and access my Profile Page.
As a customer, I can view my current orders with their status and estimated delivery.
As a customer, I can view my past orders with dates, totals, and receipts.
As a customer, I can update my account information (name, email, address).
As a customer, I can see my cart items and any low-stock warnings.
As a customer, I will not see vendor/admin links.
As a vendor, I can log into the webpage and access my Profile Page.
As a vendor, I can access vendor-specific links (Manage Inventory, Price Updates) that lead to the Client Portal.
As a vendor, I can still view my own orders and account info.
As a vendor, I will not see customer-specific cart features.

</p>

<img src="profile_layout.png" alt="Profile Page Wireframe" width="500">

