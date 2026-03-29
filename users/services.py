from .models import User
from .serializers import UserSerializer
from .utils import validate_csv_file, parse_csv
from django.db import transaction

def process_csv(file):
    """
    Main service function to process the CSV upload.
    """
    validate_csv_file(file=file)
    
    rows = parse_csv(file=file)
    
    existing_emails = set(User.objects.values_list("email", flat=True))
    
    seen_emails = set()
    valid_onjects = []
    errors = []
    
    success_count, failure_count = 0,0
    
    for row_number, row_data in rows:
        email = row_data.get("email","").strip().lower()
        row_data["email"] = email
        serializer = UserSerializer(data=row_data)   
    
        if not serializer.is_valid():
            errors.append({"row":row_number, "errors":serializer.errors})
            failure_count+= 1
            continue
    
        validated_data = serializer.validated_data
        email = validated_data["email"]
        
        if email in existing_emails or email in seen_emails:
            errors.append({"row":row_number, "errors":{"email": ["Skipping duplicate email"]}})
            failure_count+= 1
            continue
        
        seen_emails.add(email)
        
        user = User(**validated_data)
        valid_onjects.append(user)
    
    with transaction.atomic():
        User.objects.bulk_create(valid_onjects)
        
    success_count = len(valid_onjects)
    
    return {
        "success_count": success_count,
        "failure_count": failure_count,
        "errors": errors
    }
        