from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from authentication.jwt_utils import get_current_user
from workspace.schemas import WorkspaceCreate
from workspace.models import Workspace
from authentication.models import User
from db import db_dependency


router = APIRouter(
    prefix="/workspace",
    tags=["workspace"],
    responses={404: {"description": "Not found"}},
)


@router.post("/create-workspace")
async def create_workspace(db: db_dependency, workspace: WorkspaceCreate, user : Annotated[User, Depends(get_current_user)]):
    try:
        workspace_obj = Workspace(
            name=workspace.name,
            description=workspace.description,
            user_id=user.id,
        )
        workspace_obj.save(db)
        return JSONResponse(
            {
                "message": "Workspace Created!",
                "data": {
                    "id": workspace_obj.id,
                    "name": workspace_obj.name,
                    "description": workspace_obj.description,
                },
            }
        )
    except Exception as e:
        return JSONResponse({"error": str(e)})
    
