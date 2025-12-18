# Django Shell Tutorial - Create and Query Data

Django shell is an interactive Python shell with Django environment loaded, allowing you to interact with your models and database directly.

## Starting Django Shell

```bash
python manage.py shell
```


##  Importing Models
Inside the shell:
```python
from notes.models import Notes
```

---

##  Query Examples

### 1. Fetch All Notes
```python
newObject = Notes.objects.all()
newObject
```
**Output:**
```python
<QuerySet [<Notes: Notes object (3)>, <Notes: Notes object (4)>, ...]>
```
Shows all records in the `Notes` table.

---

### 2. Fetch a Single Note by ID
```python
note = Notes.objects.get(pk=3)
note
```
**Output:**
```python
<Notes: Notes object (3)>
```
💡 `pk` = primary key (usually the `id` field).

---

### 3. Fetch the First Record
```python
note = Notes.objects.first()
note
```
**Output:**
```python
<Notes: Notes object (3)>
```

---

### 4. View All Field Values of an Object
```python
note.__dict__
```
**Output:**
```python
{
  '_state': <django.db.models.base.ModelState object>,
  'id': 3,
  'title': 'added note',
  'text': 'i have added this today!',
  'created': datetime.datetime(2025, 11, 27, 16, 15, 51, 312455, tzinfo=datetime.timezone.utc),
  'user_id': 1
}
```

---

##  Key Takeaways
- `objects.all()` → returns all rows  
- `objects.get(pk=ID)` → fetches a single row by primary key  
- `objects.first()` → fetches the first row  
- `__dict__` → reveals all field values of a model instance  

---

## Basic Model Operations

### Import Your Models

```python
from notes.models import Notes
from django.contrib.auth.models import User
```

### Create Data

#### Method 1: Create and Save
```python
# Create a new note
note = Notes()
note.title = "My First Note"
note.text = "This is the content of my first note"
note.save()
```

#### Method 2: Create in One Line
```python
# Create and save in one step
note = Notes.objects.create(
    title="Second Note",
    text="Content of second note"
)
```

#### Method 3: Using get_or_create
```python
# Create only if it doesn't exist
note, created = Notes.objects.get_or_create(
    title="Unique Note",
    defaults={'text': 'This note is unique'}
)
print(f"Created: {created}")  # True if new, False if existed
```

### Query Data

#### Get All Objects
```python
# Get all notes
all_notes = Notes.objects.all()
print(all_notes)
```

#### Get Single Object
```python
# Get by ID
note = Notes.objects.get(id=1)

# Get by title
note = Notes.objects.get(title="My First Note")
```

#### Filter Objects
```python
# Filter by title containing text
notes = Notes.objects.filter(title__contains="First")

# Filter by date
from datetime import date
today_notes = Notes.objects.filter(created__date=date.today())

# Multiple filters
notes = Notes.objects.filter(title__contains="Note", text__isnull=False)
```

#### Advanced Queries
```python
# Exclude certain records
notes = Notes.objects.exclude(title="Second Note")

# Order by field
notes = Notes.objects.order_by('created')  # Ascending
notes = Notes.objects.order_by('-created')  # Descending

# Limit results
first_5_notes = Notes.objects.all()[:5]

# Count objects
count = Notes.objects.count()
```

### Update Data

#### Update Single Object
```python
note = Notes.objects.get(id=1)
note.title = "Updated Title"
note.save()
```

#### Bulk Update
```python
# Update multiple objects
Notes.objects.filter(title__contains="Note").update(text="Updated content")
```

### Delete Data

#### Delete Single Object
```python
note = Notes.objects.get(id=1)
note.delete()
```

#### Bulk Delete
```python
# Delete multiple objects
Notes.objects.filter(title__contains="temp").delete()

# Delete all (be careful!)
Notes.objects.all().delete()
```

## Working with Related Models

### User Operations
```python
# Create user
user = User.objects.create_user(
    username='testuser',
    email='test@example.com',
    password='testpass123'
)

# Get user
user = User.objects.get(username='testuser')
```

## Useful Shell Commands

### Check Model Fields
```python
# See all fields of a model
print(Notes._meta.fields)

# Get field names
field_names = [f.name for f in Notes._meta.fields]
print(field_names)
```

### Raw SQL Queries
```python
# Execute raw SQL
notes = Notes.objects.raw('SELECT * FROM notes_notes WHERE title LIKE %s', ['%Note%'])
```

### Database Inspection
```python
# Check database tables
from django.db import connection
cursor = connection.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())
```

## Common Query Patterns

### Field Lookups
```python
# Exact match
Notes.objects.filter(title__exact="My Note")

# Case-insensitive
Notes.objects.filter(title__iexact="my note")

# Contains
Notes.objects.filter(text__contains="django")

# Starts with / Ends with
Notes.objects.filter(title__startswith="My")
Notes.objects.filter(title__endswith="Note")

# Date/Time queries
from datetime import datetime, timedelta
yesterday = datetime.now() - timedelta(days=1)
Notes.objects.filter(created__gte=yesterday)
```

### Aggregation
```python
from django.db.models import Count, Avg, Max, Min

# Count notes
count = Notes.objects.aggregate(Count('id'))

# Latest note
latest = Notes.objects.aggregate(Max('created'))
```

## Shell Tips

### Save Time with Imports
Create a shell script to auto-import common models:

```python
# In shell_plus (if using django-extensions)
python manage.py shell_plus
```

### Pretty Print QuerySets
```python
# Format output nicely
for note in Notes.objects.all():
    print(f"ID: {note.id}, Title: {note.title}, Created: {note.created}")
```

### Check SQL Queries
```python
# See the actual SQL being generated
from django.db import connection
print(connection.queries)
```

## Exit Shell
```python
exit()
# or Ctrl+D
```

## Common Errors and Solutions

- **DoesNotExist**: Use `get()` carefully, consider `filter().first()`
- **MultipleObjectsReturned**: Use `filter()` instead of `get()`
- **IntegrityError**: Check required fields and constraints

