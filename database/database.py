from typing import List, Union

from beanie import PydanticObjectId

from models.admin import Admin
from models.user import User
from models.role import Role
from models.permission import Permission
from models.company import Company
from models.local import Local
from models.category import Category
from models.product import Product

admin_collection = Admin
user_collection = User
role_collection = Role
permission_collection = Permission
company_collection = Company
local_collection = Local
category_collection = Category
product_collection = Product


async def add_admin(new_admin: Admin) -> Admin:
    admin = await new_admin.create()
    return admin

async def update_admin_data(id: PydanticObjectId, data: dict) -> Union[bool, Admin]:
    des_body = {k: v for k, v in data.items() if v is not None}
    update_query = {"$set": {field: value for field, value in des_body.items()}}
    admin = await admin_collection.get(id)
    if admin:
        await admin.update(update_query)
        return admin
    return False

# async def update_admin_password(id: PydanticObjectId) -> Admin:
#     admin = await admin_collection.get(id)
#     if admin:
#         return admin



############################### User Schema #############################

async def retrieve_users() -> List[User]:
    users = await user_collection.all().to_list()
    return users

async def add_user(new_user: User) -> User:
    user = await new_user.create()
    return user

async def retrieve_user(id: PydanticObjectId) -> User:
    user = await user_collection.get(id)
    if user:
        return user

async def delete_user(id: PydanticObjectId) -> bool:
    user = await user_collection.get(id)
    if user:
        await user.delete()
        return True

async def update_user_data(id: PydanticObjectId, data: dict) -> Union[bool, User]:
    des_body = {k: v for k, v in data.items() if v is not None}
    update_query = {"$set": {field: value for field, value in des_body.items()}}
    user = await user_collection.get(id)
    if user:
        await user.update(update_query)
        return user
    return False

############################### Fin User Schema #############################

############################### Role Schema #################################

async def retrieve_roles() -> List[Role]:
    roles = await role_collection.all().to_list()
    return roles

async def add_role(new_role: Role) -> Role:
    role = await new_role.create()
    return role

async def retrieve_role(id: PydanticObjectId) -> Role:
    role = await role_collection.get(id)
    if role:
        return role

async def delete_role(id: PydanticObjectId) -> bool:
    role = await role_collection.get(id)
    if role:
        await role.delete()
        return True

async def update_role_data(id: PydanticObjectId, data: dict) -> Union[bool, Role]:
    des_body = {k: v for k, v in data.items() if v is not None}
    update_query = {"$set": {field: value for field, value in des_body.items()}}
    role = await role_collection.get(id)
    if role:
        await role.update(update_query)
        return role
    return False

############################### Fin Role Schema #############################

############################### Permission Schema ###########################

async def retrieve_permissions() -> List[Permission]:
    permissions = await permission_collection.all().to_list()
    return permissions


async def add_permission(new_permission: Permission) -> Permission:
    permission = await new_permission.create()
    return permission


async def retrieve_permission(id: PydanticObjectId) -> Permission:
    permission = await permission_collection.get(id)
    if permission:
        return permission


async def delete_permission(id: PydanticObjectId) -> bool:
    permission = await permission_collection.get(id)
    if permission:
        await permission.delete()
        return True


async def update_permission_data(id: PydanticObjectId, data: dict) -> Union[bool, Permission]:
    des_body = {k: v for k, v in data.items() if v is not None}
    update_query = {"$set": {field: value for field, value in des_body.items()}}
    permission = await permission_collection.get(id)
    if permission:
        await permission.update(update_query)
        return permission
    return False

############################### Fin Permission Schema #############################

############################### Company Schema ####################################

async def retrieve_companys() -> List[Company]:
    companys = await company_collection.all().to_list()
    return companys


async def add_company(new_company: Company) -> Company:
    company = await new_company.create()
    return company


async def retrieve_company(id: PydanticObjectId) -> Company:
    company = await company_collection.get(id)
    if company:
        return company


async def delete_company(id: PydanticObjectId) -> bool:
    company = await company_collection.get(id)
    if company:
        await company.delete()
        return True


async def update_company_data(id: PydanticObjectId, data: dict) -> Union[bool, Company]:
    des_body = {k: v for k, v in data.items() if v is not None}
    update_query = {"$set": {field: value for field, value in des_body.items()}}
    company = await company_collection.get(id)
    if company:
        await company.update(update_query)
        return company
    return False

############################### Fin Company Schema ##############################

############################### Local Schema ####################################

async def retrieve_locals() -> List[Local]:
    locals = await local_collection.all().to_list()
    return locals


async def add_local(new_local: Local) -> Local:
    local = await new_local.create()
    return local


async def retrieve_local(id: PydanticObjectId) -> Local:
    local = await local_collection.get(id)
    if local:
        return local


async def delete_local(id: PydanticObjectId) -> bool:
    local = await local_collection.get(id)
    if local:
        await local.delete()
        return True


async def update_local_data(id: PydanticObjectId, data: dict) -> Union[bool, Local]:
    des_body = {k: v for k, v in data.items() if v is not None}
    update_query = {"$set": {field: value for field, value in des_body.items()}}
    local = await local_collection.get(id)
    if local:
        await local.update(update_query)
        return local
    return False

############################### Fin Local Schema ################################

############################### Category Schema #################################

async def retrieve_categories() -> List[Category]:
    categories = await category_collection.all().to_list()
    return categories


async def add_category(new_category: Category) -> Category:
    category = await new_category.create()
    return category


async def retrieve_category(id: PydanticObjectId) -> Category:
    category = await category_collection.get(id)
    if category:
        return category


async def delete_category(id: PydanticObjectId) -> bool:
    category = await category_collection.get(id)
    if category:
        await category.delete()
        return True


async def update_category_data(id: PydanticObjectId, data: dict) -> Union[bool, Category]:
    des_body = {k: v for k, v in data.items() if v is not None}
    update_query = {"$set": {field: value for field, value in des_body.items()}}
    category = await category_collection.get(id)
    if category:
        await category.update(update_query)
        return category
    return False

############################### Fin Category Schema #############################

############################### Product Schema #################################

async def retrieve_products() -> List[Product]:
    products = await product_collection.all().to_list()
    return products


async def add_product(new_product: Product) -> Product:
    product = await new_product.create()
    return product


async def retrieve_product(id: PydanticObjectId) -> Product:
    product = await product_collection.get(id)
    if product:
        return product


async def delete_product(id: PydanticObjectId) -> bool:
    product = await product_collection.get(id)
    if product:
        await product.delete()
        return True


async def update_product_data(id: PydanticObjectId, data: dict) -> Union[bool, Product]:
    des_body = {k: v for k, v in data.items() if v is not None}
    update_query = {"$set": {field: value for field, value in des_body.items()}}
    product = await product_collection.get(id)
    if product:
        await product.update(update_query)
        return product
    return False

############################### Fin Product Schema #############################