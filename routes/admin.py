from fastapi import Body, APIRouter, HTTPException
from passlib.context import CryptContext

from auth.jwt_handler import sign_jwt
from database.database import add_admin
from models.admin import Admin, AdminData, AdminSignIn

router = APIRouter()

hash_helper = CryptContext(schemes=["bcrypt"])


@router.post("/login")
async def admin_login(admin_credentials: AdminSignIn = Body(...)):
    admin_exists = await Admin.find_one(Admin.email == admin_credentials.username)
    if admin_exists:
        password = hash_helper.verify(admin_credentials.password, admin_exists.password)
        if password:
            return sign_jwt(admin_credentials.username, admin_exists.name)

        raise HTTPException(status_code=403, detail="Incorrect email or password")

    raise HTTPException(status_code=403, detail="Incorrect email or password")


@router.post("/new", response_model=AdminData)
async def admin_signup(admin: Admin = Body(...)):
    admin_exists = await Admin.find_one(Admin.email == admin.email)
    if admin_exists:
        raise HTTPException(
            status_code=409, detail="Admin with email supplied already exists"
        )

    admin.password = hash_helper.encrypt(admin.password)
    new_admin = await add_admin(admin)
    return new_admin

# @router.put("/{id}", response_model=Response)
# async def change_admin_password(id: PydanticObjectId, req: UpdateUserPassword = Body(...)):
#     # change_admin_password = await update_admin_data(id, req.dict())
#     print(change_admin_password)
#     # updated_admin = await update_admin_password(id)
    
#     # async def get_user_data(id: PydanticObjectId):
#     # user = await retrieve_user(id)
    
    
#     if change_admin_password:
#         return {
#             "status_code": 200,
#             "response_type": "success",
#             "description": "Users with ID: {} updated".format(id),
#             "data": change_admin_password,
#         }
#     return {
#         "status_code": 404,
#         "response_type": "error",
#         "description": "An error occurred. Users with ID: {} not found".format(id),
#         "data": False,
#     }


# @router.put("/{id}", response_model=Response)
# async def update_admin(id: PydanticObjectId, req: UpdateUserPassword = Body(...)):
#     updated_admin = await update_admin_data(id, req.dict())
#     if updated_admin:
#         return {
#             "status_code": 200,
#             "response_type": "success",
#             "description": "Users with ID: {} updated".format(id),
#             "data": updated_admin,
#         }
#     return {
#         "status_code": 404,
#         "response_type": "error",
#         "description": "An error occurred. Users with ID: {} not found".format(id),
#         "data": False,
#     }

# @router.post("/refresh")
# async def admin_refresh(Authorize: RefreshToken = Body(...)):
#         current_user = Authorize.get_jwt_subject()
#         new_access_token = Authorize.create_access_token(subject=current_user)
#         # return refresh_jwt(current_user,new_access_token)
#  
