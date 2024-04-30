# Vendor Management System API

This Vendor Management System API allows you to manage vendors, purchase orders, and retrieve performance metrics for vendors.

## Setup Instructions

1. Clone the repository:
   
git clone <repository_url>

cd vendor_management_system_api

2.Create and activate a virtual environment

python3 -m venv venv

source venv/bin/activate

3. Install dependencies
   
pip install -r requirements.txt

4. Run database migrations
   
python manage.py migrate

5. Start the deployment server
   
python manage.py runserver

6. Access the API endpoints at 'http://localhost:8000/api/'.


## API Endpoints

#### Create Vendor

**URL:** `/api/vendors/`  
**Method:** `POST`  
**Description:** Create a new vendor.  
**Request Body:** JSON object containing vendor details (name, contact details, address, vendor code).  
**Response:** JSON object representing the created vendor.  

#### Retrieve Vendor

**URL:** `/api/vendors/{vendor_id}/`  
**Method:** `GET`  
**Description:** Retrieve details of a specific vendor.  
**Parameters:** `{vendor_id}` - ID of the vendor to retrieve.  
**Response:** JSON object representing the retrieved vendor.  

#### Update Vendor

**URL:** `/api/vendors/{vendor_id}/`  
**Method:** `PUT`  
**Description:** Update details of a specific vendor.  
**Parameters:** `{vendor_id}` - ID of the vendor to update.  
**Request Body:** JSON object containing updated vendor details.  
**Response:** JSON object representing the updated vendor.  

#### Delete Vendor

**URL:** `/api/vendors/{vendor_id}/`  
**Method:** `DELETE`  
**Description:** Delete a specific vendor.  
**Parameters:** `{vendor_id}` - ID of the vendor to delete.  
**Response:** Empty response with HTTP status code 204 (No Content).  

#### List Purchase Orders

**URL:** `/api/purchase_orders/`  
**Method:** `GET`  
**Description:** List all purchase orders with an option to filter by vendor.  
**Parameters:** None (Optional query parameter `vendor_id` to filter by vendor).  
**Response:** JSON array representing the list of purchase orders.  

#### Create Purchase Order

**URL:** `/api/purchase_orders/`  
**Method:** `POST`  
**Description:** Create a new purchase order.  
**Request Body:** JSON object containing purchase order details (PO number, vendor ID, order date, delivery date, items, quantity, status).  
**Response:** JSON object representing the created purchase order.  

#### Retrieve Purchase Order

**URL:** `/api/purchase_orders/{po_id}/`  
**Method:** `GET`  
**Description:** Retrieve details of a specific purchase order.  
**Parameters:** `{po_id}` - ID of the purchase order to retrieve.  
**Response:** JSON object representing the retrieved purchase order.  

#### Update Purchase Order

**URL:** `/api/purchase_orders/{po_id}/`  
**Method:** `PUT`  
**Description:** Update details of a specific purchase order.  
**Parameters:** `{po_id}` - ID of the purchase order to update.  
**Request Body:** JSON object containing updated purchase order details.  
**Response:** JSON object representing the updated purchase order.  

#### Delete Purchase Order

**URL:** `/api/purchase_orders/{po_id}/`  
**Method:** `DELETE`  
**Description:** Delete a specific purchase order.  
**Parameters:** `{po_id}` - ID of the purchase order to delete.  
**Response:** Empty response with HTTP status code 204 (No Content).  

#### Retrieve Vendor Performance Metrics

**URL:** `/api/vendors/{vendor_id}/performance`  
**Method:** `GET`  
**Description:** Retrieve a vendor's performance metrics.  
**Parameters:** `{vendor_id}` - ID of the vendor to retrieve performance metrics for.  
**Response:** JSON object representing the vendor's performance metrics (on-time delivery rate, quality rating, response time, fulfilment rate).  

## Usage

To use these endpoints, make HTTP requests to the specified URLs with appropriate request bodies and parameters.

## Testing

Test cases have been created to ensure the reliability and correctness of the API endpoints. You can run these tests using the following command:

```bash
python manage.py test

