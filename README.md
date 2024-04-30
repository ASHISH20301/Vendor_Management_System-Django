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

### Vendor Endpoints
POST /api/vendors/: Create a new vendor.
GET /api/vendors/: List all vendors.
GET /api/vendors/{vendor_id}/: Retrieve details of a specific vendor.
PUT /api/vendors/{vendor_id}/: Update a vendor's details.
DELETE /api/vendors/{vendor_id}/: Delete a vendor.

### Purchase Order Endpoints
POST /api/purchase_orders/: Create a new purchase order.
GET /api/purchase_orders/: List all purchase orders with an option to filter by vendor.
GET /api/purchase_orders/{po_id}/: Retrieve details of a specific purchase order.
PUT /api/purchase_orders/{po_id}/: Update a purchase order.
DELETE /api/purchase_orders/{po_id}/: Delete a purchase order.

### Vendor Performance Endpoint
GET /api/vendors/{vendor_id}/performance/: Retrieve a vendor's performance metrics.


