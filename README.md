# Django REST Framework - Dive into APIs & Customization
This repository contains the source code and documentation for the Django REST Framework (DRF) development. Building upon the basic API structure established in the first section, this phase implements relational models, Class-Based Views (CBVs), generic views, mixins, and robust authentication/permission workflows.
## Key Features & Implementation
* Class-Based Views (CBVs): Transitioned API views from function-based to `APIView` class-based structures, increasing modularity, reusability, and code readability.
* Mixins & Generic Views: Integrated DRF’s built-in `mixins` and concrete generic views (e.g., `ListCreateAPIView`, `RetrieveUpdateDestroyAPIView`) to eliminate boilerplate code.
* Relational Serializers: Implemented relational mappings (Foreign Keys) between models using dynamic approaches like `Nested Serializers` and `PrimaryKeyRelatedField`.
* Authentication & Permissions: Secured API endpoints using default permission policies like `IsAuthenticated` and `IsAuthenticatedOrReadOnly`.
* Implemented a Custom Permission class to restrict write access (`PUT`, `PATCH`, `DELETE`) exclusively to the object's creator.

##Tech Stack

* **Python**
* **Django**
* **Django REST Framework**




<img width="1607" height="871" alt="11" src="https://github.com/user-attachments/assets/4074759e-3dd6-4759-9345-4c0983b6fbd8" />
<img width="740" height="796" alt="22" src="https://github.com/user-attachments/assets/3a3aca0f-759e-4a42-b19e-aff74c9086cc" />
<img width="1888" height="862" alt="fake_user" src="https://github.com/user-attachments/assets/56983224-87e5-4370-bff9-15f748297081" />
<img width="1124" height="868" alt="Ekran görüntüsü 2026-06-25 135420" src="https://github.com/user-attachments/assets/afe5cdf6-1ff3-494b-8f3b-f77ea7189841" />

