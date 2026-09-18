from fastapi import APIRouter

router = APIRouter(prefix="/users")


@router.get("/me")
def get_me():
    pass

@router.put("/me")
def update_me():
    pass

@router.delete("/me")
def delete_me():
    pass
