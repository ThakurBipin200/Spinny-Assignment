# API Service for CRUD

Consider a store which has an inventory of boxes which are all cuboid(which have length, breadth and height). Each Cuboid has been added by a store employee who is associated as the creator of the box even if it is updated by any user later on.

## Tasks

### Task 0: Data Modeling

- Build minimal Models required for the such a store. You can use contrib modules for necessary models(for eg: users)


### Task 1: Add API

- Endpoint: `/api/boxes/add/`
- Method: POST
- Description: Adds a new box with specified dimensions.
- Permissions: Only staff users can add boxes.

### Task 2: Update API

- Endpoint: `/api/boxes/update/{id}/`
- Method: PUT
- Description: Updates the dimensions of a box with the given ID.
- Permissions: Any staff user can update boxes, except for the creator and creation date.

### Task 3: List All API

- Endpoint: `/api/boxes/list/`
- Method: GET
- Description: Retrieves a list of all boxes with detailed information.
- Permissions: All users can access this endpoint.
- Filters: Various filters available to search for boxes based on dimensions and other attributes.

### Task 4: List My Boxes API

- Endpoint: `/api/boxes/my-boxes/`
- Method: GET
- Description: Retrieves a list of boxes created by the authenticated user.
- Permissions: Only staff users can access their own created boxes.
- Filters: Additional filters available to search for boxes based on dimensions.

### Task 5: Delete API

- Endpoint: `/api/boxes/delete/{id}/`
- Method: DELETE
- Description: Deletes a box with the given ID.
- Permissions: Only the creator of the box can delete it.

## Additional Conditions

- Average area of all added boxes should not exceed A1.
- Average volume of all boxes added by the current user should not exceed V1.
- Total boxes added in a week cannot exceed L1.
- Total boxes added in a week by a user cannot exceed L2.

## Installation and Setup

1. Clone the repository.
2. Create a virtual environment and activate it.
3. Install the required dependencies from `requirements.txt`.
4. Configure the database settings in `settings.py`.
5. Run database migrations using `python manage.py migrate`.
6. Start the development server with `python manage.py runserver`.

