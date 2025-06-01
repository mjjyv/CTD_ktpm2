# Product Management API

API RESTful để quản lý sản phẩm sử dụng Flask và SQLite.

## Cài đặt

1. Tạo môi trường ảo:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows

2. Cài đặt dependencies:
pip install -r requirements.txt

3. Chạy ứng dụng:
./run.sh


## Troubleshooting

- **Permission denied for run.sh**:
  ```bash
  chmod +x run.sh


rm products.db


pytest

pylint src/ tests/




## API POSTMAN



product-api/
└── tests/
    └── postman/
        ├── ProductManagementAPI.postman_collection.json
        └── Local.postman_environment.json

./run.sh
newman run tests/postman/ProductManagementAPI.postman_collection.json -e tests/postman/Local.postman_environment.json


git add .
git commit -m "Minor update"
git push origin main