from tinydb import TinyDB, Query
import uuid

# Initialize the database (creates a JSON file if it doesn't exist)
db = TinyDB("db/applications_db.json")
applications = db.table("applications")

# ------------------------------
# Data Model Structure
# ------------------------------
# Each application record will look like:
# {
#   "id": "a1b2c3d4",
#   "title": "Software Engineering Intern - Google", 
#   "company":  "Google"
#   "job_description": "Looking for a candidate with React, Node.js, and cloud experience...",
#   "generated_resume": "<tailored resume text here>"
# }

# ------------------------------
# CRUD FUNCTIONS
# ------------------------------

def create_application(title: str, company:str, job_description: str, generated_resume: str = "") -> str:
    """Create a new application record and add it to the database."""
    record_id = str(uuid.uuid4())
    new_record = {
        "id": record_id,
        "title": title, 
        "company": company,
        "job_description": job_description,
        "generated_resume": generated_resume,
    }
    applications.insert(new_record)
    print(f" Application created with ID: {record_id}")
    return record_id


def get_application_by_id(record_id: str):
    """Retrieve an application by its unique ID."""
    Application = Query()
    result = applications.get(Application.id == record_id)
    if result:
        return result
    else:
        print(f" No record found with ID: {record_id}")
        return None


def update_application(record_id: str, field: str, new_value: str):
    """Update a specific field in an application record."""
    Application = Query()
    valid_fields = {"title", "job_description", "generated_resume"}
    if field not in valid_fields:
        print(f"Invalid field name '{field}'. Valid fields: {valid_fields}")
        return False

    updated = applications.update({field: new_value}, Application.id == record_id)
    if updated:
        print(f"Updated '{field}' for record {record_id}")
        return True
    else:
        print(f"No record found with ID: {record_id}")
        return False


def delete_application(record_id: str):
    """Delete an application from the database."""
    Application = Query()
    deleted = applications.remove(Application.id == record_id)
    if deleted:
        print(f"Deleted record with ID: {record_id}")
        return True
    else:
        print(f"No record found with ID: {record_id}")
        return False


def list_all_applications():
    """Return all applications in the database."""
    all_apps = applications.all()
    if not all_apps:
        print(" No applications found.")
    return all_apps


